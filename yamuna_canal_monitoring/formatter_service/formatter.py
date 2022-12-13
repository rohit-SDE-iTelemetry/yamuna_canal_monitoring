import os
from datetime import datetime
import json
import logging
from os.path import basename
import sys 
import django

# django settings
sys.path.append('/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring')
from box import setting_type
_ = setting_type()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", _.get('settings'))
sys.path.append(_.get('path'))
sys.path.append(_.get('env'))
django.setup()

from yamuna_canal_monitoring.GLOBALS import SITE_DETAILS, READING_DB_FILE
from formatter_service import celerytasks

FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename='/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring/formatter_service/formatter.log', filemode='a', format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


class FTPRequest:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = basename(self.filepath)
        self.station = None
        self.ftype = None

        print('self.filepath >>>> ',self.filepath)
        print('self.filename >>>> ',self.filename)


    def initiate(self):
        print('%s: initiate' % self.filename)
        if self.filepath.endswith('.json'):
            print('%s: initiate details received' % self.filename)
            details = self.get_json_details()
            print('details >>>> ',details)

            fls = []
            for idx, detail in enumerate(details):
                self.to_tpro(detail)
                tmp_kwargs = {
                    'prefix': detail.get('prefix'),
                    'current_flpath': detail.get('filename'),
                }
                fls.append(tmp_kwargs)
            celerytasks.move2last_file(fls)

    
    def get_json_details(self):
        response = {}
        fpath = self.filepath
        print('fpath >>> ',fpath)
        with open(fpath) as f:
            json_data = json.load(f)
            print('json data >>>>> ',json_data, type(json_data))
            response = json_data
        
        print('response >>>> ',response)

        self.prefix = response.get('prefix')
        ts = int(response.get('timestamp'))
        self.timeStamp = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        reading_data = response.get('data')
        self.reading_string = []

        get_id = SITE_DETAILS.get(self.prefix,'')

        if get_id:
            station_id = SITE_DETAILS.get(self.prefix).get('site_id')
            phone = SITE_DETAILS.get(self.prefix).get('phone')
            self.reading_string = ['&' + station_id,datetime.utcfromtimestamp(ts).strftime('%d/%m/%Y %H:%M'), str(phone)]

        param_array = reading_data.keys()
        print('param_array >>>>>> ',param_array)
        for i in param_array:
            param_val = reading_data[i]['value']
            self.reading_string.append(str(param_val))
            
        self.reading_string = ','.join(self.reading_string)
        print('self.reading_string >>>> ',self.reading_string)

        self.reading = self.timeStamp + " \t---\t " + self.prefix + " \t---\t " + self.reading_string + "\n"
        self.write2db_file()
        self.upload2db()
    

    # def get_csv_details(self):
    #     response = {}
    #     fpath = self.filepath
    #     print('fpath >>> ',fpath)
    #     with open(fpath) as f:
    #         json_data = json.load(f)
    #         print('json data >>>>> ',json_data, type(json_data))
    #         response = json_data
    #     print('response >>>> ',response)

    
    def write2db_file(self):
        try:
            with open(READING_DB_FILE, 'a') as db_writer:
                db_writer.write(self.reading)
        except Exception as err:
            print('Unable to write to DB file due to : ',err)


    def upload2db(self):
        pass



    

