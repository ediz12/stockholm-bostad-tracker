from typing import TYPE_CHECKING
from discord.ext import tasks, commands
import asyncio
import logging
import settings

if TYPE_CHECKING:
    from main import DiscordBot
log = logging.getLogger()


class CheckForNewHousingCog(commands.Cog):
    def __init__(self, bot: "DiscordBot"):
        self.bot = bot
        self.stockholm_housing_service = self.bot.stockholm_housing_service
        self.embed_service = self.bot.embed_service
        self.check_for_new_housing_task.start()

    def cog_unload(self):
        self.check_for_new_housing_task.cancel()
        log.warning("Check For New Housing Task is unloaded.")

    @tasks.loop(seconds=60)
    async def check_for_new_housing_task(self):
        total_apartments, apartments = self.stockholm_housing_service.check_for_new_housing()
        embeds = [self.embed_service.convert_apartment_to_embed(apartment) for apartment in apartments]

        guild = self.bot.get_guild(settings.DISCORD_GUILD_ID)
        channel = guild.get_channel(settings.DISCORD_CHANNEL_ID)
        for i in range(0, total_apartments, 10):
            await channel.send("-" * 75, embeds=embeds[i: min(i+10, total_apartments)])

    @check_for_new_housing_task.before_loop
    async def wait_for_load(self):
        await self.bot.wait_until_ready()
        log.info("Check For New Housing Task ready, giving it time to load cache...")
        await asyncio.sleep(1)
        log.info("Check For New Housing Task started.")

    @commands.Cog.listener()
    async def on_ready(self):
        log.info("Connected as: {}".format(self.bot.user))
