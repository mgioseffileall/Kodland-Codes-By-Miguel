import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


GUILD_ID = discord.Object(id=1549162712712486953)


@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')
    bot.tree.copy_global_to(guild=GUILD_ID)
    synced = await bot.tree.sync(guild=GUILD_ID)
    print(f'{len(synced)} comando(s) de barra sincronizado(s) no servidor.')


@bot.hybrid_command(name="hello", description="O bot diz oi")
async def hello(ctx: commands.Context):
    await ctx.send("Oi! Como você está?")


@bot.hybrid_command(name="bye", description="O bot se despede")
async def bye(ctx: commands.Context):
    await ctx.send("Tchau! Até mais!" + " " + "\U0001F44B") 


@bot.hybrid_command(name="comandos", description="Mostra a lista de comandos disponíveis")
async def comandos(ctx: commands.Context):
    await ctx.send(
        "**Comandos disponíveis:**\n"
        "`/hello` — o bot responde 'Oi!'\n"
        "`/bye` — o bot responde com um emoji de tchau\n"
        "`/comandos` — mostra essa lista\n"
        "`/kick @membro [motivo]` — expulsa um membro (confirmação só sua)\n"
        "`/ban @membro [motivo]` — bane um membro (confirmação só sua)\n"
        "`/clear [quantidade]` — apaga mensagens do canal"
    )


class ConfirmView(discord.ui.View):
    def __init__(self, author: discord.Member):
        super().__init__(timeout=30)
        self.author = author
        self.value = None
        self.message: discord.Message | None = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("Esse botão não é seu.", ephemeral=True)
            return False
        return True

    async def on_timeout(self):
        if self.message:
            await self.message.edit(content="⏱️ Tempo esgotado, nada foi feito.", view=None)

    @discord.ui.button(label='Confirmar', style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
        await interaction.response.defer()

    @discord.ui.button(label='Cancelar', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = False
        self.stop()
        await interaction.response.edit_message(content="Cancelado.", view=None)


@bot.hybrid_command(name="kick", description="Expulsa um membro do servidor")
@commands.has_permissions(kick_members=True)
async def kick(ctx: commands.Context, membro: discord.Member, *, motivo: str = "Não especificado"):
    view = ConfirmView(ctx.author)
    view.message = await ctx.send(f"Expulsar {membro.mention}? Motivo: {motivo}", view=view, ephemeral=True)
    await view.wait()
    if view.value:
        await membro.kick(reason=motivo)
        await view.message.edit(content=f"👢 {membro.mention} foi expulso. Motivo: {motivo}", view=None)


@bot.hybrid_command(name="ban", description="Bane um membro do servidor")
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, membro: discord.Member, *, motivo: str = "Não especificado"):
    view = ConfirmView(ctx.author)
    view.message = await ctx.send(f"Banir {membro.mention}? Motivo: {motivo}", view=view, ephemeral=True)
    await view.wait()
    if view.value:
        await membro.ban(reason=motivo)
        await view.message.edit(content=f"🔨 {membro.mention} foi banido. Motivo: {motivo}", view=None)

@bot.hybrid_command(name="clear", description="Apaga uma quantidade de mensagens do canal")
@commands.has_permissions(manage_messages=True)
async def clear(ctx: commands.Context, quantidade: int):
    is_slash = ctx.interaction is not None
    if is_slash:
        await ctx.defer(ephemeral=True)

    limite = quantidade if is_slash else quantidade + 1  
    apagadas = await ctx.channel.purge(limit=limite)
    contagem = len(apagadas) if is_slash else len(apagadas) - 1

    msg = await ctx.send(f"🧹 {contagem} mensagens apagadas.", ephemeral=True)
    if not is_slash:
        await msg.delete(delay=3)


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("🚫 Você não tem permissão pra usar esse comando.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("❓ Não achei esse membro. Confere se digitou certo ou usa @menção.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❓ Faltou um argumento: `{error.param.name}`.")
    else:
        print(f"Erro não tratado: {error}")

bot.run(TOKEN)