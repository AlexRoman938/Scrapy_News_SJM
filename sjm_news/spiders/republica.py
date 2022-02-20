import scrapy
from helium import *

"""
What do I want? :

DIARIO LA REPÚBLICA



Href del artículo : response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/@href').getall()

Luego entrar al artículo

Título de artículo : response.xpath("//h1/text()").get()

Sacar el parrafo de subtitulo : response.xpath('//h2[@class = "DefaultSubtitle"]/text()').get()

fecha : response.xpath("//div[@class = 'comp-autor-dateTime']/time/text()").get()

Posiblemente hacer el ver más de abajo

"""

class SJMSpider(scrapy.Spider):

    name = "sjm_republica"

    start_urls = [

          'https://larepublica.pe/tag/san-juan-de-miraflores/'

    ]

    custom_settings = {

        'FEEDS': {
            'sjm_news_republica.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['link_republica', 'title_republica', 'subtitle_republica'],
                'overwrite': True
            }
        }
    }



    def parse(self, response):
        
        start_firefox('https://larepublica.pe/tag/san-juan-de-miraflores/')

        

        href_republica = response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/@href').getall()

 
               

    """def parse_link(self, response, **kwargs):
        
        link_comercio = kwargs['url_comercio']
        title_comercio = response.xpath('//h1/text()').get()
        subtitle_comercio = response.xpath('//h2/text()').get()
        fecha = response.css('.story-contents__time ::text').get()

        yield{

            'link_comercio' : link_comercio,
            'title_comercio' : title_comercio,
            'subtitle_comercio' : subtitle_comercio,
            'fecha' : fecha
        }
"""

    
