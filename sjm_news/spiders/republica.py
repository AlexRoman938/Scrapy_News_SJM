from tkinter import E
from urllib.request import Request
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

"""
What do I want? :

DIARIO LA REPÚBLICA



Href del artículo : response.css('.PostSectionListA ::attr(href)').getall()

Luego entrar al artículo

Título de artículo : response.xpath("//h1/text()").get()

Sacar el parrafo de subtitulo : response.xpath('//h2[@class = "DefaultSubtitle"]/text()').get()

fecha : response.xpath("//div[@class = 'comp-autor-dateTime']/time/text()").get()

Posiblemente hacer el ver más de abajo

"""

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

class SJMSpider(scrapy.Spider):

    name = "sjm_republica"

    allowed_domains = ['www.larepublica.pe']

    start_urls = [

          'https://larepublica.pe/tag/san-juan-de-miraflores/'

    ]

    custom_settings = {

        'FEEDS': {
            'sjm_news_republica.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['link_republica',],
                'overwrite': True
            }
        }
    }

    def __init__(self):
        
        self.driver = webdriver.Firefox(firefox_binary= binary,
                         executable_path= 'C:\\Users\\sasuk\gecko\\geckodriver.exe')

        
    def parse(self, response):
        
        self.driver.get('https://larepublica.pe/tag/san-juan-de-miraflores/')

        while True:

            button_down = self.driver.find_element(By.CSS_SELECTOR, 'button#btnLoadMore')

            try:


                button_down.click()
                break
                
 

            except:

                break
        
        href_republica = response.css('.PostSectionListA ::attr(href)').getall()

        yield{

             'link_republica' : href_republica

        }

                
        

        
    """def parse2(self, response):

        href_republica = response.xpath('//li[@class = "PostSectionListLI"]/h2[@class = "PostSectionListH3"]/a[@class = "PostSectionListA"]/@href').getall()

        for href in href_republica:

            yield response.follow(href, callback = self.parse_link2,
                                                cb_kwargs = {'url_republica': response.urljoin(href)})"""
    


    """def parse_link2(self, response, **kwargs):

        link_republica = kwargs['url_republica']
        title_republica = response.xpath("//h1/text()").get()
        subtitle_republica = response.xpath('//h2[@class = "DefaultSubtitle"]/text()').get()
        fecha = response.xpath("//div[@class = 'comp-autor-dateTime']/time/text()").get()

        yield{

            'link_republica' : link_republica,
            'title_republica' : title_republica,
            'subtitle_republica' : subtitle_republica,
            'fecha' : fecha

        }"""

    
