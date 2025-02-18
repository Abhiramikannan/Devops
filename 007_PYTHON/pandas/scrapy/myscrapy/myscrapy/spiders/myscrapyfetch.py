#created by me
#scrapy crawl abhi -o links.json
import scrapy

class Extracturls(scrapy.Spider):
    name='abhi'
    def start_requests(self):
        urls=['https://www.example.com']
        for url in urls:
            yield scrapy.Request(url=urls, callback=self.parse)
    def parse(self,response):
        links=response.css('a::attr(href)').extract()
        for link in links:
            yield{'links': link}
        