import discord
import random 
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    dicas = [
        "Desligue as luzes de cômodos vazios.",
        "Reutilize potes de vidro como organizadores.",
        "Tome banhos mais curtos pra economizar água.",
        "Use transporte público ou bicicleta sempre que possível.",
        "Recicle papel, plástico e vidro.",
        "Plante árvores e cuide do meio ambiente.",
        "Evite produtos descartáveis, prefira reutilizáveis.",
        "Compre produtos locais e da estação.",
        "Reduza o consumo de carne e prefira alimentos orgânicos.",
        "Doe roupas e objetos que você não usa mais."
    ]
    
    tempos_decomposicao = {
    "garrafa pet": "450 anos",
    "lata de aluminio": "200 anos",
    "papel": "3 a 6 meses",
    "chiclete": "5 anos",
    "cigarro": "1 a 5 anos",
    "sacola plastica": "10 a 20 anos",
    "vidro": "1 milhão de anos",
    "pneu": "1000 anos",
}

    compostavel = {
    "casca de banana": True,
    "borra de cafe": True,
    "papel": True,
    "carne": False,
    "plastico": False,
    "vidro": False,

}

    if message.content.startswith('$oi'):
        await message.channel.send("Oi! Eu sou o EcoBot 🌱")
    elif message.content.startswith('$dica'):
        await message.channel.send(random.choice(dicas))
    elif message.content.startswith('$decompoe'):
        partes = message.content.split(' ', 1)
        item = partes[1].lower()
        resultado = tempos_decomposicao.get(item, "Não tenho essa informação ainda.")
        await message.channel.send(resultado)
    elif message.content.startswith('$compostagem'):
        partes = message.content.split(' ', 1)
        item = partes[1].lower()
        pode = compostavel.get(item)
        if pode is None:
            await message.channel.send("Não sei sobre esse item ainda.")
        elif pode:
            await message.channel.send(f"Sim! {item} pode ir na composteira.")
        else:
            await message.channel.send(f"Não, {item} não deve ir na composteira.")
    else:
        await message.channel.send(message.content)


client.run(TOKEN)
