# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:32

author @heyao
"""

import re
import json
from urlparse import urlparse, parse_qs


def parse_pre_login(response):
    reg = re.compile(r"\((.*?)\)")
    login_info = json.loads(reg.search(response.body).group(1))
    login_param_keys = ['servertime', 'nonce', 'rsakv']
    pubkey = 'pubkey'
    return {k: login_info[k] for k in login_param_keys}, login_info[pubkey]


def parse_login_callback_info(response):
    reg = re.compile(r"feedBackUrlCallBack\((.*?)\)")
    callback_info = json.loads(reg.search(response.body).group(1))
    return callback_info


def get_msg_from_url(url, key='reason'):
    queries = urlparse(url.decode('gb2312')).query
    return parse_qs(queries)[key][0]
