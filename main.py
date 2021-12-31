## Imports
import os

## Cnfigurations
configFile = "config.json"
inputDirectory = "input/"
outputDirectory = "output/"

## Read the file
def readFileToString(fileName):
    parsedFile = ""
    try:
        fileContent = open(fileName, "r")
        for line in fileContent:
            parsedFile += line
        fileContent.close()
        return parsedFile
    except (OSError, IOError) as error:
        print(">>> ERROR! - An error occured:", error)
        return parsedFile

## Write the output AAs to file
def writeStringToFile(fileName, stringToWrite):
    try:
        outputFile = open(fileName, "w")
        outputFile.write(stringToWrite)
        outputFile.close()
    except (OSError, IOError) as error:
        print(">>> ERROR! - An error occured:", error)

## App entry
if __name__ == '__main__':
    print("> Compiling Angry Assignments")

    ## Create the output directory
    try:
        print(">> Creating the output directory")
        os.makedirs(outputDirectory)
    except FileExistsError:
        pass

