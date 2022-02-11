import scrapy

"""
What do I want?  Quiero :

DIARIO EL COMERCIO

fecha de la noticia -> Con una condición de que solo extraer las que son del 2022
títulos de cada artículo

Titulo del artículo : response.xpath('//h1/text()').get()

Luego entrar al artículo

Href articulo : response.css('.story-item__title ::attr(href)').getall()


Sacar el subtítulo: response.xpath('//h2/text()').get()


Recorrer las páginas : response.css('.pagination__page ::attr(href)')[:1].get()



DIARIO LA REPÚBLICA

Título de artículo : response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/text()').getall()

Href del artículo : response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/@href').getall()

Luego entrar al artículo

Sacar el parrafo de subtitulo : response.xpath('//h2[@class = "DefaultSubtitle"]/text()').get()

Posiblemente hacer el ver más de abajo



"""


class SJMSpider(scrapy.Spider):

    name = "sjm_scr"

    start_urls = [

          'https://elcomercio.pe/noticias/san-juan-de-miraflores/',

          #'https://larepublica.pe/tag/san-juan-de-miraflores/'

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

        href_comercio = response.css('.story-item__title ::attr(href)').getall()

        for href in href_comercio:

            yield response.follow(href, callback = self.parse_link,
                                                cb_kwargs = {'url_comercio': response.urljoin(href)})
    

    def parse_link(self, response, **kwargs):
        
        link_comercio = kwargs['url_comercio']
        title_comercio = response.xpath('//h1/text()').get()
        subtitle_comercio = response.xpath('//h2/text()').get()

        yield{

            'link_comercio' : link_comercio,
            'title_comercio' : title_comercio,
            'subtitle_comercio' : subtitle_comercio
        }

