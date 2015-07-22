import logging, os
from scrapy import signals
from scrapy.exceptions import NotConfigured
from logentriesadapter import LogentriesAdapter, ScrapingHubFilter
logger = logging.getLogger(__name__)

class LogentriesExtension(object):

    def __init__(self, token):
        self.token = token
        from logentries import LogentriesHandler
        import logging
        root = logging.getLogger()

        handler = LogentriesHandler(token)

        spider_id = os.environ.get('SCRAPY_SPIDER_ID')
        project_id = os.environ.get('SCRAPY_PROJECT_ID')
        job_id = os.environ.get('SCRAPY_JOB_ID')

        formatted = False
        if job_id is not None:
            formatted = True
            filter = ScrapingHubFilter({
                        'project_id': project_id,
                       'spider_id': spider_id,
                       'job_id': job_id,
                       })
            format = "%(name)s - %(levelname)s - [project_id=%(project_id)s spider_id=%(spider_id)s job_id=%(job_id)s] %(message)s"
            formatter = logging.Formatter(format)

            handler.addFilter(filter)
            handler.setFormatter(formatter)

        root.addHandler(handler)
        if formatted:
            logger.info('Logentries activated with token {} and custom SH format'.format(token))
        else:
            logger.info('Logentries activated with token {} and no custom SH format'.format(token))

    @classmethod
    def from_crawler(cls, crawler):
        # first check if the extension should be enabled and raise
        # NotConfigured otherwise
        token = crawler.settings.get('LOGENTRIES_TOKEN')
        if not token:
            raise NotConfigured


        # instantiate the extension object
        ext = cls(token)


        # return the extension object
        return ext


