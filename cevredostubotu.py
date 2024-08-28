import discord
import random
import os
from discord.ext import commands
from geopy.geocoders import Nominatim


# Discord botunu oluşturun
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Atık yönetimi komutları
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı.")

@bot.command(name="geridonusum")
async def geri_donusum_bilgisi(ctx):
    bilgi = """
    Geri Dönüşüm Bilgisi:
    Plastik, kağıt, cam, metal ve organik atıklar geri dönüşüme kazandırılabilir.
    Geri dönüşüm, doğal kaynakların korunmasına ve enerji tasarrufuna yardımcı olur.
    """
    await ctx.send(bilgi)

@bot.command(name="atikayristirma")
async def atik_ayristirma_bilgisi(ctx):
    bilgi = """
    Atık Ayrıştırma Bilgisi:
    - Plastik: Plastik şişeler, poşetler, ambalajlar.
    - Kağıt: Gazete, dergi, karton kutular.
    - Cam: Cam şişeler, kavanozlar.
    - Metal: Teneke kutular, alüminyum folyolar.
    - Organik: Yiyecek atıkları, bitki atıkları.
    """
    await ctx.send(bilgi)




bot.run("TOKEN")
