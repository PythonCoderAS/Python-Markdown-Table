#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .exceptions import (SuppressedError,
                         TooManyValues)
from .messages import (not_enough_values,
                       overwrite_message,
                       no_more_rows)


# Todo: Add remove_column and remove row


class Table:
    """docstring for Table.
    This is the main class. It adds rows and columns, with data

    Usage:

    >>> t = Table('name')

    >>> t.all_columns('column_name')

    >>> t.add_row([value, value, value, ...])

    >>> table_code = t.table #gets table code

    """

    def __init__(self, name: str, debug: bool = True):  # creates self variables
        """
        The initiator of the Table() class. Creates all the initial self values

        :type name: str
        :type debug: bool
        :param name: The name of the first column
        :param debug: Do you want to enable debug function?
        """
        super(Table, self).__init__()  # idk
        self.to_debug = debug  # debug?
        self.rows = 0  # rows
        self.columns = 1  # columns
        self.table = '''|{}|'''.format(str(name))
        self.finalized = False
        if self.to_debug:
            self.functions = []
            self.finalized_run = False

    def debug(self, print_d=True):
        """

        :raise: SuppressedError
        :type print_d: bool
        :param print_d: Print the debug or return as string
        :return: The debug value
        :rtype: str
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

    def add_column(self, name: str, all_cols: bool = False):
        """
        Adds a column to the table. Must be used before adding rows.

        :type all_cols: bool
        :type name: str
        :param name: The name of the columns
        :param all_cols: Determines if all_columns() called add_column()
        :return: Nothing
        :rtype: None
        :raise: SuppressedError
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
        Adds all columns, as many as you want

        :type args: str
        :param args: The names of every column. Can be a list
        :return: Nothing
        :rtype: None
        :raise: SuppressedError
        """
        if isinstance(args[0], list):
            self.all_columns_with_list(args[0])
        else:
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
        Finalizes columns. Can be called manually, but usually called by the first add_row() argument.

        :return: Nothing
        :rtype: None
        :raise: SuppressedError
        """
        try:
            finalizer = '\n|'
            for i in range(self.columns):
                finalizer += '---|'
            self.table += finalizer
            self.functions.append({'function': 'finalize_cols', 'data': finalizer})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))

    def add_row(self, *args, show_warning_message: bool = True):
        """
        Adds rows, one for each arg. A row may be in string or list form. If too little arguments are in the list,
        then the rest will be blanked. If there are too many errors, an exception will be raised.

        :type args: str
        :type show_warning_message: bool
        :param show_warning_message: Shows warning messages if there is an exception.
        :param args: The values for the row.
        :return: Nothing
        :rtype: None
        :raises: SuppressedError, TooManyValues
        """
        if isinstance(args[0], list):
            self.add_row_with_list(args[0], show_warning_message=show_warning_message)
        else:
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

    def add_row_with_list(self, li: list, show_warning_message: bool = True):
        """
        Adds a row based on a list.

        :type show_warning_message: bool
        :type li: list
        :param show_warning_message: Shows the debug message if there is an exception.
        :param li: The list to be used to add values
        :return: Nothing
        :rtype: None
        :raise: SuppressedError
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
            for i in range(int(len(li))):
                row += '{}|'.format(str(li[i]))
                rows_made += 1
                add_row_data['data']['values'].append(li[i])
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

    def remove_row(self):
        lines = self.table.split('\n')
        last_line = lines[len(lines)]
        new_table = ''
        if '|---|' not in last_line:
            lines.remove(lines[len(lines)])
            for line in lines:
                new_table += line + '\n'
        else:
            print(no_more_rows)

    def export_table_to_file(self, filename: str = 'markdowntable', extension: str = 'txt', mode: str = 'w'):
        """

        :type mode: str
        :type extension: str
        :type filename: str
        :param filename: The filename to use
        :param extension: The extension to use
        :param mode: The mode to write in, usually write and read
        :return: Nothing
        :rtype: None
        :raise: SuppressedError
        """
        try:
            with open('{fname}.{ext}'.format(fname=str(filename), ext=str(extension)), str(mode)) as file:
                file.write(self.table)
                self.functions.append({'function': 'export_table_to_file',
                                       'data': {'filename': filename, 'extension': extension, 'writemode': mode}})
        except Exception as e:
            raise SuppressedError(type(e).__name__, str(e), self.debug(print_d=False))
