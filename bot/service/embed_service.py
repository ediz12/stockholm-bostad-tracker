from bot.model.apartment import Apartment
import discord
import settings


class EmbedService(object):
    def __init__(self):
        pass

    def convert_apartment_to_embed(self, apartment: Apartment) -> discord.Embed:
        embed = discord.Embed(title=f"💰 Rent: {apartment.rent} kr / month")
        embed.set_author(name=f"🏙️ {apartment.municipality}, {apartment.district} - {apartment.address}", url=settings.BOSTAD_STOCKHOLM_DETAILS_URL.format(a_id=apartment.a_id))
        embed.add_field(name=f"🏢 Floor: {apartment.floor}", value="---", inline=True)
        embed.add_field(name=f"🚪 Total rooms: {apartment.total_rooms}", value="---", inline=True)
        embed.add_field(name=f"🔢 Sqm: {apartment.sqm}", value="---", inline=True)
        embed.add_field(name="📅 Last application date", value=apartment.last_application_date, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="ℹ Other details", value=self._get_other_details(apartment), inline=True)
        embed.add_field(name="🗺️ Google Maps", value=settings.GOOGLE_MAPS_LOCATION_URL.format(
            latitude=apartment.latitude, longitude=apartment.longitude), inline=False)

        return embed

    def _get_other_details(self, apartment: Apartment):
        details = []
        if apartment.new_production:
            details.append("🆕 New production")
        if apartment.has_balcony:
            details.append("💺 Has balcony")
        if apartment.has_elevator:
            details.append("🛗 Has elevator")
        if len(details) == 0:
            details = "No balcony, no elevator and not new production"
        return ", ".join(details)
