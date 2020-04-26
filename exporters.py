from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter


class Utf8JsonItemExporter(JsonItemExporter):

    def __init__(self, file, **kwargs):
        super(Utf8JsonItemExporter, self).__init__(
            file, ensure_ascii=False, **kwargs)