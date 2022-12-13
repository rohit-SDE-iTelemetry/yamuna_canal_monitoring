import os
import sys
import django
from datetime import datetime,date
from os.path import basename

# django settings
sys.path.append('/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring')
from box import setting_type
_ = setting_type()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", _.get('settings'))
sys.path.append(_.get('path'))
sys.path.append(_.get('env'))

from django.conf import settings
from yamuna_canal_monitoring.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()

import inotify.adapters
from multiprocessing import Process
import threading
import enum
import shutil

from yamuna_canal_monitoring.GLOBAL_DEV import TODAYS_BASE,\
    BUFFER_BASE,  TODAYS_JUNK, LAST_FILE_BASE, PROCESSED_BASE

# from yamuna_canal_monitoring.GLOBALS import TODAYS_BASE,\
#     BUFFER_BASE,  TODAYS_JUNK, LAST_FILE_BASE, PROCESSED_BASE
# from formatter_service import formatter
import formatter_service

class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == SIZE_UNIT.KB:
        return size_in_bytes / 1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes / (1024 * 1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes


def move_to_junk_folder(file_name):
    bsname = os.path.basename(file_name)
    print('%s: is junk' % file_name)
    try:
        hourly_junk_loc = os.path.join(TODAYS_JUNK,
                                       datetime.now().strftime('%H_%p'))
        if not os.path.exists(hourly_junk_loc):
            os.mkdir(hourly_junk_loc)
        junk_loc = os.path.join(hourly_junk_loc, bsname)
        if os.path.exists(file_name):
            shutil.move(file_name, junk_loc)
            print('junk file %s moved to %s' % (bsname, junk_loc))

    except Exception as err:
        print('%s: failed to move junk file err: %s' % (bsname, err))


def file_size_allowed(file_name, size_type=SIZE_UNIT.KB):
    """ Get file in size in given unit like KB, MB or GB"""
    try:
        size = os.path.getsize(file_name)
        size_of_file = round(convert_unit(size, size_type), 2)
        fname = os.path.basename(file_name)
        print('%s size %s KB' % (fname, size_of_file))
        if size_of_file > 140 and fname.startswith(
                datetime.now().strftime('%Y%m%d_')):
            return False
        print('%s size %s KB' % (fname, size_of_file))
        return True
    except:
        pass


def check4raw_file():
    """
    Keeps an eye on gatekeeper directory for every entry of file and puts it
    in a queue.

    """
    i = inotify.adapters.Inotify()
    i.add_watch(TODAYS_BASE)

    for event in i.event_gen():
        if event is not None:
            (header, type_names, watch_path, filename) = event
            if 'IN_CLOSE_WRITE' in type_names and (
                    filename.endswith('.csv') or filename.endswith(
                '.CSV') or filename.endswith('.json')):
                old_loc = os.path.join(watch_path, filename)
                print("%s: received via FTP" % filename)
                if file_size_allowed(os.path.join(watch_path, filename)):
                    new_loc = os.path.join(BUFFER_BASE, filename)
                    try:
                        shutil.move(old_loc, new_loc)
                        dest = new_loc
                    except Exception as err:
                        dest = old_loc
                        print('failed to move %s' % old_loc)
                    thread = threading.Thread(target=process, args=(dest,))
                    thread.start()
                    thread.join(2)
                else:
                    print('%s file size not allowed' % filename)
                    move_to_junk_folder(os.path.join(watch_path, filename))


def process(f):
    """
    picks file from check4raw_file queue and processes it further...
    """
    try:
        g = formatter_service.FTPRequest(f)
        g.initiate()
    except FileNotFoundError:
        print('%s not found' % f)
    except Exception as error:
        if type(error).__name__ == 'ConnectionError':
            print('%s: Server not responding...', basename(f))
        elif type(error).__name__ == 'ReadTimeout':
            print('%s: Server took too long to respond.',
                      basename(f))
        else:
            print("ERROR: %s "
                      "Reason: %s", basename(f), error)
        print('%s: %s', basename(f), error)


def prerequisite():
    print('_______ SERVER RESTARTING _______')
    dir2chk = [TODAYS_BASE,
                BUFFER_BASE,
                TODAYS_JUNK, 
                LAST_FILE_BASE,
                PROCESSED_BASE,
                ]
    for dr in dir2chk:
        if not os.path.exists(dr):
            os.mkdir(dr)
    print('_______ SERVER RESTARTED _______')


def _main():
    prerequisite()
    p = Process(target=check4raw_file, daemon=True)
    p.start()
    p.join()


if __name__ == '__main__':
    _main()