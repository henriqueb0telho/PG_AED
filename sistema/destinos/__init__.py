class Destino:
    def __init__(self, name, country, city, near_airport, coordinates, url, searches, next=None):
        self._name = name
        self._country = country
        self._city = city
        self._near_airport = near_airport
        self._coordinates = coordinates
        self._url = url
        self._searches = searches
        self._next = next