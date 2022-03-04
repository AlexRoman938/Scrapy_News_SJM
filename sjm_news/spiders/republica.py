from tkinter import E
from urllib.request import Request
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
import time

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

href_republica = []



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
                'fields': ['link_republica', 'title_republica', 'subtitle_republica', 'fecha'],
                'overwrite': True
            }
        }
    }

    def __init__(self):

        #Block all cookies
        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.cookie.cookieBehavior", 2)
        
        self.driver = webdriver.Firefox(firefox_binary= binary,
                         executable_path= 'C:\\Users\\sasuk\gecko\\geckodriver.exe',
                         firefox_profile=fp)
        

        
    def parse(self, response):
        
        self.driver.get('https://larepublica.pe/tag/san-juan-de-miraflores/')
        time.sleep(2)

        count = 1
        while count == 1:

            

            try:
                
                """button_cookie = self.driver.find_element(By.CSS_SELECTOR, 'button. css-47sehv')
                button_cookie.click()
                time.sleep(2)"""
            
                button_down = self.driver.find_element(By.CSS_SELECTOR, 'button#btnLoadMore')
                button_down.click()
                time.sleep(2)
                button_down.click() 
                time.sleep(2)
                button_down.click()
                time.sleep(2)
                button_down.click()  
                time.sleep(2)
                
                href_republica.extend([link.get_attribute('href') for link in self.driver.find_elements(By.CSS_SELECTOR, 'a.PostSectionListA')])

                count = count + 1        

            except:

                pass
        
        for link in href_republica:

            yield response.follow(link, callback = self.parse_link2, cb_kwargs = {'url' : response.urljoin(link)})


                
    def parse_link2(self, response, **kwargs):

        link_republica = kwargs['url']
        title_republica = self.driver.find_elements(By.XPATH,"//h1/text()").get()
        subtitle_republica = self.driver.find_elements(By.XPATH,'//h2[@class = "DefaultSubtitle"]/text()').get()
        fecha = self.driver.find_elements(By.XPATH,"//div[@class = 'comp-autor-dateTime']/time/text()").get()

        yield{

            'link_republica' : link_republica,
            'title_republica' : title_republica,
            'subtitle_republica' : subtitle_republica,
            'fecha' : fecha

        }

    
