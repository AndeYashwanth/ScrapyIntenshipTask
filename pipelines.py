from scrapy import Request
import os
from scrapy.pipelines.files import FilesPipeline
import urllib.parse


class ScrapeTestPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name = urllib.parse.unquote(request.url.split("/")[-1])
        return file_name