#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import io

from .exceptions import (SuppressedError,
                         TooManyValues,
                         DoNotOverwrite)


class Table:
    """docstring for Table.
    This is the main class. It adds rows and columns, with data
    """

    def __init__(self, name, debug=True):
        super(Table, self).__init__()
        self.todebug = debug
        self.rows = 0
        self.columns = 1
        self.table = '''|{}|'''.format(str(name))
        self.finalized = False
        if self.todebug:
            self.functions = []
            self.finalized_run = False

    def debug(self, print_d=True):
        """
        :rtype: str
        """
        global dmessage
        try:
            dmessage = '''Printing debug information:
            Rows: {rows}
            Columns: {cols}
            Finalized?: {fin}
            Table Content: {table}
            Functions: {funcs}'''.format(rows=str(self.rows),
                                         cols=str(self.columns),
                                         fin=str(self.finalized),
                                         table=self.table,
                                         funcs=self.functions)
            if print_d:
                print(dmessage)
            else:
                return dmessage
        except NameError:
            pass
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), dmessage)

    def add_column(self, name, all_cols=False):
        self.columns += 1
        self.table += '{}|'.format(str(name))
        try:
            if all_cols:
                return {'function': 'add_column', 'data': [str(name)]}
            else:
                self.functions.append({'function': 'add_column', 'data': [str(name)]})
        except NameError:
            pass
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def all_columns(self, *args):
        try:
            all_col_data = {'function': 'all_columns', 'data': []}
            for value in args:
                all_col_data['data'].append(self.add_column(str(value), all_cols=True))
            self.functions.append(all_col_data)
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def finalize_cols(self):
        try:
            finalizer = '\n|'
            for i in range(self.columns):
                finalizer += '---|'
            self.table += finalizer
            self.functions.append({'function': 'finalize_cols', 'data': finalizer})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def add_row(self, show_warning_message=True, *args):
        try:
            if self.finalized_run:
                self.finalized_run = False
            if not self.finalized:
                self.finalize_cols()
                self.finalized_run = True
                self.finalized = True
            add_row_data = {'function': 'add_row',
                            'data': {'finalized_run': self.finalized_run,
                                     'show_warning_message': show_warning_message,
                                     'values': []}}
            self.rows += 1
            row = '|'
            rows_made = 0
            for i in range(int(len(args))):
                row += '{}|'.format(str(args[i]))
                rows_made += 1
                add_row_data['data']['values'].append(args[i])
            if self.columns > rows_made:
                if show_warning_message:
                    print(
                        "You did not enter in enough values. You entered in {} values out of {} values. The values "
                        "that you did not enter in will be filled in with a blank space. You can stop this message "
                        "from appearing by adding the argument show_warning_message = False".format(
                            str(rows_made), str(self.columns)))
                    add_row_data['data']['message_shown'] = True
                for i in range(int(self.columns - rows_made)):
                    row += ' |'
                add_row_data['data']['values'].append('{} blank values added'.format(str(int(self.columns) - int(
                    rows_made))))
            elif self.columns < rows_made:
                raise TooManyValues(self.columns)
            self.table += '\n{}'.format(row)
            self.functions.append(add_row_data)
        except TooManyValues:
            raise
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def export_table_to_file(self, filename='markdowntable', extension='txt', mode='w+', overwrite_warning=True):
        global mode_check, message_displayed, fileread
        try:
            with open('{fname}.{ext}'.format(fname=str(filename), ext=str(extension)), str(mode)) as file:
                try:
                    contents = file.read()
                    print(contents)
                    if mode == 'w' or mode == 'w+':
                        mode_check = True
                    if len(contents) > 0 and overwrite_warning and mode_check:
                        print(
                            'This file already contains content. Do you want to overwrite the contents of the file? '
                            'You can add the argument mode = a[+] to not overwrite.')
                        true = True
                        false = False
                        overwrite = input('Write True or False:')
                        if overwrite:
                            raise DoNotOverwrite
                        message_displayed = True
                    fileread = True
                except io.UnsupportedOperation:
                    pass
                except DoNotOverwrite:
                    pass
                else:
                    file.write(self.table)
                self.functions.append({'function': 'export_table_to_file',
                                       'data': {'filename': filename, 'extension': extension, 'writemode': mode,
                                                'overwrite_warning': overwrite_warning, 'file read': fileread}})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))
