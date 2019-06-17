crawl:
	@echo "!!!!!!!!!!!!! Scrapping kijiji first !!!!!!!!!!!!!!"
	@scrapy crawl kijiji -o ../output/kijiji.csv -t csv
	@echo "!!!!!!!!!!!!! Now let's scrap Leboncoin !!!!!!!!!!!!!!"
	@scrapy crawl leboncoin -o ../output/leboncoin.csv -t csv
	@echo "!!!!!!!!!!!!! Now let's scrap Markplaats !!!!!!!!!!!!!!"
	@scrapy crawl markplaats -o ../output/markplaats.csv -t csv

