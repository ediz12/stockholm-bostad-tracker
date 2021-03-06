from bot.model.apartment import Apartment
import discord
import settings


class EmbedService(object):
    def __init__(self):
        pass

    def convert_apartment_to_embed(self, apartment: Apartment) -> discord.Embed:
        embed = discord.Embed(title=f"π° Rent: {apartment.rent} kr / month")
        embed.set_author(name=f"ποΈ {apartment.municipality}, {apartment.district} - {apartment.address}", url=settings.BOSTAD_STOCKHOLM_DETAILS_URL.format(a_id=apartment.a_id))
        embed.add_field(name=f"π’ Floor: {apartment.floor}", value="---", inline=True)
        embed.add_field(name=f"πͺ Total rooms: {apartment.total_rooms}", value="---", inline=True)
        embed.add_field(name=f"π’ Sqm: {apartment.sqm}", value="---", inline=True)
        embed.add_field(name="π Last application date", value=apartment.last_application_date, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="βΉ Other details", value=self._get_other_details(apartment), inline=True)
        embed.add_field(name="πΊοΈ Google Maps", value=settings.GOOGLE_MAPS_LOCATION_URL.format(
            latitude=apartment.latitude, longitude=apartment.longitude), inline=False)

        return embed

    def _get_other_details(self, apartment: Apartment):
        details = []
        if apartment.new_production:
            details.append("π New production")
        if apartment.has_balcony:
            details.append("πΊ Has balcony")
        if apartment.has_elevator:
            details.append("π Has elevator")
        if len(details) == 0:
            details = "No balcony, no elevator and not new production"
        return ", ".join(details)
