# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:40

author @heyao
"""

import re
import sys
import binascii
from copy import deepcopy
from time import time
from urllib2 import quote, unquote

from pyweibo.utils.log import get_logger
from pyweibo.utils.basen import bnencode
from pyweibo.utils.rsa_ import Rsa
from pyweibo.http import weibo_downloader
from pyweibo.http.downloader import cookie_format
from pyweibo.urls import API, FORMDATA, HEADERS
from pyweibo.parser.parse_response import parse_pre_login, parse_login_callback_info, get_msg_from_url

reload(sys)
sys.setdefaultencoding('utf-8')

logger = get_logger(__name__, "INFO")


def redirect(text):
    reg = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
    redirect_url = reg.search(str(text)).group(1)
    ret_code = get_msg_from_url(unquote(redirect_url), 'retcode')
    success = ret_code == '0'
    return redirect_url, success


def login(username, password):
    pre_url = API['PRE_LOGIN'].format(timestamp=int(time()))
    response = weibo_downloader.download(pre_url)
    login_params, pubkey = parse_pre_login(response)

    login_data = FORMDATA['LOGIN']
    username = _username_encode(username)
    password = _password_encrypt(password, login_params, pubkey)
    login_data.update(dict(
        su=username,
        sp=password
    ))
    login_data.update(login_params)

    login_url = API['LOGIN']
    headers = HEADERS['LOGIN_HEADERS']
    response = weibo_downloader.download(login_url, data=login_data, headers=headers)
    redirect_url, success = redirect(response.body)
    if success:
        redirect_response = weibo_downloader.download(redirect_url)
        user_info = parse_login_callback_info(redirect_response)
        cookies = cookie_format(response.cookies, 'dict')
        response = weibo_downloader.download(API['SAVE_STATE'], cookies=cookies)
        logger.info("login success")
        cookies.update(cookie_format(response.cookies, 'dict'))
        return cookies, success, user_info
    else:
        reason = get_msg_from_url(unquote(redirect_url), key='reason')
        logger.info("login failure because: {reason}".format(reason=reason))
        return {}, success, {}


def _username_encode(username):
    return bnencode(quote(username))


def _password_encrypt(password, login_params, n16):
    rsa_cryptor = Rsa()
    pubkey = rsa_cryptor.key_from_n16(n16)
    msg_data = deepcopy(login_params)
    msg_data.update(dict(
        password=password
    ))
    message = '{servertime}\t{nonce}\n{password}'.format(**msg_data)
    return binascii.b2a_hex(rsa_cryptor.encrypt(message, pubkey))


if __name__ == '__main__':
    username = ''
    password = ''
    cookies, success, user_info = login(username, password)
    print user_info
    user_url = API['USER_HOME'].format(user_id='2662018234', page=1)
    print user_url
    response = weibo_downloader.download(user_url, cookies=cookies)
    ind = response.body.find(u'我的相册')
    print(ind)
