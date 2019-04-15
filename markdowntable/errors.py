"""This class defines all exceptions used by the module."""

from __future__ import unicode_literals


class MarkdownTableException(ValueError):
    """This class is the base exception class for all exceptions in the module."""


class DeletingOnlyException(MarkdownTableException):
    """This class is the base exception class for exceptions that involve deleting a value that cannot be deleted."""


class DeletingOnlyValueException(DeletingOnlyException):
    """This class is for the exception of deleting the only value in a column."""

    def __init__(self):
        super(DeletingOnlyValueException, self).__init__('You tried deleting the only value in the column. To access '
                                                         'the value, do col[0]')


class DeletingOnlyColumnException(DeletingOnlyException):
    """This class is for the exception of deleting the only column in a table"""

    def __init__(self):
        super(DeletingOnlyColumnException, self).__init__('You tried deleting the only column in the table. To access '
                                                          'the column, do table[0]')


class InvalidException(MarkdownTableException):
    """This class is the base exception class for exceptions that involve not having the same amount of values in a row
    as the amount of values in the column."""

    def __init__(self, rnum, expected, actual, val=''):
        """Initializes the class

        Parameters:
            :param int rnum: The row number
            :param int expected: The expected values
            :param int actual: The actual values
        """
        super(InvalidException, self).__init__('Row number %d contains too %s values. It needs to contain %d values'
                                               ', but contains %d values.' % (rnum, val, expected, actual))


class TooLittleValuesException(InvalidException):
    """This exception is for when there are too little values in a row."""

    def __init__(self, rnum, expected, actual):
        """Initializes the class

        Parameters:
            :param int rnum: The row number
            :param int expected: The expected values
            :param int actual: The actual values
        """
        super(TooLittleValuesException, self).__init__(rnum, expected, actual, 'little')


class TooManyValuesException(InvalidException):
    """This exception is for when there are too many values in a row."""

    def __init__(self, rnum, expected, actual):
        """Initializes the class

        Parameters:
            :param int rnum: The row number
            :param int expected: The expected values
            :param int actual: The actual values
        """
        super(TooManyValuesException, self).__init__(rnum, expected, actual, 'many')
