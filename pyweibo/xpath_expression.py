# -*- coding: utf-8 -*-
"""
create on 2017-11-05 下午9:01

author @heyao
"""

XPATH_CONTENT2WEIBO = '//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like "]'
XPATH_BODY = './div[@node-type="feed_content"]'
XPATH_DATA = './div[@class="WB_feed_handle"]'
XPATH_FACE_IMG_URL = './div[@class="WB_face W_fl"]//img/@src'
XPATH_NICKNAME = './div[@class="WB_detail"]/div[@class="WB_info"]/a/text()'
XPATH_NICKNAME_URL = './div[@class="WB_detail"]/div[@class="WB_info"]/a/@href'
XPATH_AT = './div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a[1]/text()'
XPATH_WEIBO_URL = './div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a[1]/@href'
XPATH_PLATFORM = './div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a[2]/text()'
XPATH_UP_TEXT = './div[@class="WB_detail"]/div[@class="WB_text W_f14"]'

XPATH_UP_ID = '(//a[@class="t_link S_txt1"]/@href)[1]'

XPATH_DATA_BODY = './div[1]/ul'
XPATH_FORWARD = './/a[@action-type="fl_forward"]//span[@node-type="forward_btn_text"]//em[last()]/text()'
XPATH_COMMENT = './/a[@action-type="fl_comment"]//span[@node-type="comment_btn_text"]//em[last()]/text()'
XPATH_LIKE = './/li[last()]/a/span/span/span/em[last()]/text()'  # 不知道为什么必需用 //

# ================= BASIC INFO ===================
XPATH_BI_COUNTER = '//table[@class="tb_counter"]/tr'
XPATH_BI_FOLLOW = './td[1]/a/strong/text()'
XPATH_BI_FANS = './td[2]/a/strong/text()'
XPATH_BI_WEIBO = './td[3]/a/strong/text()'

XPATH_BI_CONTAINER = '//div[@class="PCD_text_b PCD_text_b2"]/div[2]/div/ul'
XPATH_BI_NICKNAME = u'./li[contains(., "昵称：")]/span[last()]/text()'
XPATH_BI_ADDRESS = u'./li[contains(., "所在地：")]/span[last()]/text()'
XPATH_BI_SEX = u'./li[contains(., "性别：")]/span[last()]/text()'
XPATH_BI_BIRTH = u'./li[contains(., "生日：")]/span[last()]/text()'
XPATH_BI_INTRO = u'./li[contains(., "简介：")]/span[last()]/text()'
XPATH_BI_CREATED_AT = u'./li[contains(., "注册时间：")]/span[last()]/text()'
XPATH_BI_EMAIL = u'./li[contains(., "邮箱：")]/span[last()]/text()'
XPATH_BI_QQ = u'./li[contains(., "QQ：")]/span[last()]/text()'
XPATH_BI_HIGH_SCHOOL = u'./li[contains(., "高中：")]/span[last()]/text()'
XPATH_BI_TAG = u'./li[contains(., "标签：")]/span[last()]/a/text()'

XPATH_BI_LEVEL = '//p[@class="level_info"]/span[1]/span/text()'
XPATH_BI_EXP = '//p[@class="level_info"]/span[2]/span/text()'
