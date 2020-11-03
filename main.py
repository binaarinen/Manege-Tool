#
#   Manege-Tool
#   Version 2
#   Author T.Wisotzki 2019
#

import os

from scripts import config
from scripts import convert
from scripts import read
from scripts import filewriter


print("processing...")

# read configurations and prepare processing
configuration = config.read(2)
in_dir = configuration[0]
out_dir = configuration[1]
if os.path.isdir(in_dir):
    doodles = config.get_files(in_dir, "*.xls")
else:
    print("  ERROR: input directory: " + in_dir + " not found. Please check the 'config' file")
    exit()
doodleno = 1

# loop through files and process data
for doodle in doodles:
    csv_doodle = convert.xls_to_csv(doodle)
    Trainingsday = read.doodle(csv_doodle)
    filewriter.Out(Trainingsday, out_dir)
    print(" " + str(doodleno) + "/" + str(len(doodles)) + " " + str(doodle) + ".......done")
    os.remove(csv_doodle)
    doodleno += 1

print("completed")
