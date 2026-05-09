import discord
from discord.ext import commands
import random
import os

# 1. Bot-Konfiguration
# Wir aktivieren die Intents, damit Koneko Nachrichten lesen und Mitglieder sehen kann
intents = discord.Intents.default()
intents.message_content = True  # Wichtig für Befehle wie !hug
intents.members = True          # Wichtig für das Wirtschaftssystem

# Das Präfix für deine Befehle (wie bei Nekotina)
bot = commands.Bot(command_prefix='!', intents=intents)

# 2. Event: Wenn der Bot startet
@bot.event
async def on_ready():
    print(f'Koneko ist online als {bot.user}!')
    # Setzt den Status, den man in der Vorlage sieht
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name="auf 4 Mio. Servern | !help"
        )
    )

# 3. Social Commands (Interaktionen)
@bot.command()
async def hug(ctx, member: discord.Member):
    """Umarmt ein anderes Mitglied mit einem schönen Embed"""
    # Hier kannst du Anime-GIF Links einfügen
    hugs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW94bmZ6bmZ6bmZ6&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"
    ]
    embed = discord.Embed(
        description=f"🐾 {ctx.author.mention} gibt {member.mention} eine ganz feste Umarmung!",
        color=0xFFB6C1  # Das Pastell-Rosa deiner Webseite
    )
    embed.set_image(url=random.choice(hugs))
    await ctx.send(embed=embed)

@bot.command()
async def pat(ctx, member: discord.Member):
    """Tätschelt jemandem den Kopf (Nyaa~ Effekt)"""
    embed = discord.Embed(
        description=f"✨ {ctx.author.mention} tätschelt {member.mention} sanft den Kopf. Nyaa~",
        color=0xFFB6C1
    )
    await ctx.send(embed=embed)

# 4. Economy System (Basis)
@bot.command()
async def daily(ctx):
    """Gibt dem User seine täglichen Pfoten-Coins"""
    # Später kannst du hier eine Datenbank-Verbindung einbauen
    await ctx.send(f"✨ **{ctx.author.name}**, du hast deine täglichen **100 Pfoten-Coins** erhalten! 🐾")

# 5. Start des Bots
# Nutzt den Token aus den Umgebungsvariablen für maximale Sicherheit auf GitHub
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN:
    bot.run(TOKEN)
else:
    print("FEHLER: Kein DISCORD_TOKEN in den Umgebungsvariablen gefunden!")
