# -*- coding: utf-8 -*-

import json
from datetime import datetime


ERROR_CODE = {
    "pwd_error": u'用户名或者密码错误',
    'school_code_error': u'机构代码错误',
    'name_error': u'用户名错误',
    'birth_error': u'生日错误',
    'tencent_id_error': u'视频ID错误',
    'player_error': u'播放器代码错误',
    'type_error': u'类型错误'
}


def render_json(code, data=None):

    resp = {
        'code': code,
        'data': data
    }

    if code == 1:
        resp['data']['err_msg'] = ERROR_CODE[data['err_no']]

    return json.dumps(resp)


def render_students(students):
    pass


def render_videos(videos):
    pass
