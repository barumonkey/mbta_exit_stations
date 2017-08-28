# Based on info from
# http://thedesignocean.com/2015/07/12/which-train-door-do-i-enter/

'''
INPUT: Start station name, End destination
Given that: Closest end station name
Given that: Which exit to use at end station
Given that: Which car and door to be at when exiting (Xth car from the front/back, front/middle/back door)
Given that: Where that door is in your start station
Given that (AND INPUT: Start station entrance): Which way to turn to get there from your entrance
(Don't output closest start entrance; get to the train ASAP, and optimize door choice if you have time)
'''

import sys
import urllib
import json

# edited
# Helper function. Returns distance between two map locations
def get_distance(point_a, point_b):
    # default vaules for testing
    point_a = '40.6655101,-73.89188969999998'
    point_b = '40.6655111,-73.89188970000000'

    # https://developers.google.com/maps/documentation/distance-matrix/intro
    key = 'AIzaSyCsyPiVprZXy4vhEgQIzRDBqPWp8V3nVvA'
    url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json'

    # NOTE: Multiple origins and destinations can be specified!
    # Use this to check for the shortest distance between one point and many exits
    origins = urllib.parse.urlencode('origins='+address)
    destinations = urllib.parse.urlencode('destinations='+exit_location)
    mode = 'walking'
    units = 'imperial'

    full_url = url_base+'?'+origins+'&'+destinations+'&'+mode+'&'+units+'&'+key

    """
    EXAMPLE

        https://maps.googleapis.com/maps/api/distancematrix/json
        ?origins=       Vancouver+BC
        &destinations=  San+Francisco|Victoria+BC
        &mode=          bicycling
        &key=           YOUR_API_KEY

        {
          "status": "OK",
          "origin_addresses": [ "Vancouver, BC, Canada" ],
          "destination_addresses": [ "San Francisco, California, USA", "Victoria, BC, Canada" ],
          "rows": [ {
            "elements": [ {
              "status": "OK",
              "duration": {
                "value": 340110,
                "text": "3 days 22 hours"
              },
              "distance": {
                "value": 1734542,
                "text": "735 mi"
              }
            }, {
              "status": "OK",
              "duration": {
                "value": 24487,
                "text": "6 hours 48 minutes"
              },
              "distance": {
                "value": 129324,
                "text": "129 mi"
              }
            } ]
          } ]
        }
    """


# Given end destination (street address), find the nearest T station
# Need to use some sort of API.
def end_destination_to_end_station(address):

    station_name = 'Central'
    exit_location = '40.6655101,-73.89188969999998'

    return station_name


# Given end destination (street address), find the nearest T station
# *AND* what the bext exit is.
# Need to use some sort of API and then more magic.
def end_destination_to_end_station_and_exit(address):
    station_name = 'Central'
    station_exit = 'Prospect'
    return station_name, station_exit


# Given direction, end station, and end exit,
# return which car and which door to be at when exiting
# (Xth car from the front/back, front/middle/back door)
def end_exit_to_car_and_door(direction, end_station, end_exit):

    # This list of lists represents an entire train. Each sub-list is a car, and each item is a door.
    # Most are "None" because, at all stations, most doors are not the ideal door to use.
    # Earlier entries in the list correspond to cars/doors closer to the front of the train.
    red_exits = [[None, None, None], [None, None, None], [None, None, None],
                 [None, None, None], [None, None, None], [None, None, None]]

    if direction == 'south':
        alewife_exits = [[None, None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, None]]
        davis_exits =   [[None, None, None], [None, None, None], ['All S', None, None],
                         [None, None, None], ['All N', None, None], [None, None, None]]
        porter_exits =  [[None, None, None], [None, None, None], [None, None, None],
                         [None, 'All', None], [None, None, None], [None, None, None]]
        harvard_exits = [['Main', None, None], [None, None, None], [None, None, None],
                         ['Church S', None, 'Church N'], [None, None, None], [None, None, None]]
        central_exits = [[None, 'Pearl', None], [None, None, None], [None, 'Essex', 'Mass Ave'],
                         [None, None, None], [None, None, None], [None, None, 'Western']]
        kendall_exits = [[None, 'Main S', None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, 'Main N'], [None, None, None]]
        charles_exits = [['All', None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, None]]
        park_exits =    [['Street', None, 'Green In'], [None, 'Green Out', None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, None]]
        dtx_exits =     [[None, None, None], [None, None, None], ['Concourse', 'Chauncy', None],
                         [None, None, None], [None, None, None], ['Washington', None, 'Orange']]
        south_exits =   [[None, None, None], [None, 'Commuter S', None], ['Silver', None, None],
                         [None, None, None], ['Commuter N', None, None], [None, None, None]]

    elif direction == 'north':
        south_exits =   [[None, None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, None]]
        dtx_exits =     [[None, None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, None]]
        park_exits =    [[None, None, None], [None, None, None], [None, None, None],
                         [None, None, None], ['x N', None, 'x M'], [None, None, 'x S']]
        charles_exits = [[None, None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, None, 'All']]
        kendall_exits = [[None, None, None], ['Marriot', None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, 'Main St', None]]
        central_exits = [['Western Ave', None, None], [None, None, None], [None, None, None],
                         [None, None, None], [None, None, None], [None, 'Pearl St', None]]
        harvard_exits = [[None, None, None], [None, None, None], [None, None, None],
                         ['Church St N', None, 'Church St S'], [None, None, None], [None, None, 'Main Exit']]
        porter_exits =  [[None, None, None], [None, 'All N', None], [None, None, None],
                         [None, 'All S', None], [None, None, None], [None, None, None]]
        davis_exits =   [[None, None, None], [None, None, 'All N'], [None, None, None],
                         [None, None, None], ['All S', None, None], [None, None, None]]
        alewife_exits = [[None, None, None], ['All N', None, 'All S'], [None, None, None],
                         [None, None, None], [None, None, None], [None, 'Russel Field', None]]

    else:
        sys.exit('\nDirection must be "south" or "north".\n')

    end_stations = {'Alewife': alewife_exits,
                    'Davis':   davis_exits,
                    'Porter':  porter_exits,
                    'Harvard': harvard_exits,
                    'Central': central_exits,
                    'Kendall': kendall_exits,
                    'Charles': charles_exits,
                    'Park':    park_exits,
                    'Dtx':     dtx_exits,
                    'South':   south_exits}

    if end_station in end_stations:
        my_station_exits = end_stations[end_station]
    else:
        sys.exit('\nend_station "'+end_station+'" not found in list of stations\n')

    car_names = {0: 'Front car', 1: '2nd car from the front', 2: '3rd car from the front',
                 3: '3rd car from the back', 4: '2nd car from the back', 5: 'Back car'}
    door_names = {0: 'front', 1: 'middle', 2: 'back'}

    car_num = 0
    my_car = False
    my_door = False
    for car in my_station_exits:
        # print(car)
        if end_exit in car:
            my_car = car_names[car_num]
            my_door = door_names[car.index(end_exit)]
        else:
            car_num += 1

    if my_car and my_door:
        my_car_door = my_car+', '+my_door+' door.'
        print('At '+end_station+', to get out at '+end_exit+', be at the')
        print(my_car_door)
        return [my_car, my_door, my_car_door]

    else:
        sys.exit('\nUnable to find exit "'+end_exit+'" at station "'+end_station+'".')


# Where that door is in your start station
# Output format?
def end_car_door_to_start_station_location(my_car, my_door, start_station='davis'):
    pass


end_exit_to_car_and_door(direction='south', end_station='South', end_exit='Silver')
