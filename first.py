import scrapy
import urllib.parse

class First(scrapy.Spider):
    name = 'first'

    start_urls = ['https://www.privacy.gov.ph/data-privacy-act-primer/']

    def parse(self, response):
        n = len(response.xpath('//div[@class="row"]/div'))
        for i in range(1, n + 1):
            title = ''.join(response.xpath(f'//section/div[@class="row"]/div[{i}]//h4/text()').extract()).strip()
            relative_url = response.xpath(f"//section/div[@class='row']/div[{i}]//a[contains(@href, '.pdf')]/@href").extract()[0]
            absolute_url = response.urljoin(relative_url)
            filename = urllib.parse.unquote(absolute_url.split("/")[-1])

            yield {'title': title, 'filename': filename, 'file_urls': [absolute_url]}
