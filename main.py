import scrapy
import urllib.parse

class Main(scrapy.Spider):
    name = 'main'
    start_urls = [
        'https://www.privacy.gov.ph/memorandum-circulars/'
        'https://www.privacy.gov.ph/advisories/',
        'https://www.privacy.gov.ph/advisory-opinions/'
    ]

    def parse(self, response):
        for aTag in response.xpath("//section[@class='news_content']//div[@class='col-10 text-left'][1]//a"):
            relative_url = aTag.xpath("@href").extract()[0]
            absolute_url = response.urljoin(relative_url)
            title = aTag.xpath("text()").extract()[0].replace('\n', ' ')
            file_name = urllib.parse.unquote(absolute_url.split("/")[-1])

            # If the link is a pdf download it else go 1 level deep and execute second_level() method
            if '.pdf' not in absolute_url:
                yield scrapy.Request(absolute_url, dont_filter=True, meta={'title': title},
                                     callback=self.second_level)
            else:
                yield {'title': title, 'filename': file_name, 'file_urls': [absolute_url]}


    def second_level(self, response):
        relative_url = response.xpath("//table[1]/tbody/tr[1]/td[3]//a/@href").extract()[0]
        absolute_url = response.urljoin(relative_url)
        file_name = urllib.parse.unquote(absolute_url.split("/")[-1])
        date = ''.join(response.xpath("//table[1]/tbody/tr[2]/td[3]//text()").extract()).strip()

        # this title is extracted from 2nd page level.
        title = ''.join(response.xpath("//section[@class='news_title']//text()").extract()).strip()

        yield {'title': title, 'filename': file_name, 'date': date, 'file_urls': [absolute_url]}