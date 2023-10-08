# Energy profile converter
>This project is a compensation exercise for FH Joanneum. Only Python may be used as the programming language, and among other things, no third-party libraries are allowed. The instructions are included in the folder to provide more detailed information about the exercise. In this context, I will only describe the most important parts.

The goal of this project is to create a Python program that can read energy profiles and perform operations on them.
Like converting the unit and manipulating the data.

Main objectives:

[ ] Read the profile from input_files/example.json.

[ ] change the "interval_in_minutes" from the current value (15) to 60. 3. modify the "data", so the interval matches the 60 minutes.

[ ] hange the "unit" to "KJ" (Kilojoules).

[ ] modify the data, so it is converted from the current unit (kWh) to KJ.

[ ] write the resulting new profile to output.json


**Example of the json file**
```json
{
    "name": "Solar Tracker",
    "interval_in_minutes": 15,
    "unit": "kWh",
    "data": [0.0,0.0,0.1,...]
}
```
**Example of the console input** 
```bash
$ python3 profile_converter.py input_files/example.json output.json --
interval 60 --unit KJ
```

**Your program should be able to convert between the following intervals:**
* 1 minute 
* 15 minutes 
* 30 minutes 
* 1 hour
* 1 day


* When converting from a more frequent interval to a less frequent interval use the average of the old values for the new one. For example [0.1,0.5,0.6,0.4,...] in a 15 minutes interval should give [0.3,0.5,...] in a 30 minutes interval.

* When converting from a less frequent interval to a more frequent interval just repeat the values. For example [0.3,0.5,...] in a 30 minutes interval should give [0.3,0.3,0.5,0.5,...] in a 15 minutes interval.

**Your program should be able to convert between the following units:**
* kWh (kilowatt-hours) Wh (watt-hours)
* KJ (kilojoule)
* J (joule)

Github:https://github.com/Kocunu/energy_profile_converter
