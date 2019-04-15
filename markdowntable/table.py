from __future__ import unicode_literals

from markdowntable.errors import DeletingOnlyColumnException, TooLittleValuesException, TooManyValuesException
from markdowntable.row import Row, Column


class Table(list):
    """The purpose of MarkdownTable is to make it easy to make a table and format it. The results will be printed in
    Markdown format. The table will not be appropriately formatted.

    1. How to make a Table:

        You will need at least one name for the column. You can either pass a Column instance or the values as arguments.

        Example:
            Example 1:
                >>> t = Table('Name')
            Example 2:
                >>> c = Column('Name')
                >>> t = Table(c)

        In essence, the table created by either method is equal.

    2. How to make a Row:

        There are two methods for making a Row. You can either initalize a Row class and pass it to the Table instance or
        you can pass the values to the add_rows method.

        Example:
            Example 1:
                >>> t = Table('Name', 'Age')
                >>> t.add_row('Brian', 23)
                >>> t.add_row('Josh', 34)
            Example 2:
                >>> t = Table('Name', 'Age')
                >>> t.add_row(Row('Brian', 23))
                >>> t.add_row(Row('Josh', 34))

    3. How to get the formatted table:

        There are two ways to get the table value. You can either call the make_table function, or ask for the string
        version of the table object, which calls make_table.

        Example:
            Example 1:
                >>> t = Table('Name', 'Age')
                >>> t.add_row('Brian', 23)
                >>> t.add_row('Josh', 34)
                >>> s = t.make_table()
            Example 2:
                >>> t = Table('Name', 'Age')
                >>> t.add_row('Brian', 23)
                >>> t.add_row('Josh', 34)
                >>> s = str(t)
            If we were to compare the two results, we would see that the outputs are equal.

    4. How to modify the column
        To modify the column, we can access it by getting the 0th key of the table.

        >>> t = Table('Test')
        >>> c = t[0]

        A. Adding column values
            We can add values to the column directly, or use the add_column_value method.

            >>> c.append('Test2')

            >>> t.add_column_value('Test2')
        B. Removing column values
            We can remove column values by using the remove() and pop() methods on the column interface, or by calling
            the remove_column_value method

            >>> c.remove('Test2')

            >>> c.pop(1)

            >>> t.remove_column_value('Test2')

            >>> t.remove_column_value(1)

            As noted, the remove_column method is smart, as in it can detect if the argument is an int or not an int,
            and call the appropriate method.
        C. Replacing the entire column
            If you have a new Column() and you would like to overwrite the old column, you can either set the 0th key of
            the table to the new instance or call the overwrite_column method.

            >>> c2 = Column('Num1', 'Num2')
            >>> t[0] = c2

            >>> t.overwrite_column(c2)

    5. How to modify a row
        Unlike with a column, you must access a Row directly by calling it's key number.

        >>> t = Table('Name', 'Age', 'Grade')
        >>> t.add_row('Andy')
        >>> r1 = t[1]

        A. Add values to a row
            We can either append each variable to the Row, or we can call the add_values method on the Row.

            >>> r1.append(15)
            >>> r1.append(95)

            >>> r1.add_values(15,95)
        B. Remove values from a row
            We can either use the remove() or the pop() methods.

            >>> r1.remove(95)

            >>> r1.pop(2)
        C. Remove entire row
            We can either call pop() on the Table instance or call the remove_row method, which calles pop()

            >>> t.pop(1)

            >>> t.remove_row(1)
        D. Overwrite row
            If we have a new Row() class, we can just set the key value equal to the new Row or just call the
            overwrite_row method.

            >>> r1new = Row('Andy', 15, 95)
            >>> t[1] = r1new

            >>> t.overwrite_row(1, r1new)
    """

    def __init__(self, col1, *cols, fill_empty_rows=True, ignore_length_mismatches=False):
        """Initalizes the class.

        It requires a column name to start the Column() class with.

        There are also a bunch of options.

        Parameters:
            :param str, Column col1: The name of the first column
            :param str, tuple cols: The names of the other columns
            :param bool fill_empty_rows: This indicates whether or not to run fill_empty on the rows that have less
                                         values than the amount of columns.
            :param bool ignore_length_mismatches: This indicates whether or not to ignore rows that contain more values
                                                   then the amount of columns.
        """
        if isinstance(col1, Column):
            super(Table, self).__init__((col1,))
        else:
            super(Table, self).__init__((Column(col1, *cols),))
        self.fill_empty = fill_empty_rows
        self.ignore = ignore_length_mismatches

    def add_column_value(self, name):
        self[0].append(name)

    def add_column_values(self, *names):
        for i in names:
            self.add_column_values(i)

    def add_row(self, *values):
        """Adds a row.

        If the row is of class Row(), then it will use that instead of initalizing a new row with the arguments.

        Parameters:
            :param Row, str values: A Row() class or a tuple of values to initalize a row with.
        """
        if isinstance(values[0], Row):
            self.append(values[0])
        else:
            self.append(Row(values))

    def add_rows(self, *rows):
        """Adds a bunch of rows.

        This assumes that each of the values are a Row() class or an iterable with the values.

        Parameters:
             :param tuple rows: A tuple or iterable of Row objects or iterables that contain the row values.
        """
        for i in rows:
            if isinstance(i, Row):
                self.add_row(i)
            else:
                self.add_row(*i)

    def pop(self, index):
        """Removes the value at the position index.

        The method is identical to the pop used by list() except that an error is raised if the index is 0.

        Parameters:
            :param int index: The index to delete at

        Returns:
            :return: The value that was removed.
            :rtype: Any
        """
        if index == 0:
            raise DeletingOnlyColumnException
        else:
            return super(Table, self).pop(index)

    def __delitem__(self, key):
        """Removes the value at the position key.

        The method is identical to the __delitem__ used by list() except that an error is raised if the index is 0.

        Parameters:
            :param int key: The index to delete at

        Returns:
            :return: The value that was removed.
            :rtype: Any
        """
        if key == 0:
            raise DeletingOnlyColumnException
        else:
            super(Table, self).__delitem__(key)

    @staticmethod
    def format_string(s, item):
        """Duplicates a string, fills in each with either an item or copies the string item times.

        Parameters:
            :param str s: The string to be used
            :param item: The item or number of times to fill/duplicate the string

        Returns:
            :return: The formatted/duplicated string
            :rtype: str
        """
        formatted_str = '|'
        if isinstance(item, int):
            for i in range(item):
                formatted_str += s
        else:
            for i in item:
                formatted_str += s % i
        return formatted_str

    def format_row(self, row, count=None, num=None):
        """Formats a row into string.

        If the count is given, then it will check the row and act accordingly.

        Parameters:
            :param Row row: The Row to check.
            :param int count: The amount of values to check for
            :param int num: The row number

        Returns:
            :return: The formatted string
            :rtype: str
        """

        assert isinstance(row, Row), "A Row was not passed in the initial setup. Re-define the class."
        if count is not None:
            if len(row) < count:
                row.fill_empty(count)
                if not self.ignore:
                    if self.fill_empty:
                        row.fill_empty(count)
                    else:
                        raise TooLittleValuesException(num, count, len(row))
            elif len(row) > count:
                if not self.ignore:
                    raise TooManyValuesException(num, count, len(row))
        return self.format_string('%s|', row)

    def make_table(self):
        """Makes the table.

        Returns:
            :return: The table in string format.
            :rtype: str
        """
        col_length = len(self[0])
        table = self.format_row(self[0]) + '\n' + self.format_string('---|', col_length)
        for n, i in enumerate(self[0:]):
            n += 1
            table += '\n' + self.format_row(i, col_length, n)
        return table.strip()

    def __str__(self):
        return self.make_table()

    def remove_column_value(self, param):
        """Removes a column value.

        The function is smart as it will use remove or pop depending on type of value passed to param

        Parameters:
            :param param: The number of the index of the value to remove or the value to remove.

        Returns:
            :return: The value of the item removed
        """
        if isinstance(param, int):
            return self[0].pop(param)
        else:
            return self[0].remove(param)

    def overwrite_column(self, col):
        """Overwrites a column with a new column.

        Parameters:
            :param Column col: The new column to overwrite with
        """
        if isinstance(col, Column):
            self[0] = col

    def remove_row(self, index):
        """Removes a row at index number index.

        Parameters:
            :param int index: The index of the row to delete.

        Returns:
            :return: The Row class deleted
            :rtype: Row
        """
        return self.pop(index)

    def overwrite_row(self, index, newrow):
        """Overwrite the row at index number index with the row newrow.

        The column has it's own overwrite process, overwrite_column.

        Parameters:
            :param int index: The index number to overwrite
            :param Row newrow: The new Row instance to overwrite with
        """
        if index > 0:
            if isinstance(newrow, Row):
                self[index] = newrow
        else:
            raise DeletingOnlyColumnException
