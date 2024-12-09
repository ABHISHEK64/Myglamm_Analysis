# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
class ShopingPipeline:
    def open_spider(self, spider):
        self.file = open('items.csv', 'a', newline='',encoding='utf-8')  # Open in append mode
        self.writer = csv.writer(self.file)
        # Only write the header iteif the file is empty
        self.file.seek(0, 2)  # Move to the end of the file
        if self.file.tell() == 0:
            self.writer.writerow(['Title', 'Rating', 'Votes','Disc_Price','Mark_price','Prod_varites','Description','Categoary','Sub_Categoary','Prod_Availbility','system_time','Prod_varites_img'])
    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        self.writer.writerow([item['Title'], item['Rating'], item['Votes'],item['Disc_Price'],item['Mark_price'],item['Prod_varites'],item['Description'],item['Categoary'],item['Sub_Categoary'],item['Prod_Availbility'],item['system_time'],item['Prod_varites_img']])

        return item
