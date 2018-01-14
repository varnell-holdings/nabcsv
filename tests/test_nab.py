import csv
from decimal import Decimal
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import nab_income_adder as nab


def test_1():
    test_data_1 = [['name', 'inc', 'blub'],
                   ['john', '+$1,000.00', 'uiop'],
                   ['pete', '+$1,000.05', 'uiop']]
    with open('data_1.csv', 'w') as f:
        writer = csv.writer(f)
        for row in test_data_1:
            writer.writerow(row)
    assert nab.main('data_1.csv') == Decimal('2000.05')


def test_2():
    assert nab.main('TransactionHistory-25.csv') == Decimal('213234.33')
