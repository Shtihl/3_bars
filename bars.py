import sys
import json
from math import sqrt


def load_json_data(source_file):
    with open(source_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)['features']


def get_biggest_bar(parsed_json_data):
    biggest_bar = max(parsed_json_data,
                      key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    bar_attributes = biggest_bar['properties']['Attributes']
    return bar_attributes['Name'], bar_attributes['SeatsCount']


def get_smallest_bar(parsed_json_data):
    smallest_bar = min(parsed_json_data,
                       key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    bar_attributes = smallest_bar['properties']['Attributes']
    return bar_attributes['Name'], bar_attributes['SeatsCount']


def get_closest_bar(parsed_json_data, longitude, latitude):
    closest_bar = min(parsed_json_data,
                      key=lambda point: get_distance(latitude,
                                                     longitude,
                                                     point['geometry']['coordinates']))
    bar_attributes = closest_bar['properties']['Attributes']
    return bar_attributes['Name'], bar_attributes['Address']


def get_distance(latitude, longitude, user_point):
    return sqrt((latitude - user_point[0])**2 + (longitude - user_point[1])**2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print("Самый большой бар: {}\nКоличество мест: {}\n".format(
            *get_biggest_bar(load_json_data(filepath))))
        print("Самый маленький бар: {}\nКоличество мест: {}\n".format(
            *get_smallest_bar(load_json_data(filepath))))
        print("Для определения ближайшего бара введите ваши координаты")
        user_latitude = float(input("Введите широту "))
        user_longitude = float(input("Введите долготу "))
        print("\nБлижайший бар: {}\nАдрес: {}".format(
            *get_closest_bar(load_json_data(filepath),
                             user_longitude,
                             user_latitude)
        ))
    else:
        print("Usage: python bars.py path_to_json_file")
