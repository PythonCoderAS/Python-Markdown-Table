import logging

from pokestarfansloggingsetup import setup_logger

logger = setup_logger('quicktest', loglevel=logging.DEBUG)


def quicktest():  # this is so it can be imported.
    try:
        import markdowntable
        exble = markdowntable.Table('ex 1')
        logging.info('Run create table')
        exble.all_columns(1, 2, 3, 4, 5, 6, 7, 8, 9)
        logging.info('Run all columns')
        exble.add_row(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        logging.info('Run add row with 10/11 values')
        exble.add_row(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        logging.info('Run add row with 11/11 values')
        try:
            exble.add_row(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        except markdowntable.exceptions.TooManyValues:
            logging.info('TooManyValues exception found, sucess', exc_info=True)
        exble.export_table_to_file(filename='test 1')
        logging.info('Run export table to file')
        exble.export_table_to_file(filename='test 2', mode='w')
        logging.info('Run export table to file with mode w')
        exble.export_table_to_file(filename='test 3', mode='a')
        logging.info('Run export table to file with mode a')
        logging.debug(exble.debug(print_d=False))
    except Exception as e:
        logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    quicktest()
