from __future__ import absolute_import
from __future__ import (print_function, unicode_literals)


class Table():
    """docstring for Table.
    This is the main class. It adds rows and columns, with data
    """
    def __init__(self,name):
        super(Table, self).__init__()
        self.rows = 0
        self.columns = 1
        self.table = '''|{}|'''.format(str(name))

    def add_column(self, name):
        self.columns += 1
        self.table += '''{}|'''.format(name)

    def finalize_cols(self):
        finalizer = '\n|'
        for i in range(self.columns):
            finalizer += '---|'
        self.table += finalizer


    def add_row(self, list):
        self.rows += 1
        row = '|'
        try:
            assert int(len(list)) == self.columns
        except(AssertionError):
            raise AssertionError('The list does not have enough values, or has too many values. Make sure only {} values are present.'.format(self.columns))
        for i in range(int(len(list))):
            row += '{}|'.format(list[i])
        self.table += '\n{}'.format(row)

    def get_table(self):
        return self.table
