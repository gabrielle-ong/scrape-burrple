import scrapy
from scrapy.http import Request
from tutorial.items import TutorialItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from bs4 import BeautifulSoup

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["www.burpple.com"]
	start_urls = [
	#"http://localhost:8000"
	"http://www.burpple.com/categories/sg"
	]
	base_url = "http://www.burpple.com"

	def parse(self, response):
		soup = BeautifulSoup(response.body, 'html.parser')
		result = soup.select(".categoriesList .clearfix a")
		for record in result:
			url = self.base_url + record['href']	#retrieve the href path and join the base url
			return scrapy.Request(url,  callback = self.parse_categories)

	def parse_categories(self, response):
		#find elements that contains topVenue-details for class
		soup = BeautifulSoup(response.body, 'html.parser')
		details = soup.select(".topVenue-details")
		for detail in details:
			detail_body = detail.select(".topVenue-details-info")
			for link in detail_body:
				found_link = link.find_all('a')[0]['href']
				url = self.base_url + found_link
				return scrapy.Request(url, callback = self.parse_details)

	def parse_details(self, response):
		soup = BeautifulSoup(response.body, 'html.parser')
		address = soup.select(".venueInfo-details-header .venueInfo-details-header-item-header--address")
		address = address[0].find_next_sibling().get_text(" ", strip=True)
		with open('test.txt', 'a') as f:
			f.write(str(address) + "\n")
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

