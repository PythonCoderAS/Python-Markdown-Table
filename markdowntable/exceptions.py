from __future__ import unicode_literals

class SupressedError(Exception):
    """docstring for SupressedError."""
    def __init__(self, error, message):
        super(SupressedError, self).__init__()
        Exception.__init__(self, '''An error has occured. Printing error. information:
        Error Name: {n}
        Error Message: {m}'''.format(n = error,
        m = message))
