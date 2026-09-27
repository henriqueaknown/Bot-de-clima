# Importa as bibliotecas necessárias
import discord
from discord.ext import commands
import requests
import pyttsx3


# Inicializa o sintetizador de voz
engine = pyttsx3.init()


# Inicializa o objeto do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Função para obter a previsão do tempo usando a API wttr.in
def get_weather(city: str) -> str:
    """
    Obtém informações meteorológicas para a cidade especificada.

    Parâmetros:
    city (str): Nome da cidade

    Retorna:
    str: Informações meteorológicas ou uma mensagem de erro
    """

    base_url = f"https://wttr.in/{city}?format=%C+%t"

    response = requests.get(base_url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Não foi possível obter os dados meteorológicos. Tente novamente mais tarde."


# Função para síntese de fala
def speak(text: str):
    """
    Converte o texto fornecido em fala usando a biblioteca pyttsx3.

    Parâmetros:
    text (str): Texto que será reproduzido por voz
    """

    engine.say(text)
    engine.runAndWait()


# Comando para obter a previsão do tempo
@bot.command()
async def weather(ctx, *, city: str):
    """
    Comando para obter informações meteorológicas e reproduzi-las em voz.

    Parâmetros:
    ctx: Contexto do comando
    city (str): Nome da cidade
    """

    weather_info = get_weather(city)

    await ctx.send(
        f"Tempo em {city}: {weather_info}"
    )

    speak(weather_info)


# Inicia o bot
bot.run("YOUR_BOT_TOKEN")
