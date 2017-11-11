# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:11

author @heyao
"""

import re
import socket
from urllib import urlencode
from urllib2 import unquote

import requests

from pyweibo.http.response import Response
from pyweibo.selector.selector import Selector


def cookie_format(cookies, type='dict'):
    cookie_dict = {}
    for cookie in cookies:
        name = cookie.name
        cookie_dict[name] = cookie.value
    if type == 'dict':
        return cookie_dict
    return urlencode(cookie_dict).replace('&', ';')


def weibo_headers(cookies):
    headers = {
        'User-Agent': 'Baiduspider'
    }
    if isinstance(cookies, dict):
        return dict(Cookie=cookie_format(cookies), **headers)
    return dict(Cookie=cookies, **headers)


class Downloader(object):
    def __init__(self, cookie_enable=False):
        self.cookie_enable = cookie_enable
        self.reg = re.compile(r"charset=(.*?)")
        # self.cookies = None

    def download(self, url, headers=None, data=None, cookies=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT, method='GET', **options):
        headers = headers or {}
        if data:
            method = 'POST'
        headers['User-Agent'] = 'Baiduspider'
        ua = options.pop('ua', None)
        if ua:
            headers['User-Agent'] = ua
        options.update(dict(
            headers=headers,
            data=data,
            timeout=timeout
        ))
        # if self.cookie_enable:
        #     options.update(dict(
        #         cookies=self.cookies
        #     ))
        if cookies is not None:
            options['cookies'] = cookies
        # if cookies:
        #     options['cookies'] = cookies
        response = requests.request(method=method, url=url, **options)
        # self.cookie_dict.update(cookie_format(response.cookies, type='dict'))
        # if self.cookies:
        #     self.cookies.update(response.cookies)
        # else:
        #     self.cookies = response.cookies
        response_obj = Response(response)
        sel = Selector(text=response.text)
        text = response.text
        setattr(response_obj, "text", text)
        setattr(response_obj, "content", response.content)
        setattr(response_obj, "cookies", response.cookies)
        encoding_str = sel.xpath('//meta[contains(@content, "charset")]/@content').extract_first()
        if encoding_str:
            encoding = self.reg.search(encoding_str).group(1)
            if encoding:
                setattr(response_obj, "encoding", encoding)
                text.decode(encoding, 'ignore')
        setattr(response_obj, "body", text)
        return response_obj


if __name__ == '__main__':
    downloader = Downloader(True)
    data = {
        'loginName': 15647238472,
        'loginPwd': 123,
        'qqCode': '',
        'sCookie': '',
        'imgcode': 26,
        'rnd': 0.45617345410825316,
    }
    response_post = downloader.download('http://www.xxsy.net/login/doLogin', data=data)
    pass
