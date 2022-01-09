## Imports
from argparse import ArgumentParser
from AssignmentGenerator import AssignmentGenerator

def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for quickly generating AngryAssignment messages for WoW TBC-Classic')
    argParser.add_argument("-i", "--input", dest="config", help="The config file to use", type=str, default="config.json")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Create the app and run
    app = AssignmentGenerator(args.config)
    app.run()


## Main thread check
if __name__ == '__main__':
    main()
