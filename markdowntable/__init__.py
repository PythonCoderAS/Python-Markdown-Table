from __future__ import print_function, unicode_literals


class Table():
    """docstring for Table.
    This is the main class. It adds rows and columns, with data
    """
    def __init__(self, name):
        super(Table, self).__init__()
        self.rows = 0
        self.columns = 1
        self.table = '''|{}|'''.format(str(name))
        self.finalized = False

    def debug(self):
        print('''Printing debug information:
        Rows: {rows}
        Columns: {cols}
        Finalized?: {fin}
        Table Content: {table}'''.format(rows = str(self.rows),
        cols = str(self.columns),
        fin = str(self.finalized),
        table = self.table))

    def add_column(self, name):
        self.columns += 1
        self.table += '''{}|'''.format(name)

    def all_columns(self, *args):
        for value in args:
            self.add_column(str(value))

    def finalize_cols(self):
        finalizer = '\n|'
        for i in range(self.columns):
            finalizer += '---|'
        self.table += finalizer

    def add_row(self,show_warning_message = True, *args):
        if not self.finalized:
            self.finalize_cols()
            self.finalized = True
        self.rows += 1
        row = '|'
        rows_made = 0
        for i in range(int(len(args))):
            row += '{}|'.format(str(args[i]))
            rows_made += 1
        if self.columns > rows_made:
            if show_warning_message:
                print('You did not enter in enough values. You entered in {} values out of {} values. The values that you did not enter in will be filled in with a blank space. You can stop this message from appearing by adding the argument show_warning_message = False'.format(str(rows_made), str(self.columns)))
            for i in range(int(self.columns-rows_made)):
                row += ' |'
        elif self.columns < rows_made:
            raise AssertionError('You entered in too many row values. Please only enter {} row names.'.format(str(self.columns)))
        self.table += '\n{}'.format(row)


    def export_table_to_file(self, filename = 'markdowntable', extension='txt', mode = 'w+', overwrite_warning = True):
        with open('{fname}.{ext}'.format(fname = str(filename), ext = str(extension)),str(mode)) as file:
            try:
                contents = file.read()
                if mode == 'w' or mode == 'w+':
                    mode_check = True
                if len(contents) > 0 and overwrite_warning and mode_check:
                    print('This file already contains content. Do you want to overwrite the contents of the file? You can add the argument mode = a[+] to not overwrite.')
            except(io.UnsupportedOperation):
                pass
            file.write(table)
            return True
