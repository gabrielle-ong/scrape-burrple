import scrapy
from scrapy.http import Request
from tutorial.items import TutorialItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.burpple.com"]
    start_urls = [
    "http://localhost:8000"
    #"http://www.burpple.com/categories/sg"
    ]
    #rules = (Rule(SgmlLinkExtractor(allow=('')), callback='parse_categories',follow=True))
	#rules = (Rule(SgmlLinkExtractor(allow=('')), callback='parse_categories',follow=True))
	

    def parse(self, response):
		for sel in response.xpath('//div[re:test(@class, "categoriesList")]/div/div/ul/li'):
			link = sel.xpath('a/@href').extract()
			url = response.urljoin(link[0])
			yield scrapy.Request(url,  callback = self.parse_categories)
		# yield scrapy.Request("http://www.burpple.com",  callback = self.parse_categories)

    def parse_categories(self, response):
    	with open('test.txt', 'a') as f:
			f.write(str(response.url) + "\n")
    	# for x in range(0, 10):
    	# 	print "HAHSHSDHADHS"
    	#yield

		# links = response.selector.xpath('*')

		# for link in links:
		# 	item = TutorialItem()
		# 	item['title'] = sel.xpath('a/text()').extract()
		# 	item['link'] = sel.xpath('a/@href').extract()
		# 	print item['link']
		# 	yield item
		# sel = Selector(response)
		# models = sel.xpath("//li[@class='class_12']")
		# for model in models:
		# 	item = SiteUtem(response.meta["item"])
		# 	url2 = model.xpath('a/@href')[0].extract()
		# 	item ['model'] = model.xpath("a/text()")[0].extract()
		# 	item ['model_link'] = url2
		# 	yield item
