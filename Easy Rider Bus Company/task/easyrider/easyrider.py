import json
import re

raw_data = json.loads(input())
#raw_data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "a", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "two"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "39:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:95"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08.13"},  {"bus_id" : 256, "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "d", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08;44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "o", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "s", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:76"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
#raw_data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "a", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "two"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "39:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:95"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08.13"},  {"bus_id" : "", "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "d", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08;44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : "eleven", "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "o", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "s", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:76"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : "", "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
#raw_data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : 9, "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : "", "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : 23.9, "a_time" : 8},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : 34.6, "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : "eleven", "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : 3, "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : "21", "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : 13.01},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "FF", "a_time" : ""},  {"bus_id" : "", "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
filed_names = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']


def check_integer_type(data):
    if type(data) is not int:
        return False
    else:
        return True


def check_string_format(data, regs):
    if type(data) is not str:
        return True
    elif type(data) is str:
        if not re.match(regs, data):
            return True


def check_stop_type(data):
    if type(data) is not str:
        return True
    elif data == '':
        return False
    elif type(data) is str:
        regs = r'^[OFS]$'
        if not re.match(regs, data):
            return True


def create_lines_by_id(bus_id, info, line_128, line_256, line_512):
    if bus_id == 128:
        line_128.append(info)
    if bus_id == 256:
        line_256.append(info)
    if bus_id == 512:
        line_512.append(info)


def create_transfer_stops_list(line_128_stop_names, line_256_stop_names, line_512_stop_names):
    transfer_list = []
    for i in line_128_stop_names:
        if (i in line_256_stop_names and i not in transfer_list) or (i in line_512_stop_names and i not in transfer_list):
            transfer_list.append(i)
    for j in line_256_stop_names:
        if (j in line_128_stop_names and j not in transfer_list) or (j in line_512_stop_names and j not in transfer_list):
            transfer_list.append(j)
    return sorted(transfer_list)


def create_start_stop_lists(stop_type, stop_name):
    global stop_list, start_list, on_demand_list
    if stop_type == 'S' and stop_name not in start_list:
        start_list.append(stop_name)
    if stop_type == 'F' and stop_name not in stop_list:
        stop_list.append(stop_name)
    if stop_type == 'O' and stop_name not in on_demand_list and stop_name not in stop_list and stop_name not in start_list:
        on_demand_list.append(stop_name)


def check_time(line_stop_time):
    for i in range(len(line_stop_time) -1):
        if line_stop_time[i] > line_stop_time[i+1]:
            return 1

    return 0


total_errors = 0
bus_ids = 0
stop_ids = 0
stop_names = 0
next_stops = 0
stop_types = 0
a_times = 0

line_128_stop_ids = []
line_256_stop_ids = []
line_512_stop_ids = []

line_128_stop_types = []
line_256_stop_types = []
line_512_stop_types = []

line_128_stop_names = []
line_256_stop_names = []
line_512_stop_names = []

line_128_stop_time = []
line_256_stop_time = []
line_512_stop_time = []

stop_list = []
start_list = []
on_demand_list = []

for i in raw_data:
    if check_integer_type(i[filed_names[0]]) is False:
        bus_ids += 1
        total_errors += 1
    if check_integer_type(i[filed_names[1]]) is False:
        stop_ids += 1
        total_errors += 1
    if check_string_format(i[filed_names[2]], r"\b([A-Z][a-z]*\s)+(?:Road|Avenue|Boulevard|Street)$\b"):
        stop_names += 1
        total_errors += 1
    if check_integer_type(i[filed_names[3]]) is False:
        next_stops += 1
        total_errors += 1
    if check_stop_type(i[filed_names[4]]):
        total_errors += 1
        stop_types += 1
    if check_string_format(i[filed_names[5]], r'[0-2][0-9]:[0-5][0-9]'):
        total_errors += 1
        a_times += 1
    create_lines_by_id(i[filed_names[0]], i[filed_names[1]], line_128_stop_ids, line_256_stop_ids, line_512_stop_ids)
    create_lines_by_id(i[filed_names[0]], i[filed_names[4]], line_128_stop_types, line_256_stop_types, line_512_stop_types)
    create_lines_by_id(i[filed_names[0]], i[filed_names[2]], line_128_stop_names, line_256_stop_names, line_512_stop_names)
    create_lines_by_id(i[filed_names[0]], i[filed_names[5]], line_128_stop_time, line_256_stop_time, line_512_stop_time)
    create_start_stop_lists(i[filed_names[4]], i[filed_names[2]])


time_errors = check_time(line_128_stop_time) + check_time(line_256_stop_time) + check_time(line_512_stop_time)

print('Type and field validation:', total_errors + time_errors, 'errors')
print('bus_id:', bus_ids)
print('stop_id:', stop_ids)
print('stop_name:', stop_names)
print('next_stop:', next_stops)
print('stop_type:', stop_types)
print('a_time:', a_times + time_errors)

print('Line names and number of stops:')
if len(line_128_stop_ids) != 0:
    print('bus_id: 128 stops:', len(line_128_stop_ids))
if ('S' in line_128_stop_types and 'F' not in line_128_stop_types) or ('F' in line_128_stop_types and 'S' not in line_128_stop_types):
    print('There is no start or end stop for the line: 128')
if len(line_256_stop_ids) != 0:
    print('bus_id: 256 stops:', len(line_256_stop_ids))
if ('S' in line_256_stop_types and 'F' not in line_256_stop_types) or ('F' in line_256_stop_types and 'S' not in line_256_stop_types):
    print('There is no start or end stop for the line: 256')
if len(line_512_stop_ids) != 0:
    print('bus_id: 512 stops:', len(line_512_stop_ids))
if ('S' in line_512_stop_types and 'F' not in line_512_stop_types) or ('F' in line_512_stop_types and 'S' not in line_512_stop_types):
    print('There is no start or end stop for the line: 512')

if ('S' in line_128_stop_types and 'F' in line_128_stop_types) and ('S' in line_256_stop_types and 'F' in line_256_stop_types) and ('S' in line_512_stop_types and 'F' in line_512_stop_types):
    print('Start stops:', len(start_list), sorted(start_list))
    print('Transfer stops:', len(create_transfer_stops_list(line_128_stop_names, line_256_stop_names, line_512_stop_names)), create_transfer_stops_list(line_128_stop_names, line_256_stop_names, line_512_stop_names))
    print('Finish stops:', len(stop_list), sorted(stop_list))
    print('On demand stops:', len(on_demand_list), sorted(on_demand_list))
