from datetime import date
import os

SITE_DETAILS = {'demo001': {'phone': '6398202828', 'site_id': 'DEMO001',
                            'station_name': 'demo station 001'},
                'demo002': {'phone': '7541041991', 'site_id': 'DEMO002',
                            'station_name': 'demo station 002'},
                'demo003': {'phone': '9997168997', 'site_id': 'DEMO003',
                            'station_name': 'demo station 003'},
                }

LOG_DT_FORMAT = "%(asctime)s - %(message)s"
READING_DB_FILE = '/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring/formatter_service/reading_db.txt'

TDAY = date.today().strftime('%d%b%Y')
RAW_FILES_DESTINATION = "/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring/autogenerated_raw_files/raw_files/"
LAST_FILE_BASE = os.path.join(RAW_FILES_DESTINATION, 'LAST_FILE')
CURRENT_DATE_BASE = os.path.join(RAW_FILES_DESTINATION, TDAY)
TODAYS_BASE = os.path.join(RAW_FILES_DESTINATION, TDAY)
BUFFER_BASE = os.path.join(TODAYS_BASE, 'UNPROCESSED')
PROCESSED_BASE = os.path.join(TODAYS_BASE, 'PROCESSED')
TODAYS_JUNK = os.path.join(RAW_FILES_DESTINATION, TDAY + '_BAD_FILES')
