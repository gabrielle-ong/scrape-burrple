import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    "http://www.burpple.com/categories/sg",
    ]

    def parse(self, response):
		for sel in response.xpath('//div[re:test(@class, "categoriesList")]/div/div/ul/li'):
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			desc = sel.xpath('text()').extract()
			print title, link, desc