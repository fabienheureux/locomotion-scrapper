
import scrapy


class MarkplaatsSpider(scrapy.Spider):
    name = "markplaats"

    def start_requests(self):
        urls = [
            'https://www.marktplaats.nl/l/fietsen-en-brommers/q/bakfiets+babboe/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ad in response.css('.mp-Listing.mp-Listing--list-item '):
            yield {
                'title': ad.css('.mp-Listing-title::text').get().strip(),
                'description': ad.css('.mp-Listing-description.mp-text-paragraph::text').get().strip(),
                'price': ad.css('.mp-Listing-price.mp-text-price-label::text').get().replace(" ", "").replace("€", "").replace(",", ".").strip(),
                'location': ad.css('.mp-Listing-location::text').get().strip(),
                'source': 'markplaats'
            }
