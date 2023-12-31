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

supported_units = ['kJ', 'kWh', 'Wh', 'J']
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

conversion_factors = {
    "kWh": {
        "Wh": 1000,
        "kJ": 3600,
        "J": 3600000,
        "kWh": 1
    },
    "Wh": {
        "Wh": 1,
        "kJ": 3.6,
        "J": 3600,
        "kWh": 0.001
    },
    "J": {
        "Wh": 0.000277778,
        "kJ": 0.001,
        "J": 1,
        "kWh": 2.77778e-7
    },
    "kJ": {
        "Wh": 0.277778,
        "kJ": 1,
        "J": 1000,
        "kWh": 0.000277778
    }
}

conversion_factor = conversion_factors[json_object['unit']][unit]
json_object['data'] = [x * conversion_factor for x in json_object['data']]


# Intervals
# 1 minute
# 15 minutes
# 30 minutes
# 1 hour
# 1 day
old_interval = json_object['interval_in_minutes']
json_object['interval_in_minutes'] = interval
new_interval = json_object['interval_in_minutes']


def convert_interval(data, old_interval, new_interval):
    result = []
    if old_interval < new_interval:
        for i in range(0, len(data), new_interval // old_interval):
            chunk = data[i:i + new_interval // old_interval]
            if chunk:
                result.append(sum(chunk) / len(chunk))
    elif old_interval > new_interval:
        for value in data:
            repetitions = old_interval // new_interval
            result.extend([value] * repetitions)
    else:
        result = data

    return result


data = json_object['data']
newData = convert_interval(data, old_interval, int(new_interval))
json_object['data'] = newData
# print(convert_interval(data,15, 30))

with open(outFile, 'w') as json_output_file:
    json.dump(json_object, json_output_file, indent=4)
