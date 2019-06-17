
import scrapy


class KijijiSpider(scrapy.Spider):
    name = "kijiji"

    def start_requests(self):
        urls = [
            'https://www.kijiji.ca/b-quebec/velo-yuba/k0l9001?dc=true',
            'https://www.kijiji.ca/b-quebec/velo-babboe/k0l9001?dc=true',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ad in response.css('.info-container'):
            yield {
                'title': ad.css('.title>a::text').get().strip(),
                'description': ad.css('.description::text').get().strip(),
                'price': ad.css('.price::text').get().replace(" ", "").replace("$", "").replace(",", ".").strip(),
                'location': ad.css('.location::text').get().strip(),
                'source': 'kijiji'
            }
