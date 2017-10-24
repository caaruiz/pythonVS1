
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
import getopt
import argparse
import os.path

operations_list = {'heat': {'time': 15, 'name': 'heating'},
                   'stir': {'time': 8, 'name': 'stiring'},
                   'move': {'time': 3, 'name': 'moving'}}


def isOperationValid(operation):
    if operation in operations_list:
        return True
    return False


def runOperation(operation):
    ops_time = operations_list[operation]['time']
    ops_name = operations_list[operation]['name']
    for i in range(ops_time, 0, -1):
        print(ops_name, i)
        time.sleep(1)
    return


def parseOperation(optList):
    for operation in optList:
        if isOperationValid(operation):
            runOperation(operation)
        else:
            print("The command ",'"',operation,'"',"does not exist", )
    return


def printOperations():
    print('Operations: ', ','.join(operations_list))
    return


def cmd_usage():
    # printOperations()
    print('USAGE: cmd.py --ifile,-f <filename> --opt=,-o <cmd1,cmd2,cmd3>')
    return


def isOptListValid(operations):

    # commands = cmdlist.split(",")

    for operation in operations:
        if isOperationValid(operation) == False:
            print('The command ', operation , ' does not exist')
            return False
    return True


def readOperationsFromUser(optList):
    opts = optList.lower().split(',')
    opts = [x.strip(' ') for x in opts]
    # #TODO: Do we want to allow program to run
    # #      if there is a invalid command?
    # if isOptsListValid(opts) == False:
    # ....sys.exit(2)
    parseOperation(opts)
    return


def readOperationsFromFile(inputfile):
    with open(inputfile) as f:
        opts = [x.strip('\n').lower() for x in f.readlines()]

    # #TODO: Do we want to allow program to run
    # #      if there is a invalid command?
    # if isOptsListValid(opts) == False:
    # ....sys.exit(2)

    parseOperation(opts)
    return

##REMOVED: THIS MAIN WORKS ONLY IF YOU RUN SCRIPT THROUGHT HE COMMAND LINE
##         EX. USAGE: cmd.py --ifile,-f <filename> --opt=,-o <cmd1,cmd2,cmd3>
def cmd_main(argv):
    optlist = ''
    inputfile = ''
    if len(sys.argv) == 1:
        while True:
            try:
                optlist = input("Please Enter commands (seprated by commans ex. stir,move):")
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
    else:
        try:
            (opts, args) = getopt.getopt(argv, 'f:ho:', ['opt=', 'ifile='])
        except getopt.GetoptError:
            cmd_usage()
            sys.exit(0)
        for (opt, arg) in opts:
            if opt == '-h':
                cmd_usage()
                sys.exit()
            elif opt in ('-f', '--ifile'):
                inputfile = arg
                if os.path.isfile(inputfile) == False:
                    print('Cannot File: %s') % inputfile
                    sys.exit(2)
                break
            elif opt in ('-o', '--opt'):
                optlist = arg

            # #TODO: Do we want to allow program to run
            # #      if there is a invalid command?
            # arg_opts = optlist.split(",")
            # if isOptListValid(arg_opts) == False:
            # ....sys.exit(2)

                break

    if inputfile != '' and os.path.isfile(inputfile):
        readOperationsFromFile(inputfile)
    elif optlist != '':
        readOperationsFromUser(optlist)
    return

def main(argv):
    while True:

        try:
            userInput = input("Type in Command List(comma seperated) or File Path: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            if os.path.isfile(userInput):
                readOperationsFromFile(userInput)
            else:
                readOperationsFromUser(userInput)
            continue
    return

if __name__ == '__main__':
    main(sys.argv[1:])

