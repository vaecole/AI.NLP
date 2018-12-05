from functools import lru_cache
from functools import wraps

prices = {i + 1: v for i, v in
          enumerate([1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 40, -2, 56, -6, 25, -10, 100, -23, 200, -30])}
cache = {}


def revenue_cache(r):
    if r in cache:
        return cache[r]

    r_optimal = max([prices[r]] + [(revenue_cache(i) + revenue_cache(r - 1)) for i in range(1, r)])
    cache[r] = r_optimal
    return r_optimal


@lru_cache(maxsize=20)
def revenue_lru(r):
    return max([prices[r]] + [(revenue_lru(i) + revenue_lru(r - 1)) for i in range(1, r)])


def memo(func):
    _cache = {}

    @wraps(func)
    def __wrap(*args, **kwargs):
        str_key = str(args) + str(kwargs)
        if str_key not in _cache:
            result = func(*args, **kwargs)
            _cache[str_key] = result
        return _cache[str_key]

    return __wrap


@memo
def revenue_memo(r):
    return max([prices[r]] + [(revenue_memo(i) + revenue_memo(r-1)) for i in range(1, r)])
