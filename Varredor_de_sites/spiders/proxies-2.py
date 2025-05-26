import scrapy

class ProxiesSpider2(scrapy.Spider):
    name = 'proxies_bot2'
    
    def start_requests(self):
        urls = ["https://free-proxy-list.net/web-proxy.html"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for cards in response.xpath("//table[@class='table table-striped table-bordered']//tbody/tr"):
            yield {
                "Proxy name": cards.xpath("./td[1]/a/text()").get(),
                "Domain": cards.xpath("./td[2]/text()").get(),
                "Country": cards.xpath("./td[3]/text()").get(),
                "Speed": cards.xpath("./td[4]/text()").get(),
                "Popularity": cards.xpath("./td[5]//div/text()").get(),
            }