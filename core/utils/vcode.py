# -*- coding: utf-8 -*-

import hashlib
import random
import requests
from flask import current_app


class Vcode(object):

    @staticmethod
    def random_verification_code():
        return ''.join(random.choice('0123456789') for i in range(6))

    @staticmethod
    def generate_vcode_sign(data):
        SMS_SECRET = 'XiaoYeZi.SMS'
        keys = data.keys()
        keys.sort()
        parameters = "%s%s" % (
            SMS_SECRET,
            str().join('&%s=%s' % (key, data[key]) for key in keys)
        )
        sms_sign = hashlib.md5(parameters).hexdigest()
        return sms_sign

    @staticmethod
    def send_verification_code(phone, vcode):
        data = {
            'sign_name': '尤克里里教室',
            'template_code': 'SMS_0001',
            'json_params': '{"code": "%s"}' % vcode,
            'phone_numbers': str(phone)
        }
        resp = requests.post(current_app.config['SMS_SERVICE_URL'].format(
            sign=Vcode.generate_vcode_sign(data)), data=data)
        if resp.status_code == 200 and resp.json()['code'] == 0:
            return True
        else:
            print 'error:', str(resp), str(resp.json())
            return False

    @staticmethod
    def save_vcode_and_phone(phone, vcode):
        current_app.redis.set(phone, vcode)
        current_app.redis.expire(phone, 5 * 60)

    @staticmethod
    def get_vcode_by_phone(phone):
        return current_app.redis.get(phone)
