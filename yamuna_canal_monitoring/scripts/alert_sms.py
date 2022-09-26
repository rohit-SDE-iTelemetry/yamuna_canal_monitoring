import json
import requests
import logging

log = logging.getLogger('ymc')

AAXIS_SMS = "YAMUNA CANAL MONITORING\n Site: {prefix}\n Gate: {gate_prefix}\n Action: {action}"
SMS_CONTEXT = []

def gate_action(**kwargs):
    # TODO: SEND SMS ALERT WHEN GATE IS OPENED/CLOSED
    prefix = kwargs.get('prefix')
    gate_prefix = kwargs.get('gate_prefix')
    action = kwargs.get('action')

    # site = Site.objects.get(prefix__iexact=prefix)
    try:
        numbrs = site.user_ph.split(';')
    except:
        pass
    numbers = ["7217392393"]

    ALERT_MSG = AAXIS_SMS.format(**kwargs)

    sms_context = {
                # replace & with and else JSON will fail
                'content': ALERT_MSG,
                'sender': "AAXISN",
                'numbers': numbers,
                'prefix': prefix
            }
    SMS_CONTEXT.append(sms_context)
    send_sms_alert(SMS_CONTEXT)
    # send_email_alert()


def send_sms_alert(sms_context_lst):
    for context in sms_context_lst:
        prefix = context.get('prefix')
        list_numbers = context.get('numbers', [])  # list of numbers
        msg_content = context.get('content')

    sender = context.get('sender')  # "AAXISN"
    for numbr in list_numbers:
        if len(numbr) < 10:
            log.warning('not a valid number:%s' % prefix)
            continue
        sms = []
        tmp = {"to": "%s" % numbr,
                "msgid": "1",
                "message": "%s" % msg_content,
                "sender": sender
                }
        sms.append(tmp)
        json_to_send = {'sender': 'FALERT',
                        'sms': sms,
                        'unicode': 0,
                        'flash': 0
                        }
        url = 'https://api-alerts.kaleyra.com/v4/?api_key=Afec70c518d25680e63d76509a7af705a&method=sms.json&json=' + str(
            json.dumps(json_to_send))
        # resp = requests.get(url)
        print(url)

if __name__ == '__main__':
    log.info('SMS Alert script initiated!')
    q = {
        "prefix" : "site1",
        "gate_prefix" : "gate25",
        "action" : 1,
    }
    gate_action(**q)

    

 