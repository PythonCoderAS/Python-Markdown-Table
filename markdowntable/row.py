from __future__ import unicode_literals

from markdowntable.errors import DeletingOnlyValueException


class Row(list):
    """The Row class. This allows the rows to be dynamically calculated in the Table class.

    The Row class is a subset of the list class, meaning that the Row acts like a list with extra functionality.

    Extra functionalities:
    1. Allows you to fill the list with values until it has x total values.
    2. Allows you to add x value y times.
    """

    def __init__(self, *values):
        """Initiates the class.

        The class will not convert an iterable to list, so make sure to pass in the argument using the * operator.

        Example:
            >>> t = (1,2,3,4,5,6,7,8,9,10)
            >>> r = Row(t, num = 0)
            >>> r
            Row(num=0, values =(1,2,3,4,5,6,7,8,9,10))

            >>> t = (1,2,3,4,5,6,7,8,9,10)
            >>> r = Row(*t, num = 0)
            >>> r
            Row(num=0, values = 1,2,3,4,5,6,7,8,9,10)

        Parameters:
            values: A tuple or list or other iterable of values to use.

        """
        super(Row, self).__init__(values)

    def add_values(self, *values):
        for i in values:
            self.append(i)

    def fill_empty(self, tonum):
        """Fills the row until it has x total values.

        If the number provided is less than or equal to the total amount of values, it does nothing.

        Parameters:
            :param int tonum: How many total values should be in the row.

        Returns:
            :return: The amount of times it added an empty value.
            :rtype: int
        """
        ct = 0
        while len(self) < tonum:
            self.append('')
            ct += 1
        return ct

    def fill_with(self, amount, times):
        """Fills the row with the value amount times times.

        If times is zero or lower, nothing will loop.

        Parameters:
            :param str amount: The thing to add to the row. It should preferrably be a string.
            :param int times: The amount of times to add it.

        :return: Nothing
        :rtype: None
        """
        for i in range(times):
            self.append(amount)

    def __repr__(self) -> str:
        return 'Row(values = %s)' % str(self).replace('[', '').replace(']', '')


class Column(Row):
    """The Column class. It is nearly identical to the Row class except that you cannot delete the first entry."""

    def __init__(self, value1, *values):
        """Initalizes the class.

        Parameters:
            :param str col1: The name of the first column
            :param tuple cols: The names of the other columns
        """
        super(Column, self).__init__(value1, *values)

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
            raise DeletingOnlyValueException
        else:
            return super(Column, self).pop(index)

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
            raise DeletingOnlyValueException
        else:
            super(Column, self).__delitem__(key)
