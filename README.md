# Angry Assignments Generator
Quick and dirty Python script for generating AngryAssignments from specified templates.

<br>

---

## Usage Guide
Rostering, class assignment and role values are done via the default JSON config file found in the repository, or via a specified JSON config handed to the app on execution.

On execution, the script will iterate through the "assignments" object of the config file and replace any matching placeholders in the templates (e.g. <tank_1>) with the values set in the corresponding assignment. The names will also be formatted using the class values assigned in the config's "roster" object.

Custom assignment values can be set by adding another key to the "assignments" object of the config and using the key surrounding with <> inside the templates - E.g. <custom_key>.

<br>

Example JSON Config:
```json
{
    "assignments": {
        "tank_1": "Koz",
        "tank_2": "Brovo",
        "healer_1": "Mirian",
        "healer_2": "Andy"
    },
    "roster": {
        "Koz": "Warrior",
        "Brovo": "Warrior",
        "Andy": "Paladin",
        "Mirian": "Paladin"
    }
}
```

Example Template:
```txt
Trash Assignments
--------------------
{Skull} = <tank_1> - (<healer_1>)
{Cross} = <tank_2> - (<healer_2>)
```

Example Ouput:
```txt
Trash Assignments
--------------------
{Skull} = |cWarriorKoz|r - (|cPaladinMirian|r)
{Cross} = |cWarriorBrovo|r - (|cPaladinAndy|r)
```

<br>

---

## Execution Guide
Arguments:
```bash
python main.py [-h] [-i config_file]
python main.py [--help] [--input config_file]
```

* -h, --help - Show the command-line usage manual
* -i, --input - Specify the JSON config file to use for the assignment and roster

Example usage:
```bash
python main.py -h
python main.py -i config.json
python main.py -i red_team.json
python main.py -i blue_team.json

python main.py --help
python main.py --input config.json
python main.py --input red_team.json
python main.py --input blue_team.json
```

<br>

---