import scrapy

class ProxiesSpider(scrapy.Spider):
    name = 'proxies_bot'
    
    def start_requests(self):
        urls = ["https://www.us-proxy.org/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for cards in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                'ip_address': cards.xpath("./td[1]/text()").get(),
                'port': cards.xpath("./td[2]/text()").get(),
                'code': cards.xpath("./td[3]/text()").get(),
                'country': cards.xpath("./td[4]/text()").get(),
                'anonymity': cards.xpath("./td[5]/text()").get(),
                'google': cards.xpath("./td[6]/text()").get(),
                'https': cards.xpath("./td[7]/text()").get(),
                'last_checked': cards.xpath("./td[8]/text()").get(),
            }
