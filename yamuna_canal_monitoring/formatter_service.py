import os
from datetime import datetime
import json
import logging
from os.path import basename
from monitoring_app.models import *
from yamuna_canal_monitoring.GLOBAL_DEV import SITE_DETAILS, READING_DB_FILE,\
    LOG_DT_FORMAT
# from yamuna_canal_monitoring.GLOBALS import SITE_DETAILS, READING_DB_FILE,\
#     LOG_DT_FORMAT
import celerytasks
from monitoring_app.models import Site, SiteInfo, Reading2022

logging.basicConfig(filename='/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring/formatter.log', filemode='a', format=LOG_DT_FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


class FTPRequest:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = basename(self.filepath)
        self.station = None
        self.ftype = None

    def initiate(self):
        if self.filepath.endswith('.json'):
            details = self.get_json_details()
            celerytasks.move2last_file(details)
    
    def get_json_details(self):
        response = {}
        fpath = self.filepath
        response['current_flpath'] = fpath
        with open(fpath) as f:
            json_data = json.load(f)
            response = json_data
        self.prefix = response.get('prefix')
        self.ts = int(response.get('timestamp'))
        self.timeStamp = datetime.utcfromtimestamp(self.ts).strftime('%Y-%m-%d %H:%M:%S')
        self.reading_data = response.get('data')
        self.reading_string = self.format_reading2wims()
        self.reading = self.timeStamp + " \t---\t " + self.prefix + " \t---\t " + self.reading_string + "\n"
        self.write2db_file()
        self.db_reading = self.format_reading2db()
        self.upload2db()
        return response
    
    def format_reading2wims(self):
        self.reading_string = []
        get_id = SITE_DETAILS.get(self.prefix,'')
        if get_id:
            station_id = SITE_DETAILS.get(self.prefix).get('site_id')
            phone = SITE_DETAILS.get(self.prefix).get('phone')
            self.reading_string = ['&' + station_id,datetime.utcfromtimestamp(self.ts).strftime('%d/%m/%Y %H:%M'), str(phone)]
        param_array = self.reading_data.keys()
        for i in param_array:
            self.reading_string.append(str(self.reading_data[i]['value']))
        self.reading_string = ','.join(self.reading_string)
        return self.reading_string

    def format_reading2db(self):
        self.db_reading = []
        param_array = self.reading_data.keys()
        for i in param_array:
            data_string = f'"{i}"=>"{self.reading_data[i]["value"]}"'
            self.db_reading.append(str(data_string))
        self.db_reading = ','.join(self.db_reading)
        print('self.db_reading >>>> ',self.db_reading)
        return self.db_reading

    def write2db_file(self):
        try:
            with open(READING_DB_FILE, 'a') as db_writer:
                db_writer.write(self.reading)
        except Exception as err:
            print('Unable to write to DB file due to : ',err)

    def upload2db(self):
        try:
            site_obj = Site.objects.get(prefix__iexact = self.prefix)
            db_record = Reading2022(site=site_obj, readings=self.db_reading, timestamp=datetime.now())
            db_record.save()
            print('reading saved!')
        except:
            print('%s prefix site not found', self.prefix)



    

