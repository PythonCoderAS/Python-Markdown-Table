from markdowntable import Table


def import_from_csv(filename: str, extension: str = 'csv'):
    """
    Creates a table from a csv.

    :type extension: str
    :type filename: str
    :param filename: The csv filename
    :param extension: The extension, default csv
    :return: markdown.Table object
    """
    global header_row, csv_table
    with open(filename + '.' + extension, 'r') as file:
        rows = file.read().split('\n')
        row_num = 0
        for row in rows:
            entries = row.split(',')
            if row_num == 0:
                header_row = True
            if header_row:
                first_entry = entries[0]
                entries.remove(first_entry)
                csv_table = Table(first_entry)
                for entry in entries:
                    csv_table.add_column(entry)
                header_row = False
            else:
                csv_table.add_row_with_list(entries)

            row_num += 1
    return csv_table


def import_from_code(code: str):
    """
    The function makes a table from existing Markdown code.

    :type code: str
    :param code: The code to use
    :return: The table
    :rtype: markdown.Table object
    """
    global codetable
    lines = code.split('\n')
    altlines = []
    for line in lines:
        if '|---|' not in line:
            altlines.append(line)
    lines = altlines
    line_no = 0
    for line in lines:
        entries = line.split('|')
        if line_no == 0:
            codetable = Table(entries[0])
            entries.remove(entries[0])
            codetable.all_columns_with_list(entries)
        else:
            codetable.add_row_with_list(entries)
        line_no += 1
    return codetable
