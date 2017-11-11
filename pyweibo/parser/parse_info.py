# -*- coding: utf-8 -*-
"""
create on 2017-11-04 下午12:55

author @heyao
"""

import json
from urlparse import urljoin

from pyweibo.regular_expression import *
from pyweibo.xpath_expression import *
from pyweibo.selector.selector import Selector


class WeiboMainPageParser(object):
    def __init__(self, is_login=False):
        self.is_login = is_login

    def parse(self, content):
        return content

    def _parse(self, content):
        main_contents = RE_FM_CONTENT.findall(content)
        if not main_contents:
            raise RuntimeError("can not find right text in 'content' with %s" % RE_FM_CONTENT)
        max_len = 0
        main_content = ''
        for text in main_contents:
            if len(text) > max_len:
                max_len = len(text)
                main_content = text
        json_data = json.loads(main_content)
        if 'html' not in json_data:
            return ''
        return json_data['html']


class WeiboInfoParser(object):
    def __init__(self):
        pass

    def content2weibo(self, content, forward=True, response_url=None):
        sel = Selector(text=content)
        weibos = sel.xpath(XPATH_CONTENT2WEIBO)
        for weibo in weibos:
            yield self.weibo2info(weibo, forward=forward, response_url=response_url)

    def weibo_user_action_id(self, content=None, sel=None):
        sel = sel or Selector(text=content)
        follow_url = sel.xpath(XPATH_UP_ID).extract()[0]
        user_action_id = follow_url.split('/')[4]
        return user_action_id

    # url_info_url = 'https://weibo.com/p/{user_id}/info?mod=pedit_more'.format(user_id=user_id)

    def weibo_basic_info(self, content=None, sel=None):
        sel = sel or Selector(text=content)
        result = {}
        counter = sel.xpath(XPATH_BI_COUNTER).extract()[0]
        result['follow'] = int(counter.xpath(XPATH_BI_FOLLOW)[0])
        result['fans'] = int(counter.xpath(XPATH_BI_FANS)[0])
        result['weibo'] = int(counter.xpath(XPATH_BI_WEIBO)[0])

        def info_collector(xpath, container, is_list=True):
            data = {}
            for key in xpath:
                try:
                    if is_list:
                        value = container.xpath(xpath[key])[0].strip()
                    else:
                        value = container.xpath(xpath[key]).strip().replace('\n', '').replace('\r', '').replace('\t', '')
                except IndexError:
                    value = ''
                if value:
                    data[key.lower()] = value
            return data

        container = sel.xpath(XPATH_BI_CONTAINER).extract()[0]
        result['basic_info'] = info_collector(XPATH_BASIC_INFO, container)
        domain = '|'.join(container.xpath(XPATH_BI_DOMAIN))
        if domain:
            result['basic_info']['domain'] = domain

        contact_info_container = sel.xpath(XPATH_CI_CONTAINER).extract()[0]
        result['contact_info'] = info_collector(XPATH_CONTACT_INFO, contact_info_container)

        work_info_container = sel.xpath(XPATH_WI_CONTAINER).extract()[0]
        result['work_info'] = ['|'.join(i.strip() for i in c.xpath('.//text()') if i.strip()) for c in work_info_container.xpath(XPATH_COMPANY)][1:]

        education_info_container = sel.xpath(XPATH_EI_CONTAINER).extract()[0]
        result['education_info'] = info_collector(XPATH_EDUCATION_INFO, education_info_container, is_list=False)

        tag_info_container = sel.xpath(XPATH_TI_CONTAINER).extract()[0]
        result['tags'] = '|'.join(t.strip() for t in tag_info_container.xpath(XPATH_TI_TAG) if t.strip())
        result['level'] = container.xpath(XPATH_BI_LEVEL)[0]
        result['exp'] = int(container.xpath(XPATH_BI_EXP)[0])
        return result

    def weibo_up_baike_info(self, content=None, sel=None):
        sel = sel or Selector(text=content)
        school = sel.xpath(u'//li[@class="li_2 clearfix" and contains(., "毕业院校")]/span[last()]/text()').extract_first()
        return school

    def _url_type(self, content):
        if content.startswith('#') and content.endswith('#'):
            return 'topic'
        if content.startswith('@'):
            return 'user'
        return 'other'

    def _parse_up_text(self, element, response_url=None):
        """解析阿婆主的文本内容
        :param element: 阿婆主内容的Element对象
        :param response_url: 响应的链接，用于处理链接的相对引用
        :return: dict
        """
        result = {}
        full_text = ''.join(p.strip() for p in element.xpath('.//text()'))
        result['full_text'] = full_text
        result['tags'] = []
        for a in element.xpath('./a'):
            content = a.xpath('./text()')[0]
            result['tags'].append({
                'content': content,
                'url': urljoin(response_url, a.xpath('./@href')[0]),
                'type': self._url_type(content)
            })
        result['up_text'] = full_text.split('//')[0]
        return result

    def weibo2info(self, element, forward=True, response_url=None):
        body = element.xpath(XPATH_BODY)[0]
        data = element.xpath(XPATH_DATA)[0]
        result = {}
        result['weibo_url'] = urljoin(response_url, body.xpath(XPATH_WEIBO_URL)[0])
        result['face_img_url'] = urljoin(response_url, body.xpath(XPATH_FACE_IMG_URL)[0])
        result['nick_name'] = body.xpath(XPATH_NICKNAME)[0]
        result['nick_name_url'] = urljoin(response_url, body.xpath(XPATH_NICKNAME_URL)[0])
        result['up_text'] = self._parse_up_text(body.xpath(XPATH_UP_TEXT)[0], response_url)
        if forward:
            # 转发信息的解析
            pass
        result['feedback'] = {}
        forward_data = data.xpath(XPATH_FORWARD)[0]
        if forward_data == u'转发':
            forward_data = 0
        result['feedback']['forward'] = int(forward_data)
        comment_data = data.xpath(XPATH_COMMENT)[0]
        if comment_data == u'评论':
            comment_data = 0
        result['feedback']['comment'] = int(comment_data)
        like_data = data.xpath(XPATH_LIKE)[0]
        if like_data == u'赞':
            like_data = 0
        result['feedback']['like'] = int(like_data)
        return result


