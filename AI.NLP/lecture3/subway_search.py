import math

def get_successors(city_conn_, current):
    return city_conn_[current]


def search_destination(subway_net, cities, start, destination, get_succsssors_func, strategy):
    close_city = []
    open_paths = [[start]]
    while open_paths:
        current_path = open_paths.pop(0)
        current_city = current_path[-1]
        close_city.append(current_city)

        if current_city == destination:
            return current_path

        for next_ in get_succsssors_func(subway_net, current_city):
            if next_ not in close_city:
                open_paths.append(current_path + [next_])

        open_paths = strategy(open_paths, cities)

    return 'path not found'


def sort_pathes(pathes, func):
    return sorted(pathes, key=func)


def get_city_distance(city1, city2, cities):
    return geo_distance(cities[city1], cities[city2])


def get_path_distance(path, cities):
    if not path: return 0
    if len(path) == 1: return 0
    return sum(get_city_distance(path[i], path[i + 1], cities) for i in range(len(path) - 1))


# strategies
def min_distance(paths, cities):
    return sort_pathes(paths, lambda p: get_path_distance(p, cities))


def min_change(paths, cities):
    return sort_pathes(paths, lambda p: len(p))


def comprehensive_min(paths, cities):
    return sort_pathes(paths, lambda p: get_path_distance(p, cities) + len(p))


def geo_distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

