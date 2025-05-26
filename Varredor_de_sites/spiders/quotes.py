import scrapy
from scrapy.loader import ItemLoader
from Varredor_de_sites.items import Quotes_item

class QuotesSpider(scrapy.Spider):
    name = 'quotes_bot'
    
    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for cards in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=Quotes_item() ,selector=cards, response=response)
            loader.add_xpath('frase', ".//span[@class='text']/text()")
            loader.add_xpath('autor', ".//small[@class='author']/text()")
            loader.add_xpath('tags', ".//a[@class='tag']/text()")
            yield loader.load_item()
            
        try:
            link_proxima_pagina = response.xpath("//li[@class='next']/a/@href").get()
            if link_proxima_pagina is not None:
                link_proxima_pagina = response.urljoin(link_proxima_pagina)
                yield scrapy.Request(url = link_proxima_pagina, callback = self.parse)
        except:
            print('Chegamos na ultima pagina')

# precisa desativar certa configuraçao do settings.py
