# -*- coding: utf-8 -*-
"""
create on 2017-11-05 下午1:04

author @heyao
"""

import cPickle

from pyweibo.http import weibo_downloader
from pyweibo.weibo.user.login import login

try:
    with open('cookies.pkl', 'r') as f:
        cookies = cPickle.load(f)
except IOError:
    cookies = None
if cookies is None:
    print 'log in with username & password'
    user_name = ''
    password = ''
    cookies, success, user_info = login(username=user_name, password=password)
    if success:
        with open('cookies.pkl', 'w') as f:
            cPickle.dump(cookies, f)
url = 'http://weibo.com/2662018234/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'
response = weibo_downloader.download(url, cookies=cookies)
content = response.body
print content.find(u'我的相册')
