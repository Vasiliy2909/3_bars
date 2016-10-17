import json
import os
import math
import pprint


def input_way_to_filepath():
    way = input('Укажите путь к файлу с барами:')
    if os.path.exists(way):
        return way


def input_longitude():
    longitude = float(input('введите координату longitude ='))
    while -180 > longitude or longitude > 180:
        print('Введите координату в диапазоне от -180 до 180')
        return input_longitude()
    return longitude


def input_latitude():
    latitude = float(input('введите координату latitude ='))
    while -90 > latitude or latitude > 90:
        print('Введите координату в диапазоне от -90 до 90 ')
        return input_latitude()
    return latitude


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as bars:
            return json.load(bars)


def get_biggest_bar(data):
    seatscount_bar = []
    bar_max = []
    for bar in data:
        seatscount_bar.append(bar['Cells']['SeatsCount'])
    for bar_num_max, size in enumerate(seatscount_bar):
        if size == max(seatscount_bar):
            bar_max.append(bar_num_max)
    bar_max_output = {'Самый большой бар №' + str(number + 1):
                      data[bar_num] for number, bar_num
                      in enumerate(bar_max)}
    return bar_max_output


def get_smallest_bar(data):
    seatscount_bar = []
    bar_min = []
    for bar in data:
        seatscount_bar.append(bar['Cells']['SeatsCount'])
        t = min(seatscount_bar)
    for bar_num_min, size in enumerate(seatscount_bar):
        if size == min(seatscount_bar):
            bar_min.append(bar_num_min)
    bar_min_output = {'Cамый маленький бар №' + str(number + 1):
                      data[bar_num] for number, bar_num
                      in enumerate(bar_min)}
    return bar_min_output


def get_closest_bar(data, longitude, latitude):
    sumgeo_bar = []
    bar_closest = []
    incoming_geo_data = longitude+latitude
    for bar in data:
        total_geo_data = math.fabs(
            (bar['Cells']['geoData']['coordinates'][0]
             + bar['Cells']['geoData']['coordinates'][1])
            - incoming_geo_data)
        sumgeo_bar.append(total_geo_data)
    sumgeosort = sorted(sumgeo_bar)
    for geo_num_closest, closest_geo in enumerate(sumgeo_bar):
        if closest_geo <= sumgeosort[0]:
            bar_closest.append(geo_num_closest)
    bar_closest_output = {'Самый близкий бар №' + str(number + 1):
                          data[geo_num] for number, geo_num
                          in enumerate(bar_closest)}
    return bar_closest_output


def readout_bars():
    output_options = input('Введите критерии поиска бара: ')
    if output_options.lower() == 'самый большой бар':
        pprint.pprint(get_biggest_bar(data))
    elif output_options.lower() == 'самый маленький бар':
        pprint.pprint(get_smallest_bar(data))
    elif output_options.lower() == 'самый близкий бар':
        longitude = input_longitude()
        latitude = input_latitude()
        pprint.pprint(get_closest_bar(data, longitude, latitude))
    while output_options != 'выход':
        return readout_bars()


if __name__ == '__main__':
    filepath = input_way_to_filepath()
    data = load_data(filepath)
    readout_bars()
