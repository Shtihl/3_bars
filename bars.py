import sys
import json
from math import sqrt


def load_json_data(source_file):
    with open(source_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)['features']


def get_biggest_bar(parsed_json_data):
    biggest_bar = max(parsed_json_data,
                      key=lambda bar: bar['properties']['Attributes']['SeatsCount'])

    return (biggest_bar['properties']['Attributes']['Name'],
            biggest_bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(parsed_json_data):
    smallest_bar = min(parsed_json_data,
                       key=lambda bar: bar['properties']['Attributes']['SeatsCount'])

    return (smallest_bar['properties']['Attributes']['Name'],
            smallest_bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(parsed_json_data, longitude, latitude):
    closest_bar = min(parsed_json_data,
                      key=lambda point: get_distance(latitude,
                                                     longitude,
                                                     point['geometry']['coordinates']))
    return (closest_bar['properties']['Attributes']['Name'],
            closest_bar['properties']['Attributes']['Address'])


def get_distance(latitude, longitude, user_point):
    return sqrt((latitude - user_point[0])**2 + (longitude - user_point[1])**2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print("The biggest Bar: {}\nNumber of seats: {}\n".format(
            *get_biggest_bar(load_json_data(filepath))))
        print("The smallest Bar: {}\nNumber of seats: {}\n".format(
            *get_smallest_bar(load_json_data(filepath))))
        print("To find the nearest bar, enter your coordinates")
        user_latitude = float(input("Enter your latitude "))
        user_longitude = float(input("Enter your longitude "))
        print("\nNearest bar: {}\nAddress: {}".format(
            *get_closest_bar(load_json_data(filepath),
                             user_longitude,
                             user_latitude)
        ))
    else:
        print("Usage: python bars.py path_to_json_file")
