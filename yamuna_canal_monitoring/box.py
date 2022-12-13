import os

GKCONF = '/etc/supervisor/conf.d/gatekeeper.conf'


def setting_type():
    # if os.path.exists(GKCONF):
    #     return {
    #         'settings': 'aaxisnit.box_settings.gk',
    #         'path': '/var/www/apps/aaxipro/aaxisnit',
    #         'env': '/var/www/apps/env3_7/lib/python3.7/site-packages'
    #     }
    return {
        'settings': 'yamuna_canal_monitoring.box_settings.web',
        'path': '/home/rohit/Desktop/eyc/yamuna_canal_monitoring/yamuna_canal_monitoring',
        'env': '/home/rohit/Desktop/eyc/env/lib/python3.8/site-packages'
    }