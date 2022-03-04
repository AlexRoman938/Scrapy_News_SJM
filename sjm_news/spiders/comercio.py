import scrapy

"""
What do I want? :

DIARIO EL COMERCIO


Title article : response.xpath('//h1/text()').get()

Href article : response.css('.story-item__title ::attr(href)').getall()

Subtitle article: response.xpath('//h2/text()').get()

date : response.css('.story-contents__time ::text').get()

Loop in all pages : response.css('.pagination__right ::attr(href)').get()


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
                'fields': ['link_comercio', 'title_comercio', 'subtitle_comercio', 'date'],
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
        date = response.css('.story-contents__time ::text').get()

        yield{

            'link_comercio' : link_comercio,
            'title_comercio' : title_comercio,
            'subtitle_comercio' : subtitle_comercio,
            'date' : date
        }

        


