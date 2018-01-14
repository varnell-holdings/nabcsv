"""Script to sum income from downloaded nab statement"""

import csv
from decimal import Decimal


def clean_up(inc):
    inc = inc.lstrip('$+')
    inc = inc.replace(',', '')
    inc = Decimal(inc)
    return inc


def main(download):
    with open(download, 'r') as f:
        rows = csv.reader(f)
        next(rows)
        total = sum(clean_up(row[1]) for row in rows)
        return total


if __name__ == '__main__':
    download = input('Enter the csv file name you have just downloaded. ')
    download = '/Users/jtair/Downloads/' + download
    total = main(download)
    print('Total income is {}'.format(total))
