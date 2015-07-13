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

# Given end destination (street address), find the nearest T station
# Need to use some sort of API.
def end_destination_to_end_station(address):
    station_name = 'Central'
    return station_name

# Given end destination (street address), find the nearest T station
# *AND* what the bext exit is.
# Need to use some sort of API and then more magic.
def end_destination_to_end_station_and_exit(address):
    station_name = 'Central'
    station_exit = 'Prospect'
    return station_name, station_exit

# Given end station and end exit,
# return which car and which door to be at when exiting
# (Xth car from the front/back, front/middle/back door)
def end_exit_to_car_and_door(end_station='Central', end_exit='Pearl'):

    red_exits =     [ [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ] ]

    davis_exits =   [ [ None,None,None ], [ None,None,None ], [ 'All S',None,None ], [ None,None,None ], [ 'All N',None,None ], [ None,None,None ] ]
    porter_exits =  [ [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,'All',None ], [ None,None,None ], [ None,None,None ] ]
    harvard_exits = [ [ 'Main',None,None ], [ None,None,None ], [ None,None,None ], [ 'Church S',None,'Church N' ], [ None,None,None ], [ None,None,None ] ]
    central_exits = [ [ None,'Pearl',None ], [ None,None,None ], [ None,'Essex','Prospect' ], [ None,None,None ], [ None,None,None ], [ None,None,None ] ]
    kendall_exits = [ [ None,'Main S',None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,'Main N' ], [ None,None,None ] ]
    charles_exits = [ [ 'All',None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ None,None,None ] ]
    park_exits =    [ [ 'Street',None,'Lechmere' ], [ None,'Outbound',None ], [ None,None,None ], [ None,None,None ], [ None,None,None ], [ 'Emergency',None,None ] ]
    dtx_exits =     [ [ None,None,None ], [ None,None,None ], [ 'Concourse','Chauncy',None ], [ None,None,None ], [ None,None,None ], [ 'Washington',None,'Orange' ] ]
    south_exits =   [ [ None,None,None ], [ None,'Commuter S',None ], [ 'Silver',None,None ], [ None,None,None ], [ 'Commuter N',None,None ], [ None,None,None ] ]

    stations =      ['Davis',    'Porter',     'Harvard',     'Central',     'Kendall',     'Charles',     'Park',     'Dtx',     'South']
    station_exits = [davis_exits, porter_exits, harvard_exits, central_exits, kendall_exits, charles_exits, park_exits, dtx_exits, south_exits]

    if end_station in stations:
        my_station_exits = station_exits[stations.index(end_station)]
    else:
        sys.exit('\nend_station "'+end_station+'" not found in list of stations\n')

    car_names = {0:'Front car', 1:'2nd car from the front', 2:'3rd car from the front', 3:'3rd car from the back', 4:'2nd car from the back', 5:'Back car'}
    door_names = {0:'front', 1:'middle', 2:'back'}

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
        print(my_car_door)
        return [my_car, my_door, my_car_door]

    else:
        sys.exit('\nUnable to find exit "'+end_exit+'" at station "'+end_station+'".')

# Where that door is in your start station
# Output format?
def end_car_door_to_start_station_location(my_car, my_door, start_station='davis'):
    pass


end_exit_to_car_and_door()
