from __future__ import unicode_literals


class MarkdownTableException(Exception):
    """
    Base class exception for all exceptions in the module.
    """
    def __init__(self, debug):
        """
        The initiator

        :type debug: str
        :param debug: Debug information from Table().debug()
        :return: Nothing
        :rtype: None
        """
        Exception.__init__(self,
                           'There is an error with your Markdown Table. Printing debug information. \n {debug}'.format(
                               debug=debug))


class SuppressedError(MarkdownTableException):
    """docstring for SuppressedError. The error is raised when an actual error is called, along with debug info."""

    def __init__(self, error, message, debug):
        """
        The initiator.

        :type error: str
        :type message: str
        :type debug: str
        :param error: The error name
        :param message: The error message
        :param debug: Debug info from Table().debug()
        """
        Exception.__init__(self, '''An error has occured. Printing error. information:
        Error Name: {n}
        Error Message: {m}
        Debug Info: {d}'''.format(n=error, m=message, d=debug))


class TooManyValues(MarkdownTableException):
    """
    The error is raised when row info has more values than columns
    """
    def __init__(self, columns):
        """
        The initiator.

        :param columns: The amount of columns
        :return: Nothing
        :rtype: None
        """
        Exception.__init__(self,
                           'You entered in too many row values. Please only enter {} row names.'.format(str(columns)))


