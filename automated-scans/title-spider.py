import scrapy

class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["engineeur.com"]
    start_urls = ["http://engineeur.com/"]

    def parse(self, response):
        # Extract the title of the page
        title = response.xpath('//title/text()').extract_first()

        # Extract the URLs of all the pages in the website
        page_links = response.css('a::attr(href)').extract()

        # Filter out external URLs
        internal_page_links = [link for link in page_links if 'engineeur.com' in link]

        # Yield a dictionary containing the title and URLs of all the internal pages
        yield {
            'title': title,
            'internal_pages': internal_page_links
        }
