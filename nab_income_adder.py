"""Script to sum income from downloaded nab statement"""

import csv


download = input('Enter the csv file name you have just downloaded. ')
download = '/Users/jtair/Downloads/' + download
with open(download, 'r') as f:
        rows = csv.reader(f)
        next(rows)
        total = 0
        for row in rows:
            inc = row[1]
            inc = inc.strip('$+')
            inc = inc.replace(',', '')
            total += float(inc)
        print('Total income is {: .2f}'.format(total))
