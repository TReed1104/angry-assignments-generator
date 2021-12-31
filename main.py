## Imports
from argparse import ArgumentParser
import os
import json

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
    for placeholderToken in configData["assignments"]:
        if placeholderToken != "":
            fileData = fileData.replace(f"<{placeholderToken}>", GetFormattedRaiderName(placeholderToken))

    ## Save the parsed AA file
    writeStringToFile(outputDirectory + fileName, fileData)

## Get the raider information to replace the placeholder token with
def GetFormattedRaiderName(placeholder):
    raiderName = configData["assignments"][placeholder]
    raiderClass = configData["roster"][raiderName]
    formattedRaiderName = f"|c{raiderClass}{raiderName}|r"
    return formattedRaiderName

## App entry
if __name__ == '__main__':
    print("> Compiling Angry Assignments")

    ## Setup the command-line arguments
    argParser = ArgumentParser(description='AA generator for the Double Trouble Raids')
    argParser.add_argument("-i", "--input", dest="config", help="The config file to use", type=str, default="config.json")
    args = argParser.parse_args()

    ## Setup
    inputDirectory = "templates/"
    outputDirectory = "bin/"

    ## Load the config json 
    configFile = open(args.config)
    configData = json.load(configFile)
    configFile.close()

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
