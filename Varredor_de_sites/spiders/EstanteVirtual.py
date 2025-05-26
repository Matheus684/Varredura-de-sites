import scrapy
from scrapy.loader import ItemLoader
from Varredor_de_sites.items import BibliotecaVirtual

# CamelCase
class BibliotecaVirtualSpider(scrapy.Spider):
    # identidade
    name = 'dados_livros'
    # request
    def start_requests(self):
        for c in range(1,3):
            url = f"https://www.estantevirtual.com.br/lst/mais-vendidos?page={c}"
            yield scrapy.Request(url=url, callback=self.parse)
    # resposta
    def parse(self, response):
        for cards in response.xpath("//div[@class='product-item product-list__item']"):
            loader = ItemLoader(item=BibliotecaVirtual() ,selector=cards, response=response)
            loader.add_xpath('titulo', ".//div[@class='product-item__info']//h2/text()")
            loader.add_xpath('escritor', ".//div[@class='product-item__info']/p[1]/text()")
            loader.add_xpath('ano_publicado', ".//div[@class='product-item__info']/p[2]/text()")
            loader.add_xpath('preco', ".//div[@class='product-item__info']//p[@class='product-item__text']/span[2]/text()")
            yield loader.load_item()
