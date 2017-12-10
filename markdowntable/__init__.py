#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import io

from .exceptions import (SuppressedError,
                         TooManyValues,
                         DoNotOverwrite)
from .messages import (not_enough_values,
                       overwrite_message)


# Todo: Add remove_column and remove row


class Table:
    """docstring for Table.
    This is the main class. It adds rows and columns, with data
    """

    def __init__(self, name, debug=True):  # creates self variables
        """

        :param name: string
        :param debug: boolean
        """
        super(Table, self).__init__()  # idk
        self.todebug = debug  # debug?
        self.rows = 0  # rows
        self.columns = 1  # columns
        self.table = '''|{}|'''.format(str(name))
        self.finalized = False
        if self.todebug:
            self.functions = []
            self.finalized_run = False

    def debug(self, print_d=True):
        """

        :param print_d: bool
        :return: string
        """
        global debugmessage
        try:
            debugmessage = '''Printing debug information:
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
                print(debugmessage)
            else:
                return debugmessage
        except NameError:
            pass
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), debugmessage)

    def add_column(self, name, all_cols=False):
        """

        :param name: string
        :param all_cols: string
        :return: None
        """
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
        """

        :param args: string
        :return: None
        """
        try:
            all_col_data = {'function': 'all_columns', 'data': []}
            for value in args:
                all_col_data['data'].append(self.add_column(str(value), all_cols=True))
            self.functions.append(all_col_data)
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def all_columns_with_list(self, list):
        """

        :param list: list
        :return: None
        """
        try:
            all_col_data = {'function': 'all_columns', 'data': []}
            for value in list:
                all_col_data['data'].append(self.add_column(str(value), all_cols=True))
            self.functions.append(all_col_data)
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))


    def finalize_cols(self):
        """

        :return: None
        """
        try:
            finalizer = '\n|'
            for i in range(self.columns):
                finalizer += '---|'
            self.table += finalizer
            self.functions.append({'function': 'finalize_cols', 'data': finalizer})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def add_row(self, *args, show_warning_message=True):
        """

        :param show_warning_message: bool
        :param args: string
        :return: None
        """
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
                    print(not_enough_values(rows_made, self.columns))
                    add_row_data['data']['message_shown'] = True
                for i in range(int(self.columns - rows_made)):
                    row += ' |'
                # noinspection PyTypeChecker
                add_row_data['data']['values'].append('{} blank values added'.format(str(self.columns - rows_made)))
            elif self.columns < rows_made:
                raise TooManyValues(self.columns)
            self.table += '\n{}'.format(row)
            self.functions.append(add_row_data)
        except TooManyValues:
            raise
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def add_row_with_list(self, list, show_warning_message=True):
        """

        :param show_warning_message: bool
        :param list: list
        :return: None
        """
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
            for i in range(int(len(list))):
                row += '{}|'.format(str(list[i]))
                rows_made += 1
                add_row_data['data']['values'].append(list[i])
            if self.columns > rows_made:
                if show_warning_message:
                    print(not_enough_values(rows_made, self.columns))
                    add_row_data['data']['message_shown'] = True
                for i in range(int(self.columns - rows_made)):
                    row += ' |'
                # noinspection PyTypeChecker
                add_row_data['data']['values'].append('{} blank values added'.format(str(self.columns - rows_made)))
            elif self.columns < rows_made:
                raise TooManyValues(self.columns)
            self.table += '\n{}'.format(row)
            self.functions.append(add_row_data)
        except TooManyValues:
            raise
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def export_table_to_file(self, filename='markdowntable', extension='txt', mode='w+', overwrite_warning=True):
        """

        :param filename: string
        :param extension: string
        :param mode: string
        :param overwrite_warning: bool
        :return: None
        """
        global mode_check, message_displayed, file_read
        try:
            with open('{fname}.{ext}'.format(fname=str(filename), ext=str(extension)), str(mode)) as file:
                try:
                    contents = file.read()
                    print(contents)
                    if mode == 'w' or mode == 'w+':
                        mode_check = True
                    if len(contents) > 0 and overwrite_warning and mode_check:
                        print()
                        true = True
                        false = False
                        overwrite = input('Write True or False:')
                        if overwrite:
                            raise DoNotOverwrite
                        message_displayed = True
                    file_read = True
                except io.UnsupportedOperation:
                    pass
                except DoNotOverwrite:
                    pass
                else:
                    file.write(self.table)
                self.functions.append({'function': 'export_table_to_file',
                                       'data': {'filename': filename, 'extension': extension, 'writemode': mode,
                                                'overwrite_warning': overwrite_warning, 'file read': file_read}})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))
