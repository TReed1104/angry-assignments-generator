## Imports
import os

## Cnfigurations
configFile = "config.json"
inputDirectory = "input/"
outputDirectory = "output/"

## App entry
if __name__ == '__main__':
    print("> Compiling Angry Assignments")

    ## Create the output directory
    try:
        print(">> Creating the output directory")
        os.makedirs(outputDirectory)
    except FileExistsError:
        pass

