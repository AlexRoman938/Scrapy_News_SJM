import scrapy

"""
What do I want? :

DIARIO LA REPÚBLICA

Título de artículo : response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/text()').getall()

Href del artículo : response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/@href').getall()

Luego entrar al artículo

Sacar el parrafo de subtitulo : response.xpath('//h2[@class = "DefaultSubtitle"]/text()').get()

Posiblemente hacer el ver más de abajo

"""

class SJMSpider(scrapy.Spider):

    name = "sjm_republica"

    start_urls = [
          'https://larepublica.pe/tag/san-juan-de-miraflores/'

    ]

    custom_settings = {

        'FEEDS': {
            'sjm_news_comercio.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['link_comercio', 'title_comercio', 'subtitle_comercio'],
                'overwrite': True
            }
        }
    }



    def parse(self, response):

        pass
    

    def parse_link(self, response, **kwargs):
        
        pass
