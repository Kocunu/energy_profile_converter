import json
import sys

# Error handling on wrong input
if len(sys.argv) != 4:
    print("Wrong input!")
    sys.exit(1)

inFile = sys.argv[1]
unit = sys.argv[3]
outFile = sys.argv[4]

supported_units = ['KJ', 'kWh', 'Wh', 'J']

if unit not in supported_units:
    print(f"The Input {unit} is not supported.")
    sys.exit(1)


with open(inFile, 'r') as json_file:
    json_object = json.load(json_file)
    # DumpJsonFile = json.dumps(json_object, indent=1)
    # print(DumpJsonFile)

json_object['unit'] = unit

with open(outFile, 'w') as json_output_file:
    json.dump(json_object,json_output_file, indent=4)


