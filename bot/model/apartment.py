class Apartment(object):
    def __init__(self, a_id: int, municipality: str, district: str, address: str, rent: int, floor: int, total_rooms: int,
                 sqm: int, last_application_date: str, latitude: float, longitude: float, has_balcony: bool,
                 has_elevator: bool, new_production: bool, minimum_rent: int, maximum_rent: int, minimum_sqm: int,
                 maximum_sqm: int, minimum_rooms: int, maximum_rooms: int):
        self.a_id = a_id
        self.municipality = municipality
        self.district = district
        self.address = address
        self.rent = self._set_rent(rent, minimum_rent, maximum_rent)
        self.floor = self._set_floor(floor)
        self.total_rooms = self._set_total_rooms(total_rooms, minimum_rooms, maximum_rooms)
        self.sqm = self._set_sqm(sqm, minimum_sqm, maximum_sqm)
        self.last_application_date = last_application_date
        self.latitude = latitude
        self.longitude = longitude
        self.has_balcony = has_balcony
        self.has_elevator = has_elevator
        self.new_production = new_production

    def _set_rent(self, rent: int, minimum_rent: int, maximum_rent: int):
        if rent:
            return f"{rent}"
        else:
            return f"{minimum_rent} - {maximum_rent}"

    def _set_floor(self, floor: int):
        if floor == 0:
            return "Ground Floor"
        return floor

    def _set_total_rooms(self, total_rooms: int, minimum_rooms: int, maximum_rooms: int):
        if total_rooms:
            return str(total_rooms)
        else:
            return f"{minimum_rooms} - {maximum_rooms}"

    def _set_sqm(self, sqm: int, minimum_sqm: int, maximum_sqm: int):
        if sqm:
            return str(sqm)
        else:
            return f"{minimum_sqm} - {maximum_sqm}"
