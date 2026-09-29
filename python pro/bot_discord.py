import discord
from bot_logic import gen_pass
import requests
import random
# A variável intents armazena as permissões do bot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")



intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

memes = ['memes/meme1.png', 'memes/meme2.png', 'memes/meme3.png', 'memes/meme4.png']

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pokemon'):
        partes = message.content.split(' ')
        nome = partes[1].lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
        resposta = requests.get(url)
        dados = resposta.json()
        tipos = [t['type']['name'] for t in dados['types']]
        await message.channel.send(
            f"**{dados['name']}**\n"
            f"Altura: {dados['height'] / 10} m\n"
            f"Peso: {dados['weight'] / 10} kg\n"
            f"Tipo(s): {', '.join(tipos)}\n"
            f"{dados['sprites']['front_default']}"
        )
    elif message.content.startswith('$meme'):
        pesos = [14, 9, 4, 3]
        escolhido = random.choices(memes, weights=pesos, k=1)[0]
        await message.channel.send(file=discord.File(escolhido))
    else:
        await message.channel.send(message.content)

client.run(TOKEN)
