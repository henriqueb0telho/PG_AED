from sistema.insertion_sort import insertion_sort
from sistema.destinos.set import set_searches
from sistema.destinos.get import get_searches

def search_destinos(self, country=None, city=None, proximity=None):
        results = []
        for destino in self._destinos:
            if (not country or destino._country.lower() == country.lower()) and \
               (not city or destino._city.lower() == city.lower()) and \
               (proximity is None or destino._near_airport == proximity):
                print(get_searches(destino))
                set_searches(destino, get_searches(destino) + 1)
                print(get_searches(destino))
                results.append(destino)
        return insertion_sort(results)
    