# Angry Assignments Generator
Quick and dirty Python script for generating AngryAssignments from specified templates.

<br>

---

## Usage Guide
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