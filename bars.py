import json
import os
import math
import pprint

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as bars:
            return json.load(bars)


def get_biggest_bar(data):
    seatscount_bar = []
    for bar in data:
        seatscount_bar.append(bar['Cells']['SeatsCount'])
    bar_max = max(seatscount_bar)
    for bar_num_max, bar in enumerate(seatscount_bar):
        if bar == bar_max:
            print('Самый большой бар')
            pprint.pprint(data[bar_num_max])


def get_smallest_bar(data):
    seatscount_bar = []
    for bar in data:
        seatscount_bar.append(bar['Cells']['SeatsCount'])
    bar_min = min(seatscount_bar)
    for bar_num_min, bar in enumerate(seatscount_bar):
        if bar == bar_min:
            print('Самый маленький бар')
            pprint.pprint(data[bar_num_min])


def get_closest_bar(data, longitude, latitude):
    sumgeo_bar = []
    input_geo_data = longitude+latitude
    for bar in data:
        sumn = math.fabs((bar['Cells']['geoData']['coordinates'][0]
                          + bar['Cells']['geoData']['coordinates'][1])
                         - input_geo_data)
        sumgeo_bar.append(sumn)
    sumgeosort = sorted(sumgeo_bar)
    for geo_num, min_geo in enumerate(sumgeo_bar):
        if min_geo <= sumgeosort[0]:
            print('Самый близкий бар')
            pprint.pprint(data[geo_num])


if __name__ == '__main__':
    filepath = 'bars.json'
    data = load_data(filepath)
    get_biggest_bar(data)
    get_smallest_bar(data)
    longitude = math.fabs(float(input('введите координату longitude=')))
    latitude = math.fabs(float(input('введите координату latitude=')))
    get_closest_bar(data, longitude, latitude)
