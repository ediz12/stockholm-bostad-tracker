import requests
import settings
import logging
from bot.model.apartment import Apartment
from bot.utils.file_utils import FileUtils


class StockholmHousingService(object):
    def __init__(self):
        self.file_utils = FileUtils()
        self.checked_apartments = self.file_utils.get_checked_apartments()

    def check_for_new_housing(self) -> list:
        try:
            response = requests.get(settings.BOSTAD_STOCKHOLM_HOUSING_LIST_URL)
            results = response.json()
            return self._filter_apartments(results)
        except Exception as e:
            logging.error("Error during house checks: ", e)
            return [0, list()]

    def _filter_apartments(self, apartments: list) -> list:
        filtered_apartments = {apartment["AnnonsId"]: apartment for apartment in apartments}
        total_apartments = 0

        for apartment in apartments:
            apt_id = apartment["AnnonsId"]
            if apt_id in self.checked_apartments:
                filtered_apartments.pop(apt_id)
                continue
            else:
                self.checked_apartments.append(apt_id)

            if not self._filter_by_apartment_type(apartment):
                filtered_apartments.pop(apt_id)
                continue

            if not self._filter_by_unwanted_areas(apartment):
                filtered_apartments.pop(apt_id)
                continue

            if not self._filter_by_apartment_details(apartment):
                filtered_apartments.pop(apt_id)
                continue

            total_apartments += apartment["Antal"]

        self.file_utils.set_checked_apartments(self.checked_apartments)

        new_apartments = [Apartment(a_id= apt["AnnonsId"], municipality=apt["Kommun"], district=apt["Stadsdel"], address=apt["Gatuadress"],
                                    rent=apt["Hyra"], floor=apt["Vaning"], total_rooms=apt["AntalRum"], sqm=apt["Yta"],
                                    last_application_date=apt["AnnonseradTill"], latitude=apt["KoordinatLatitud"],
                                    longitude=apt["KoordinatLongitud"], has_balcony=apt["Balkong"],
                                    has_elevator=apt["Hiss"], new_production=apt["Nyproduktion"],
                                    minimum_rent=apt["LägstaHyran"], maximum_rent=apt["HögstaHyran"],
                                    minimum_sqm=apt["LägstaYtan"], maximum_sqm=apt["HögstaYtan"],
                                    minimum_rooms=apt["LägstaAntalRum"], maximum_rooms=apt["HögstaAntalRum"])
                          for apt in filtered_apartments.values()]

        return [total_apartments, new_apartments]

    def _filter_by_apartment_type(self, apartment: dict):
        return (settings.SHOW_COMMON_APARTMENTS and apartment["Vanlig"]) or \
               (settings.SHOW_STUDENT_APARTMENTS and apartment["Student"]) or \
               (settings.SHOW_YOUTH_APARTMENTS and apartment["Ungdom"]) or \
               (settings.SHOW_SENIOR_APARTMENTS and apartment["Senior"]) or \
               (settings.SHOW_SHORT_TERM_APARTMENTS and apartment["Korttid"])

    def _filter_by_unwanted_areas(self, apartment: dict):
        return (apartment["Kommun"] not in settings.UNWANTED_MUNICIPALITIES) and \
               (apartment["Stadsdel"] not in settings.UNWANTED_DISTRICTS)

    def _filter_by_apartment_details(self, apartment: dict):
        if apartment["Yta"] and apartment["Yta"] < settings.MINIMUM_SQM:
            return False
        if apartment["AntalRum"] and apartment["AntalRum"] < settings.MINIMUM_ROOMS:
            return False
        if apartment["Hyra"] and settings.MINIMUM_RENT <= apartment["Hyra"] <= settings.MAXIMUM_RENT:
            return True
        if apartment["Vaning"] and apartment["Vaning"] < settings.MINIMUM_FLOOR:
            return False
        if apartment["LägstaHyran"] and apartment["LägstaHyran"] < settings.MINIMUM_RENT:
            return False
        if apartment["HögstaHyran"] and apartment["HögstaHyran"] > settings.MAXIMUM_RENT:
            return False
        if apartment["HögstaAntalRum"] and apartment["HögstaAntalRum"] < settings.MINIMUM_ROOMS:
            return False

        return True
