import os
from datetime import datetime
import time
import json
import random
import csv
import logging

FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename='/home/nayan/yamuna_canal dev/project source code/git/yamuna_canal_monitoring/yamuna_canal_monitoring/autogenerated_raw_files/raw-file-generater.log', filemode='a', format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


today = datetime.now()
# change this according to your folder file location
RAW_FILES_DESTINATION = "/home/nayan/yamuna_canal dev/project source code/git/yamuna_canal_monitoring/yamuna_canal_monitoring/autogenerated_raw_files/raw_files/"

try:
    os.mkdir(RAW_FILES_DESTINATION + today.strftime('%d%b%Y'))
    log.info('raw file folder creatwd for date : %s' % today.strftime('%d%b%Y'))
except Exception as err:
    log.exception('Error : %s' % err)
    pass
    

# new location for storing raw files
# NEW_RAW_FILES_DESTINATION = RAW_FILES_DESTINATION + today.strftime('%Y%b%d')


site_array = [{'demo001':'demo001'}]
station_array = ['station001','station002','station003']
param_array = ['battery','waterLevel','flowRate','gateOpening','velocity']

'''
raw json data format : {
                        'station_id':'xxxxxx',
                        'timestamp':1663922661,
                        'data':{'battery':{'value':xx,'unit':xx},
                                'waterLevel':{'value':xx,'unit':xx},
                                'flowRate':{'value':xx,'unit':xx},
                                'gateOpening':{'value':xx,'unit':xx},
                                'velocity':{'value':xx,'unit':xx}
                                }
                        }
'''

'''
generate random values for params values
'''
def get_random_value(param):
    if(param == 'battery'):
        value = random.uniform(10.5, 45.5)
        return round(value,2),'v'
    elif(param == 'waterLevel'):
        value = random.uniform(0.01, 4)
        return round(value,2),'m'
    elif(param == 'flowRate'):
        value = random.uniform(0.01, 5.00)
        return round(value,2),'m3/s'
    elif(param == 'gateOpening'):
        value = random.uniform(0.01, 100)
        return round(value,2),'mm'
    elif(param == 'velocity'):
        value = random.uniform(3, 10)
        return round(value,2),'m/s'

'''
generate raw json formatted files
'''
def generate_files():
    json_array = {}
    station_id = station_array[int(random.uniform(0, len(station_array)))]
    unix_ts = int(time.time())
    json_array['station_id'] = station_id
    json_array['timestamp'] = unix_ts
    param_json = {}
    for i in param_array:
        random_val = get_random_value(i)
        param_json[i] = {'value':random_val[0],'unit':random_val[1]}
    json_array['data'] = param_json

    print('json_array >>>> ',json_array,)
    # Writing to a .json file
    with open(f"{RAW_FILES_DESTINATION}/{today.strftime('%d%b%Y')}/{station_id}_{unix_ts}.json", "w") as jsonFile:
        jsonFile.write(json.dumps(json_array))
        log.info('%s data : %s' % (station_id,json.dumps(json_array)))
    # Writing to a .csv file
    # Todo : by Rohit Kumar


'''
function call for generating raw json files
'''
i = 0
n = 10
while i <= n:
    time.sleep(5)
    generate_files()
    i = i+1  


