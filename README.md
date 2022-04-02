# Scrapy_News_SJM

## DESCRIPTION

This project makes a web scraping in [DIARIO EL COMERCIO WEBSITE](https://elcomercio.pe/noticias/san-juan-de-miraflores/) about current San Juan de Miraflores news along the 16 pagination.

![image](https://user-images.githubusercontent.com/85772184/159340882-ae3273a3-c56d-4e7f-8d87-cbbeaeb7819d.png)


I've used [Scrapy](https://en.wikipedia.org/wiki/Scrapy) to do web scraping with XPATH and CSS_SELECTOR.

## INSTALLATION AND RUN THE PROJECT

Use the package manager [pip](https://pypi.org/project/pip/) to install scrapy.

``` pip install scrapy ```

Then

In [CMD](https://en.wikipedia.org/wiki/Cmd.exe), you must to be in your folder location where you would like to make this project and write:

``` scrapy startproject sjm_news ``` 

Finally, if you want to running the project. You must write:

``` scrapy crawl sjm_comercio ```

## HOW TO USE THE PROJECT

In <strong>comercio.py</strong>, we have some observations about the project. 

1.How to change the format (i.e. csv)?

In 37 line,  you will see ```'format' : 'json'``` . Then, you just have to change to csv.

![image](https://user-images.githubusercontent.com/85772184/160526083-b4d55754-7201-4ced-9a4f-848513a6ef60.png)

2.How to change the order of fields?

In 39 line, you will see ```'fields': ['link_comercio', 'title_comercio', 'subtitle_comercio', 'date'],'```. Then, you just have to change the order of them (i.e. ```[ 'title_comercio', 'subtitle_comercio', 'date', 'link_comercio']```)


The result of the project is [here](https://github.com/AlexRoman938/Scrapy_News_SJM/blob/master/sjm_news/sjm_news_comercio.json)

![image](https://user-images.githubusercontent.com/85772184/160527485-ed281149-181d-4e2c-9490-ba4181437d5c.png)

<strong>Observation: There are some news don't have title, subtitle and date. It was cuz some href links have different structures (You will observse that problem when you open those links). </strong>

## FUTURE WORK

Finally, I would like to do an analysis with the news in the future. So, I would use NLP (Natural Language Process) to know which are most words in the news and what is the situation of San Juan de Miraflores.











