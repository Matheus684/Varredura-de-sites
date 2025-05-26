import scrapy
from scrapy.loader import ItemLoader
from Varredor_de_sites.items import GoodReads_item

class GoodReadsSpider(scrapy.Spider):
    name = 'goodreads_bot'
    
    def start_requests(self):
        for c in range(1,101):
            url = f"https://www.goodreads.com/quotes?page={c}"
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for cards in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=GoodReads_item(), selector=cards, response=response)
            loader.add_xpath('texto', ".//div[@class='quoteText']/text()[1]")
            loader.add_xpath('autor', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class='greyText smallText left']/a/text()")
            loader.add_xpath('curtidas', ".//a[@class='smallText']/text()")
            yield loader.load_item()
            