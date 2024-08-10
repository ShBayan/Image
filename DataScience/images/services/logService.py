from string import Template
from datetime import date
import os

class LogService:
    @staticmethod
    def set_file_error(filename, url, error_message, error_key, vendor, collection, design):

        LogService.write_file(
            Template('${fn},${url},${ke},${em}').substitute(fn=filename, url=url, ke=error_key, em=error_message),vendor, collection, design)

    @staticmethod
    def write_file(error, vendor, collection, design):
        try:
            d = date.today()
            current_date = str(d)

            if not os.path.exists('LogErrors'):
                os.mkdir('LogErrors')

            f = open('LogErrors/log_' + current_date + '_' + vendor + '_' + collection + '_' + design +'.txt','a+')
            f.write(error + '\n' + '*******************************************' + '\n')
            f.close()
        except Exception as e:
            print('file:', str(e), 'in create log file')
