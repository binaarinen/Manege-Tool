#
#   Manege-Tool
#   Version 2
#   Author T.Wisotzki 2019
#

import glob


def read(argnum):
    try:
        config_values = list()
        with open("config", "r") as config_file:
            for row in config_file.readlines():
                if row[0:1] != "#" and row[0:2] != "\n":
                    config_values.append(row[:-1])
    except Exception as e:
        print("  ERROR: configuration file not readable")
        print(e)
        exit()
    else:
        if(len(config_values) == argnum):
            return(config_values)
        else:
            print("  ERROR: configuration file has wrong format")
            exit()


def get_files(directory, form):
    files = list()
    for element in glob.glob(directory+form):
        files.append(element)
    return(files)
