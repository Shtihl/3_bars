import sys
import json
from math import sqrt


def load_json_data(source_file):
    with open(source_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)['features']


def get_biggest_bar_info(bars_info):
    biggest_bar = max(bars_info,
                      key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']


def get_smallest_bar_info(bars_info):
    smallest_bar = min(bars_info,
                       key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']


def get_closest_bar_info(bars_info, latitude, longitude):
    closest_bar = min(bars_info,
                      key=lambda point: sqrt(
                          (latitude - point['geometry']['coordinates'][0])**2 +
                          (longitude - point['geometry']['coordinates'][1])**2))
    return closest_bar['properties']['Attributes']


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print("Самый большой бар: {}\nКоличество мест: {}\n".format(
            get_biggest_bar_info(load_json_data(filepath))['Name'],
            get_biggest_bar_info(load_json_data(filepath))['SeatsCount']))
        print("Самый маленький бар: {}\nКоличество мест: {}\n".format(
            get_smallest_bar_info(load_json_data(filepath))['Name'],
            get_smallest_bar_info(load_json_data(filepath))['SeatsCount']))
        print("Для определения ближайшего бара введите ваши координаты")
        user_latitude = float(input("Введите широту "))
        user_longitude = float(input("Введите долготу "))
        print("\nБлижайший бар: {}\nАдрес: {}".format(
            get_closest_bar_info(load_json_data(filepath),
                                 user_longitude,
                                 user_latitude)['Name'],
            get_closest_bar_info(load_json_data(filepath),
                                 user_longitude,
                                 user_latitude)['Address']))
    else:
        print("Usage: python bars.py path_to_json_file")
