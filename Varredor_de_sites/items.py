# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join

def retirar_caracteres_especiais(valor):
    return valor.replace(u"\n",'')
def retirar_espacos_brancos(valor):
    return valor.strip()

class BibliotecaVirtual(scrapy.Item):
    titulo = scrapy.Field(
        input_processor=MapCompose(retirar_caracteres_especiais, retirar_espacos_brancos),
        outpu_processor=TakeFirst()
    )
    escritor = scrapy.Field(        
        input_processor=MapCompose(retirar_caracteres_especiais, retirar_espacos_brancos),
        outpu_processor=TakeFirst()
        )
    ano_publicado = scrapy.Field(
        input_processor=MapCompose(retirar_caracteres_especiais, retirar_espacos_brancos),
        outpu_processor=TakeFirst()
    )
    preco = scrapy.Field(
        input_processor=MapCompose(retirar_caracteres_especiais, retirar_espacos_brancos),
        outpu_processor=TakeFirst()
    )

class Quotes_item(scrapy.Item):
    frase = scrapy.Field()
    autor = scrapy.Field()
    tags = scrapy.Field()

class GoodReads_item(scrapy.Item):
    texto = scrapy.Field()
    autor = scrapy.Field()
    tags = scrapy.Field()
    curtidas = scrapy.Field()

class Proxies_item(scrapy.Item):
    Endereco_IP = scrapy.Field()
    Porta = scrapy.Field()
    Codigo = scrapy.Field()
    Pais = scrapy.Field()
    Anonimato = scrapy.Field()
    Google = scrapy.Field()
    Https = scrapy.Field()
    Ultima_verificacao = scrapy.Field()