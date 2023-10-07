import json

with open('input_files/example.json', 'r') as json_file:
    json_object = json.load(json_file)
    DumptJsonFile = json.dumps(json_object, indent=1)
    print(DumptJsonFile)

