"""
Part of Python-Markdown-Table. Contains the messages the main program uses.
"""


def not_enough_values(rows_made: str, columns: str):
    """
    Displays the not_enough_values message with arguments

    :type columns: str
    :type rows_made: str
    :param rows_made: The amount of row values created by the program
    :param columns: The total amount of columns
    :return: The message
    :rtype: str
    """
    message = "You did not enter in enough values. You entered in {} values out of {} values. The values that you did" \
              " " \
              "not enter in will be filled in with a blank space. You can stop this message from appearing by adding " \
              "the argument show_warning_message = False".format(str(rows_made), str(columns))
    return message


overwrite_message = 'This file already contains content. Do you want to overwrite the contents of the file? You can ' \
                    'add the argument mode = a[+] to not overwrite. '

no_more_rows = 'There are no more rows left in the table. If you would like to remove a column, please use the ' \
               'remove_column function.'
