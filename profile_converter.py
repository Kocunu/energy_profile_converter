import json
import sys

# Error handling on wrong input
if len(sys.argv) != 7 or sys.argv[5] != '--unit' or sys.argv[3] != '--interval':
    print("Wrong input!")
    sys.exit(1)

# Supporting user input and file manipulation
inFile = sys.argv[1]
outFile = sys.argv[2]
interval = sys.argv[4]
unit = sys.argv[6]

supported_units = ['KJ', 'kWh', 'Wh', 'J']
supported_intervals = ['1', '15', '30', '60', '1440']

if unit not in supported_units:
    print(f"The Input {unit} is not supported.")
    sys.exit(1)

if interval not in supported_intervals:
    print(f"The Input {interval} is not supported.")
    sys.exit(1)

# Json file manipulation
with open(inFile, 'r') as json_file:
    json_object = json.load(json_file)
    # DumpJsonFile = json.dumps(json_object, indent=1)
    # print(DumpJsonFile)

# kWH in Wh data * 1000
# kWh in J data * 3,6e+6
# kWh in KJ data * 3600

json_object['unit'] = unit

if unit == 'Wh':
    json_object['data'] = [x * 1000 for x in json_object['data']]

if unit == 'kJ':
    json_object['data'] = [x * 3600 for x in json_object['data']]

if unit == 'J':
    json_object['data'] = [x * 3600000 for x in json_object['data']]

if unit == 'kWh':
    json_object['data'] = [x * 1 for x in json_object['data']]

# Intervals
# 1 minute
# 15 minutes
# 30 minutes
# 1 hour
# 1 day

old_interval = json_object['interval_in_minutes']
json_object['interval_in_minutes'] = interval


def convert_interval(data, old_interval, new_interval):
    if old_interval < new_interval:

        result = []
        sum_values = 0
        count = 0

        for value in data:
            sum_values += value
            count += 1

            if count * old_interval >= new_interval:
                result.append(sum_values / count)
                sum_values = 0
                count = 0

        if count > 0:
            result.append(sum_values / count)

        return result
    elif old_interval > new_interval:

        result = []

        for value in data:
            repetitions = int(new_interval / old_interval)
            result.extend([value] * repetitions)

        return result
    else:

        return data


data = json_object['data']
newData = convert_interval(data, old_interval, 1)
json_object['data'] = newData
# print(convert_interval(data,15, 30))

with open(outFile, 'w') as json_output_file:
    json.dump(json_object, json_output_file, indent=4)
