# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from w3lib.html import remove_tags



class ShopingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Rating=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Votes=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Disc_Price=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Mark_price=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Prod_varites=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Description=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Categoary=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Sub_Categoary=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Prod_Availbility=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    Prod_varites_img=scrapy.Field(input_processor=MapCompose(remove_tags),output_processors=(TakeFirst))
    system_time=scrapy.Field()






    pass
