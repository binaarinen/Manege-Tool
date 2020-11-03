#
#   Manege-Tool
#   Version 2
#   Author T.Wisotzki 2019
#

import csv
import xlrd


def xls_to_csv(xlsfile):
    csvfile = (xlsfile[:-4] + ".csv")
    workbook = xlrd.open_workbook(xlsfile)
    sheet = workbook.sheet_by_index(0)
    with open(csvfile, 'w') as csv_work_file:
        csvwriter = csv.writer(csv_work_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for rownum in range(sheet.nrows):
            csvwriter.writerow(sheet.row_values(rownum))
    return csvfile
