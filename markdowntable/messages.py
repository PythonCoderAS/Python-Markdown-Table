"""
Part of Python-Markdown-Table. Contains the messages the main program uses.
"""


def not_enough_values(rows_made, columns):
    """

    :param rows_made: string
    :param columns: string
    :return: string
    """
    message = "You did not enter in enough values. You entered in {} values out of {} values. The values that you did" \
              " " \
              "not enter in will be filled in with a blank space. You can stop this message from appearing by adding " \
              "the argument show_warning_message = False".format(str(rows_made), str(columns))
    return message


overwrite_message = 'This file already contains content. Do you want to overwrite the contents of the file? You can ' \
                    'add the argument mode = a[+] to not overwrite. '