if __name__ == '__main__':
    from pyweibo.http import weibo_downloader
    from pyweibo.weibo.user.login import login
    from pyweibo.urls import API

    cookies, success, user_info = login('', '')

    main_page_parser = WeiboMainPageParser()
    user_id = '1995246233'
    response = weibo_downloader.download(
        'http://weibo.com/1995246233/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1',
        cookies=cookies)
    content = response.text
    # with open('/Users/heyao/Desktop/weibo.html', 'w') as f:
    #     f.write(content)
    print u'他还没有发过微博' in content
    main_content = main_page_parser.parse(content)

    weibo_info_parser = WeiboInfoParser()
    weibos = weibo_info_parser.content2weibo(main_content, response_url='https://weibo.com')
    for weibo in weibos:
        print weibo

    print cookies
    # user_action_id = weibo_info_parser.weibo_user_action_id(content)
    user_action_id = '1005052662018234'
    url_info_url = 'https://weibo.com/p/{user_id}/info?mod=pedit_more'.format(user_id=user_action_id)
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    response = weibo_downloader.download(url_info_url, cookies={'SUB': cookies['SUB']})
    print response.url
    with open('C:\Users\Shen\Desktop\weibo.html', 'w') as f:
        f.write(response.body)
    weibo_basic_info = weibo_info_parser.weibo_basic_info(response.body)
    print weibo_basic_info

    url = 'https://weibo.com/lixiaolu?refer_flag=1001030101_&is_hot=1'
    response = weibo_downloader.download(url)
    sel = Selector(text=response.body)
    next_url = 'https:' + sel.xpath(u'//span[@class="item_text W_fl" and contains(., "百度人物资料")]/a/@href').extract_first()
    response = weibo_downloader.download(next_url)
    content = response.body
    weibo_baike_info = weibo_info_parser.weibo_up_baike_info(content=content)
    print weibo_baike_info
