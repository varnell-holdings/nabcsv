"""Script to sum income from downloaded nab statement"""

import csv


def clean_up(inc):
    inc = inc.strip('$+')
    inc = inc.replace(',', '')
    inc = float(inc)
    return inc


def main(download):
    with open(download, 'r') as f:
        rows = csv.reader(f)
        next(rows)
        total = sum(clean_up(row[1]) for row in rows)
        return round(total, 2)


if __name__ == '__main__':
    download = input('Enter the csv file name you have just downloaded. ')
    download = '/Users/jtair/Downloads/' + download
    total = main(download)
    print('Total income is {: .2f}'.format(total))
