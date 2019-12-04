# -*- coding: utf-8 -*-
import scrapy


class Act1Spider(scrapy.Spider):
    name = 'act1'
    allowed_domains = ['goodreads.com']
    start_urls = ['http://goodreads.com/quotes/']

    def parse(self, response):
        for quotes in response.css('div.quote'):
            item={
                'quote':quotes.css('div.quoteText::text').extract_first(),
                'author':quotes.css('span.authorOrTitle::text').extract_first(),
                'tags':quotes.css('div.greyText.smallText.left>a::text').extract()
                }
        yield item
        nextpage=response.css('div>a.next_page::attr(href)').extract_first()
        if(nextpage):
            next=response.urljoin(nextpage)
            yield scrapy.Request(url=next,callback=self.parse)
