The goal of this project is to create a Python program that can read energy profiles and perform operations on them.

Example of the json file
```json
{
    "name": "Solar Tracker",
    "interval_in_minutes": 15,
    "unit": "kWh",
    "data": [0.0,0.0,0.1,...]
}
```

"name": name of the system
"interval_in_minutes": interval of data. For example, 15 means there is a data entry for every 15 minutes (35040 for a year). --> *1440 / 15 x 365*
"unit": the unit of the data.
"data": array with the data (floats) itself. --> *Depends on the interval_in_minutes*


The program should be called from the command line, read the input file, perform changes and write the changes back to an output file.

Example Input to call the programm and change the enrgy profiles

```bash
$ python3 profile_converter.py input_files/example.json output.json --
interval 60 --unit KJ
```
1. Read the profile from input_files/example.json.
2. change the "interval_in_minutes" from the current value (15) to 60. 3. modify the "data", so the interval matches the 60 minutes.
4. change the "unit" to "KJ" (Kilojoules).
5. modify the data, so it is converted from the current unit (kWh) to KJ.
6. write the resulting new profile to output.json

Your program should be able to convert between the following intervals:
* 1 minute 
* 15 minutes 
* 30 minutes 
* 1 hour
* 1 day

Your program should be able to convert between the following units:
* kWh (kilowatt-hours) Wh (watt-hours)
* KJ (kilojoule)
* J (joule)


The zip has to follow the naming comp_ws23_<YOUR-LASTNAME>_<YOUR-FIRSTNAME>.zip, e.g. comp_ws23_schwab_harald.zip.
*OPTIONAL: Create a remote git repository on GitHub or git-iit.fh-joanneum.at and add the link to the repository in your README.*
