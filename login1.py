# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest


class Login1Spider(Spider):
    name = 'login1'
    start_urls = ('http://quotes.toscrape.com/login',)

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'foobar',
                                                   'username': 'foobar'},
                                         callback=self.scrape_pages)

    def scrape_pages(self, response):
        quotes=response.css('span.text::text').extract()
        author=response.css('small.author::text').extract()
        tags=response.css('a.tag::text').extract()
        
        for quote in zip(quotes,author,tags):
            item={
                'Quote_Content':quote[0],
                'Author':quote[1],
                'Tags':quote[2]
            }
            yield item
        
