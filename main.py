# COGS
from bot.cogs.check_for_new_housing import CheckForNewHousingCog

# SERVICES
from bot.service.stockholm_housing_service import StockholmHousingService
from bot.service.embed_service import EmbedService

# SETTINGS
from settings import DISCORD_TOKEN

# OTHER
from discord.ext import commands
import discord
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(fmt='%(levelname)s: %(module)s.%(funcName)s :: %(message)s'))
log.addHandler(stream_handler)


class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), owner_id=67011588523032576,
                         strip_after_prefix=True)

        self.stockholm_housing_service = StockholmHousingService()
        self.embed_service = EmbedService()

    async def setup_hook(self) -> None:
        await self.add_cog(CheckForNewHousingCog(self))

    def begin(self) -> None:
        self.run(DISCORD_TOKEN)


bot = DiscordBot()
bot.begin()
