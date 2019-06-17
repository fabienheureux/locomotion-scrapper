
import scrapy


class LeboncoinSpider(scrapy.Spider):
    name = "leboncoin"

    def start_requests(self):
        urls = [
            'https://www.leboncoin.fr/recherche/?text=Velo%20babboe',
            'https://www.leboncoin.fr/recherche/?text=Velo%20yuba',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ad in response.css('li[data-qa-id="aditem_container"]'):
            yield {
                'title': ad.css('span[data-qa-id="aditem_title"]::text').get().strip(),
                'description': '',
                'price': ad.css('div[data-qa-id="aditem_price"] span span[itemprop="priceCurrency"]::text').get().replace(" ", "").replace("€", "").strip(),
                'location': ad.css('p[data-qa-id="aditem_location"]::text').get().strip(),
                'source': 'leboncoin',
            }
