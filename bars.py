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
        biggest_bar_info = get_biggest_bar_info(load_json_data(filepath))
        print("Самый большой бар: {}\nКоличество мест: {}\n".format(
            biggest_bar_info['Name'],
            biggest_bar_info['SeatsCount'])
        smallest_bar_info = get_smallest_bar_info(load_json_data(filepath))
        print("Самый маленький бар: {}\nКоличество мест: {}\n".format(
            smallest_bar_info['Name'],
            smallest_bar_info['SeatsCount'])
        print("Для определения ближайшего бара введите ваши координаты")
        user_latitude = float(input("Введите широту "))
        user_longitude = float(input("Введите долготу "))
        closest_bar_info = get_closest_bar_info(
            load_json_data(filepath),
            user_longitude,
            user_latitude)
        print("\nБлижайший бар: {}\nАдрес: {}".format(
            closest_bar_info['Name'],
            closest_bar_info['Address'])
    else:
        print("Usage: python bars.py path_to_json_file")
