#coding=utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from destoon.items import SellItem,SellInfoItem,CompanyItem
import MySQLdb
import hashlib
import time

class destoonCrawl(Spider):
    name="destoon"
    start_urls=[]
    db=MySQLdb.connect("localhost","root","******","destoon")

    cursor=db.cursor()
    cursor.execute("SELECT fromurl FROM `destoon_category` WHERE `moduleid` = 5 AND `child` = 0")
    data=cursor.fetchall()
    for row in data:
        start_urls.append(row[0])

    def parse(self,response):
        catid=cursor.execute("SELECT catid FROM `destoon_category` WHERE `fromurl`='{0}'".format(response.url))[0]
        sel=Selector(response)
        for sell_url in sel.xpath('//h2[@class="product-name"]/a/@href').extract():
            yield Request(sell_url,callback=self.sell_parse,meta={'catid':catid,'category_fromurl':response.url})
        try:
            next_url=sel.xpath('//div[@class="page-num"]/a[@class="next"]/@href').extract()[0]
            yield Request(next_url,callback=self.parse)
        except:
            pass
    
    def sell_parse(self,response):
        sel=Selector(response)
        item=SellItem()
        item2=SellInfoItem()
        item['catid']=response.meta('catid')
        item['category_fromurl']=response.meta('category_fromurl')
        title=sel.xpath('//h1[@itemprop="name"]/text()').extract()[0]
        item['title']=title
        introduce=''
        for i in sel.xpath('//div[@class="rich-text cf J-ATF"]/text()').extract():
            s+=i.strip()
        item['introduce']=s
        thumb=sel.xpath('//div[@class="pic-list"]/div[@class="item"]/@fsrc').extract()[0]
        item['thumb']=thumb
        username=response.url.split('/')[2].split('.')[0]
        truename=username
        item['username']=username
        item['truename']=truename
        company=sel.xpath('//p[@class="com-name"]/text()').extract()[0]
        item['company']=company
        contact_url=sel.xpath('//li[@name="menubar"]/a[@rel="nofollow"]/@href').extract()[0]
        contact=Request(contact_url,callback=self.contact_parse)
        item['telephone']=contact[0]
        item['address']=contact[1]
        editor=username
        item['editor']=editor
        item['product_url']=response.url
        product_url_md5=hashlib.md5().update(response.url).hexdigest()
        item['product_url_md5']=product_url_md5
        edittime=time.time()
        addtime=edittime
        editdata=time.asctime(time.localtime(time.time()))
        adddata=editdata
        item['edittime']=edittime
        item['addtime']=addtime
        item['editdata']=editdata
        item['adddata']=adddata
        content=[]#商品详情的图片
        for i in sel.xpath('//div[@class="rich-text cf J-ATF"]/img/@data-original').extract():
            content.append(i)
        item2['content']=content
        company_url=sel.xpath('//ul[@id="menuFl"]/li[@name="menubar"]/a/@href').extract()[0]
        yield Request(company_url,callback=self.company_parse,meta={'username':username})

    def contact_parse(self,response):
        sel=Selector(response)
        contact=[]
        telephone=sel.xpath('//div[@class="contact-info cf"]//span[@class="td"]/text()').extract()[-2]
        contact.append(telephone)
        address=sel.xpath('//div[@class="contact-info cf"]//span[@class="com-address"]/text()').extract()[0].split('\n')[0]
        contact.append(address)
        return contact

    def company_parse(self,response):
        sel=Selector(response)
        item=
