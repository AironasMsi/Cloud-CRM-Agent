"""
Cloud CRM & Operations Agent - 24/7 Autonomous Team Workflow Engine
Hosted on Oracle Cloud VPS under Linux systemd daemon service.
"""
import os
import sys
import logging
import asyncio
import discord
from discord.ext import commands
from config import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("cloud_crm.bot")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info("Bot authenticated as: %s (ID: %s)", bot.user.name, bot.user.id)
    logger.info("Deployment Target: %s (%s)", config.HOST_ENVIRONMENT, config.DEPLOYMENT_REGION)
    logger.info("SQLite WAL Database Connection Pool Ready.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pipeline & Emails"))

async def main():
    async with bot:
        await bot.start(config.DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
