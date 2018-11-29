import json
from pprint import pprint

import requests


def transform_subways_mi_2_degree(json_filename, target_filename='result_file.json'):
    with open(json_filename, encoding='utf-8') as f:
        subways = json.load(f)
        lines = subways['content']
        baiduapi = 'http://api.map.baidu.com/geoconv/v1/?coords=%s,%s&from=6&to=5&ak=5ddb28a5cdf3ca7c772420bc79c68552'
        for line in lines:
            for stop in line['stops']:
                res_str = requests.get(baiduapi % (stop['x'], stop['y']))
                transformed = res_str.json()
                stop['x'] = transformed['result'][0]['x']
                stop['y'] = transformed['result'][0]['y']

        with open(target_filename, 'w') as fp:
            json.dump(lines, fp, ensure_ascii=False)
        return target_filename


def build_subways():
    file = transform_subways_mi_2_degree('D:\\AI\\AI.NLP\\AI.NLP\\subways_bj_mi.json', 'subways_bj_degree.json')
    with open(file, encoding='utf-8') as f:
        subways = json.load(f)
    pprint(subways[0]['stops'][0])
