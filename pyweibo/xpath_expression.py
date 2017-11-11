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
XPATH_BI_COUNTER = '//table[@class="tb_counter"]/tbody/tr'
XPATH_BI_FOLLOW = './td[1]/a/strong/text()'
XPATH_BI_FANS = './td[2]/a/strong/text()'
XPATH_BI_WEIBO = './td[3]/a/strong/text()'

XPATH_BI_CONTAINER = u'//div[@class="PCD_text_b PCD_text_b2" and contains(., "基本信息")]/div[2]/div/ul'
XPATH_BASIC_INFO = dict(
    NICKNAME=u'./li[contains(., "昵称：")]/span[last()]/text()',
    ADDRESS=u'./li[contains(., "所在地：")]/span[last()]/text()',
    SEX=u'./li[contains(., "性别：")]/span[last()]/text()',
    BIRTH=u'./li[contains(., "生日：")]/span[last()]/text()',
    INTRO=u'./li[contains(., "简介：")]/span[last()]/text()',
    CREATED_AT=u'./li[contains(., "注册时间：")]/span[last()]/text()',
    SEXUAL_ORIENTATION=u'./li[contains(., "性取向：")]/span[last()]/text()',
    EMOTIONAL_STATE=u'./li[contains(., "感情状态：")]/span[last()]/text()',
    BLOOD_TYPE=u'./li[contains(., "血型：")]/span[last()]/text()',
    BLOG=u'./li[contains(., "博客：")]/a/text()'
)
XPATH_BI_DOMAIN = u'./li[contains(., "个性域名：")]/span[last()]/a/text()'
XPATH_CI_CONTAINER = u'//div[@class="PCD_text_b PCD_text_b2" and contains(., "联系信息")]/div[2]/div/ul'
XPATH_CONTACT_INFO = dict(
    EMAIL=u'./li[contains(., "邮箱：")]/span[last()]/text()',
    QQ=u'./li[contains(., "QQ：")]/span[last()]/text()',
    MSN=u'./li[contains(., "MSN：")]/span[last()]/text()'
)
XPATH_WI_CONTAINER = u'//div[@class="PCD_text_b PCD_text_b2" and contains(., "工作信息")]/div[2]/div/ul'
XPATH_COMPANY = u'//li[contains(., "公司：")]/span'
XPATH_EI_CONTAINER = u'//div[@class="PCD_text_b PCD_text_b2" and contains(., "教育信息")]/div[2]/div/ul'
XPATH_EDUCATION_INFO = dict(
    HIGH_SCHOOL=u'string(./li[contains(., "高中：")]/span[last()]/.)',
    UNIVERSITY=u'string(./li[contains(., "大学：")]/span[last()]/.)',
    VOCATIONAL_SCHOOL=u'string(./li[contains(., "职高：")]/span[last()]/.)',
    TECHNICAL_SECONDARY_SCHOOL=u'string(./li[contains(., "中专技校：")]/span[last()]/.)',
    JUNIOR_MIDDLE_SCHOOL=u'string(./li[contains(., "初中：")]/span[last()]/.)',
    PRIMARY_SCHOOL=u'string(./li[contains(., "小学：")]/span[last()]/.)',
    OVERSEAS=u'string(./li[contains(., "海外：")]/span[last()]/.)'
)
XPATH_TI_CONTAINER = u'//div[@class="PCD_text_b PCD_text_b2" and contains(., "标签信息")]/div[2]/div/ul'
XPATH_TI_TAG = u'./li[contains(., "标签：")]/span[last()]/a/text()'

XPATH_BI_LEVEL = '//p[@class="level_info"]/span[1]/span/text()'
XPATH_BI_EXP = '//p[@class="level_info"]/span[2]/span/text()'

XPATH_BAIKE_INFO = u'//span[@class="item_text W_fl" and contains(., "百度人物资料")]/a/@href'
