import datetime
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot_logic import gen_pass

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
        "`/clear [quantidade]` — apaga mensagens do canal\n"
        "`/mute @membro minutos [motivo]` — silencia um membro por um tempo\n"
        "`/warn @membro motivo` — envia um aviso por DM a um membro\n"
        "`/unban id_do_usuario [motivo]` — remove o banimento de um usuário\n"
        "`/ping` — mostra a latência do bot\n"
        "`/userinfo [@membro]` — mostra informações de um membro\n"
        "`/serverinfo` — mostra informações do servidor\n"
        "`/avatar [@membro]` — mostra o avatar de um membro\n"
        "`/dado [lados]` — rola um dado\n"
        "`/poll pergunta` — cria uma enquete de sim/não\n"
        "`/senha [tamanho]` — gera uma senha aleatória (privado)"
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


@bot.hybrid_command(name="mute", description="Silencia um membro por um tempo (timeout)")
@commands.has_permissions(moderate_members=True)
async def mute(ctx: commands.Context, membro: discord.Member, minutos: int, *, motivo: str = "Não especificado"):
    await membro.timeout(datetime.timedelta(minutes=minutos), reason=motivo)
    await ctx.send(f"🔇 {membro.mention} foi silenciado por {minutos} minuto(s). Motivo: {motivo}", ephemeral=True)


@bot.hybrid_command(name="warn", description="Envia um aviso por DM a um membro")
@commands.has_permissions(moderate_members=True)
async def warn(ctx: commands.Context, membro: discord.Member, *, motivo: str):
    try:
        await membro.send(f"⚠️ Você recebeu um aviso em **{ctx.guild.name}**. Motivo: {motivo}")
        entregue = True
    except discord.Forbidden:
        entregue = False

    aviso = f"⚠️ {membro.mention} foi avisado. Motivo: {motivo}"
    if not entregue:
        aviso += "\n(Não consegui mandar DM — a pessoa deve estar com DMs fechadas.)"
    await ctx.send(aviso, ephemeral=True)


@bot.hybrid_command(name="unban", description="Remove o banimento de um usuário pelo ID")
@commands.has_permissions(ban_members=True)
async def unban(ctx: commands.Context, id_do_usuario: str, *, motivo: str = "Não especificado"):
    try:
        usuario = await bot.fetch_user(int(id_do_usuario))
        await ctx.guild.unban(usuario, reason=motivo)
        await ctx.send(f"✅ {usuario.mention} foi desbanido. Motivo: {motivo}", ephemeral=True)
    except ValueError:
        await ctx.send("❓ ID inválido — precisa ser só números.", ephemeral=True)
    except discord.NotFound:
        await ctx.send("❓ Esse usuário não está banido.", ephemeral=True)


@bot.hybrid_command(name="ping", description="Mostra a latência do bot")
async def ping(ctx: commands.Context):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")


@bot.hybrid_command(name="userinfo", description="Mostra informações de um membro")
async def userinfo(ctx: commands.Context, membro: discord.Member = None):
    membro = membro or ctx.author
    embed = discord.Embed(title=str(membro), color=membro.color)
    embed.set_thumbnail(url=membro.display_avatar.url)
    embed.add_field(name="ID", value=membro.id, inline=False)
    embed.add_field(name="Conta criada em", value=discord.utils.format_dt(membro.created_at, "D"), inline=False)
    embed.add_field(name="Entrou no servidor em", value=discord.utils.format_dt(membro.joined_at, "D"), inline=False)
    embed.add_field(name="Cargo mais alto", value=membro.top_role.mention, inline=False)
    await ctx.send(embed=embed)


@bot.hybrid_command(name="serverinfo", description="Mostra informações do servidor")
async def serverinfo(ctx: commands.Context):
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, color=discord.Color.blurple())
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Dono", value=guild.owner.mention if guild.owner else "Desconhecido", inline=False)
    embed.add_field(name="Membros", value=guild.member_count, inline=False)
    embed.add_field(name="Criado em", value=discord.utils.format_dt(guild.created_at, "D"), inline=False)
    await ctx.send(embed=embed)


@bot.hybrid_command(name="avatar", description="Mostra o avatar de um membro")
async def avatar(ctx: commands.Context, membro: discord.Member = None):
    membro = membro or ctx.author
    embed = discord.Embed(title=f"Avatar de {membro.display_name}", color=membro.color)
    embed.set_image(url=membro.display_avatar.url)
    await ctx.send(embed=embed)


@bot.hybrid_command(name="dado", description="Rola um dado")
async def dado(ctx: commands.Context, lados: int = 6):
    if lados < 2:
        await ctx.send("❓ O dado precisa ter pelo menos 2 lados.", ephemeral=True)
        return
    resultado = random.randint(1, lados)
    await ctx.send(f"🎲 Você tirou **{resultado}** (dado de {lados} lados)")


@bot.hybrid_command(name="poll", description="Cria uma enquete de sim/não")
async def poll(ctx: commands.Context, *, pergunta: str):
    embed = discord.Embed(title="📊 Enquete", description=pergunta, color=discord.Color.blurple())
    embed.set_footer(text=f"Criada por {ctx.author.display_name}")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


@bot.hybrid_command(name="senha", description="Gera uma senha aleatória")
async def senha(ctx: commands.Context, tamanho: int = 12):
    if not 4 <= tamanho <= 64:
        await ctx.send("❓ Escolhe um tamanho entre 4 e 64.", ephemeral=True)
        return
    await ctx.send(f"🔑 Sua senha: `{gen_pass(tamanho)}`", ephemeral=True)


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