# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import schedule
import scrapy
from scrapy.spiders import SitemapSpider
from ..items import ShopingItem
from scrapy.loader import ItemLoader
from datetime import time,timedelta,datetime
from scrapy_splash import SplashRequest
class ShopingSpider(SitemapSpider):
    name = 'shoping_spider'
    sitemap_urls = ['https://www.myglamm.com/product-sitemap.xml']
    other_urls=['https://www.myglamm.com/']
    sitemap_rules = [
        ('https://www.myglamm.com/product/', 'parse_product')  # Use parse_product for product pages
    ]
    

    def start_requests(self):
        requests = list(super(ShopingSpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        for request in requests:
        # Check if it's a Scrapy Request or a URL string
            if isinstance(request, scrapy.Request):
                yield request
            elif isinstance(request, str):  # If it's a URL string
                yield SplashRequest(request, callback=self.parse_product, args={'wait': 10})
    def parse_other(self, response):
        # Define how you want to process the response for URLs in `self.other_urls`
        pass
    def parse_product(self, response):
        shoping_data=ShopingItem()
            
        shoping_data["Title"]= response.css("h1.font-bold::text").get()
        rating=response.css("span.font-bold::text").get()
        if rating is None:
            rating=0


        shoping_data["Rating"]= rating
        votes=response.xpath('//*[@id="__next"]/div/div[1]/main/section/div[2]/div/div[1]/span[2]/text()').get()
        if votes is None:
            votes=0
        shoping_data["Votes"]=votes
        shoping_data["Disc_Price"]= response.css('span.text-2xl::text').get()
        mark_price=response.xpath('//*[@id="__next"]/div/div[1]/main/section/div[2]/div/div[2]/del/text()').get()
        if mark_price is None:
            mark_price=response.css('span.text-2xl::text').get()
        
        shoping_data["Mark_price"]=mark_price
        prod_shades=response.xpath('//*[@id="__next"]/div/div[1]/main/section/div[2]/div/section[1]/a/img/@alt').getall()
        if len(prod_shades)==0:
            prod_shades=['No shades Available']

        shoping_data["Prod_varites"]=prod_shades
        prod_shades_img=response.xpath('//*[@id="__next"]/div/div[1]/main/section/div[2]/div/section[1]/a/img/@src').getall()
        
        
    

        shoping_data["Prod_varites_img"]= prod_shades_img
        desc=response.xpath('//*[@id="__next"]/div/div[1]/main/section/div[2]/div/section[2]/div/p/span/text()').getall()
        if len(desc)==0:
            desc=['No product Description is found']
        shoping_data["Description"]=desc
        shoping_data["Categoary"]=response.css('a::text')[3].get()
        shoping_data["Sub_Categoary"]=response.css('a::text')[4].get()
        shoping_data["Prod_Availbility"]=response.css('button::text')[1].get()
        shoping_data['system_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield shoping_data
    
