import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
from logentriesadapter import LogentriesAdapter
logger = logging.getLogger(__name__)

class LogentriesExtension(object):

    def __init__(self, token):
        self.token = token
        from logentries import LogentriesHandler
        import logging
        logging.info('Logentries activated with toker {}'.format(token))
        logging.root.addHandler(LogentriesHandler(token))


    @classmethod
    def from_crawler(cls, crawler):
        # first check if the extension should be enabled and raise
        # NotConfigured otherwise
        token = crawler.settings.get('LOGENTRIES_TOKEN')
        if not token:
            raise NotConfigured


        # instantiate the extension object
        ext = cls(token)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)


        # return the extension object
        return ext

    def spider_opened(self, spider):
        # Replace spider logger by LoggerAdapter giving more context if scrapy-job-parameter-extension is activated on Scrapinghub
        if spider.spider_id is not None:
            spider.logger = LogentriesAdapter(
                logger=spider.logger,
                extra={'spider_name': spider.name,
                       'spider_id': spider.spider_id,
                       'job_id': spider.job_id,
                       }
            )
