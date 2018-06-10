import logging
import time

from pokestarfansloggingsetup import setup_logger

import markdowntable.inputs

logger = setup_logger('quicktest', loglevel=logging.DEBUG)


def quicktest(sleep=0):  # this is so it can be imported.
    try:
        import markdowntable
        exble = markdowntable.Table('ex 1')
        logging.info('Run create table')
        time.sleep(sleep)
        exble.all_columns(1, 2, 3, 4, 5, 6, 7, 8, 9)
        time.sleep(sleep)
        logging.info('Run all columns')
        time.sleep(sleep)
        exble.add_row(1, 2, 3, 4, 5, 6, 7, 8, 9)
        time.sleep(sleep)
        logging.info('Run add row with 10/11 values')
        try:
            exble.add_row(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        except markdowntable.exceptions.TooManyValues:
            time.sleep(sleep)
            logging.info('TooManyValues exception found, sucess', exc_info=True)
        exble.export_table_to_file(filename='test 1')
        time.sleep(sleep)
        logging.info('Run export table to file')
        exble.export_table_to_file(filename='test 2', mode='w')
        time.sleep(sleep)
        logging.info('Run export table to file with mode w')
        exble.export_table_to_file(filename='test 3', mode='a')
        time.sleep(sleep)
        logging.info('Run export table to file with mode a')
        logging.debug(exble.debug(print_d=False))
        csvle = markdowntable.inputs.import_from_csv('bitcoinprices')
        time.sleep(sleep)
        logging.info(csvle.table)
        time.sleep(sleep)
        logging.debug(csvle.debug(print_d=False))
        time.sleep(sleep)
        '''
        codele = markdowntable.inputs.import_from_code(csvle.table)
        time.sleep(sleep)
        logging.info(codele.table)
        time.sleep(sleep)
        logging.debug(codele.debug(print_d=False))
        time.sleep(sleep)
        '''
    except Exception as e:
        logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    quicktest()
