import json
from sistema.gestorDestinos.get_destinos import get_destinos
from sistema.destinos.get import get_name, get_searches

def shell_sort(destinations):
    n = len(destinations)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = destinations[i]
            j = i
            while j >= gap and destinations[j - gap]._searches < temp._searches:
                destinations[j] = destinations[j - gap]
                j -= gap
            destinations[j] = temp
        gap //= 2
    return destinations

def destinos_mais_procurados(self):
    top10 = []
    print(get_destinos(self))
    # return
    sorted_locations = shell_sort(get_destinos(self))
    for index, location in enumerate(sorted_locations[:10], start=1):
        # print(f"{index}. {get_name(location)} - Searches: {get_searches(location)}")
        top10.append(location)
    return top10
