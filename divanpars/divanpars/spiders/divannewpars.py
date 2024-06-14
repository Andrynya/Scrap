import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lampy = response.css('div._Ud0k')

        for lamp in lampy:
            yield {
                'name' : lamp.css('div.lsooF span::text').get(),
                'price' : lamp.css('div.pY3d2 span::text').get(),
                'url' : lamp.css('a').attrib['href']
            }
