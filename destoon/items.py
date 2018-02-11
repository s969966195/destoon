	# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #----------商品----------
    catid=scrapy.Field()#分类id
    title=scrapy.Field()#商品标题
    introduce=scrapy.Field()#商品简介
    thumb=scrapy.Field()#主图
    username=scrapy.Field()#用户名 商品url的前缀
    truename=scrapy.Field()#真实姓名 与用户名一直
    company=scrapy.Field()#公司名
    telephone=scrapy.Field()#电话
    address=scrapy.Field()#地址
    editor=scrapy.Field()#和用户名一致
    category_fromurl=scrapy.Field()#当前分类的url
    product_url=scrapy.Field()#当前商品的url
    product_url_md5=scrapy.Field()#当前商品的URL MD5加密
    edittime=scrapy.Field()
    addtime=scrapy.Field()
    editdate=scrapy.Field()
    adddate=scrapy.Field()
    link_url=scrapy.Field()

class SellInfoItem(scrapy.Item):
    #---------商品信息----------
    item_id=scrapy.Field()#商品Id 插入商品后返回的主键
    content=scrapy.Field()#商品详情

class MemberItem(scrapy.Item):
    username=scrapy.Field()
    passport=scrapy.Field()
    password=scrapy.Field()
    passalt=scrapy.Field()
    payword=scrapy.Field()
    truename=scrapy.Field()

class CompanyItem(scrapy.Item):
    username=scrapy.Field()#商品url的前缀 用户名
    groupid=scrapy.Field()
    company=scrapy.Field()
    __type=scrapy.Field()
    regunit=scrapy.Field()
    regyear=scrapy.Field()
    business=scrapy.Field()
    telephone=scrapy.Field()
    fax=scrapy.Field()
    address=scrapy.Field()
    postcode=scrapy.Field()
    thumb=scrapy.Field()
    introduce=scrapy.Field()
    linkurl=scrapy.Field()

class CompanyInfoItem(scrapy.Item):
    userid=scrapy.Field()
    content=scrapy.Field()
