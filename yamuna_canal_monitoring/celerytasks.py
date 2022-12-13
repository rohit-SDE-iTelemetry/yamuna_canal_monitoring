import os
import sys
import django
import shutil

# django settings
sys.path.append('/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring')
from box import setting_type
_ = setting_type()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", _.get('settings'))
sys.path.append(_.get('path'))
sys.path.append(_.get('env'))
django.setup()


from yamuna_canal_monitoring.GLOBAL_DEV import RAW_FILES_DESTINATION, TDAY,\
    LAST_FILE_BASE, PROCESSED_BASE

# from yamuna_canal_monitoring.GLOBAL import RAW_FILES_DESTINATION, TDAY,\
#     LAST_FILE_BASE, PROCESSED_BASE

def move2last_file(detail):
    prefix = detail.get('prefix').lower()
    current_flpath = detail.get('current_flpath')
    extnsion = os.path.splitext(current_flpath)[-1]
    fname_nw = os.path.join(LAST_FILE_BASE, prefix + extnsion)
    # processed_nw = os.path.join(LAST_FILE_BASE, prefix + extnsion)

    shutil.copyfile(current_flpath, fname_nw)
    shutil.move(current_flpath, PROCESSED_BASE)