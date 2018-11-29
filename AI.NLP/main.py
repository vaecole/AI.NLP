from lecture3 import subway_search
from util import subway_util
import json

with open('subways_bj_degree.json',encoding='utf-8') as f:
    subway_lines = json.load(f)

stops_coords = subway_util.get_all_stops_coords(subway_lines)
stops_conns = subway_util.build_connected_lines(subway_lines)

print(' --> '.join(subway_search.search_destination(stops_conns, stops_coords ,'圆明园','国贸', subway_search.get_successors, subway_search.min_change)))