#
#   Manege-Tool
#   Version 2
#   Author T.Wisotzki 2019
#

from csv import reader as csvreader


class Day:
    def __init__(self, name):
        self.name = name
        self.trainings = list()


class Training:
    def __init__(self, date):
        self.date = date
        self.GETU = list()
        self.TRA = list()
        self.AKRO = list()
        self.SLACK = list()
        self.JONG = list()
        self.VERT = list()
        self.PARC = list()
        self.BREAK = list()
        self.CAN = list()


def doodle(doodle):
    name = ""
    tmpdates = list()
    with open(doodle, 'r') as csvdoodle:
        csvcontent = csvreader(csvdoodle)
        rownum = 1
        for row in csvcontent:
            row = str(row)
            if rownum == 1:                       # read in name of doodle
                name = row.split(";")[0][8:-1]
                Trainingsday = Day(name)
            elif rownum == 4:                     # read in dates of that doodle
                rowsplit = row[3:-2].split(";")
                last = ""
                for training in rowsplit:
                    if not training == "":
                        training = training.split(" ")[0]
                    else:
                        training = last
                    tmpdates.append(training)
                    last = training
            elif rownum == 5:
                rowsplit = row[3:-2].split(";")
                for day in range(len(rowsplit)):
                    month = tmpdates[day]
                    Trainingsday.trainings.append(Training(str(rowsplit[day] + "." + month)))
            elif rownum >= 6:                    # read in TL and their preferences
                if row[2:7] == 'Count':
                    break
                else:
                    discpart = row[2:-2].split(" ")[0].replace(':', '')
                    TLname = row[(3+len(discpart)):-2].split(";")[0]
                    TLdiscs = discpart.split("/")
                    if len(TLdiscs) > 1:
                        TLname = TLname + "*"
                    for i in range(len(Trainingsday.trainings)):
                        wish = row[2:-2].split(";")[i+1]
                        if wish != "":
                            for attr, value in Trainingsday.trainings[i].__dict__.items():
                                for dis in TLdiscs:
                                    if attr == dis and wish == "OK":
                                        value.append(TLname + ",\n")
                                    elif attr == 'CAN' and wish == "(OK)":
                                        disz = ""
                                        for d in TLdiscs:
                                            disz = disz + d
                                        value.append((disz + " " + str(TLname) + ",\n"))
            rownum += 1
    return Trainingsday
