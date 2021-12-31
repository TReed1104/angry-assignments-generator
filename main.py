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

## Input the raid member names
def setRaidAssignments(fileName):
    print(">> Reading File:", fileName)
    ## Read in the AA file
    fileData = readFileToString(inputDirectory + fileName)

    ## Find and replace assignment tokens e.g. <tank_0>

    ## Save the parsed AA file
    writeStringToFile(outputDirectory + fileName, fileData)

## App entry
if __name__ == '__main__':
    print("> Compiling Angry Assignments")

    ## Create the output directory
    try:
        print(">> Creating the output directory")
        os.makedirs(outputDirectory)
    except FileExistsError:
        pass

    ## Iterate through the supplied AA base files
    for fileToParse in os.listdir(inputDirectory):
        ## Parse the files and replace the values with the assigned raiders
        setRaidAssignments(fileToParse)
