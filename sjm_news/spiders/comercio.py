from gc import callbacks
import scrapy

"""
What do I want? :

DIARIO EL COMERCIO

fecha de la noticia -> Con una condición de que solo extraer las que son del 2022
títulos de cada artículo

Titulo del artículo : response.xpath('//h1/text()').get()

Luego entrar al artículo

Href articulo : response.css('.story-item__title ::attr(href)').getall()

Sacar el subtítulo: response.xpath('//h2/text()').get()

fecha : response.css('.story-contents__time ::text').get()

Recorrer las páginas : response.css('.pagination__right ::attr(href)').get()


Los artículos que dicen null es porque su estructura es muy diferente a lo de las otras noticias.

"""


class SJMSpider(scrapy.Spider):

    name = "sjm_comercio"

    start_urls = [

          'https://elcomercio.pe/noticias/san-juan-de-miraflores/',

    ]

    custom_settings = {

        'FEEDS': {
            'sjm_news_comercio.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['link_comercio', 'title_comercio', 'subtitle_comercio', 'fecha'],
                'overwrite': True
            }
        }
    }



    def parse(self, response):

        href_comercio = response.css('.story-item__title ::attr(href)').getall()

        for href in href_comercio:

            yield response.follow(href, callback = self.parse_link,
                                                cb_kwargs = {'url_comercio': response.urljoin(href)})
    
        
        next_page_button_link =  response.css('.pagination__right ::attr(href)').get() #sacamos el href

        try:

            if next_page_button_link:

                yield response.follow(next_page_button_link, callback = self.parse)
        
        except:

            pass

    def parse_link(self, response, **kwargs):
        
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

        


