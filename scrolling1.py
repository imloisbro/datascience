# -*- coding: utf-8 -*-
import json
import scrapy


class Scrolling1Spider(scrapy.Spider):
    name = 'scrolling1'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'Quote': item.get('text'),
                'Author': item.get('author', {}).get('name'),
                'Tags': item.get('tags')
                }
            if data['has_next']:
                next_scrolling_page = data['page'] + 1
                yield scrapy.Request(self.quotes_base_url % next_scrolling_page)
