import logging, os
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

        spider_id =  os.environ.get('SPIDER_ID')
        project_id=  os.environ.get('SPIDER_ID')
        job_id=  os.environ.get('JOB_ID')

        if job_id is not None:
            logging.logger = LogentriesAdapter(
                logger=logging.getLogger(),
                extra={'project_id': project_id,
                       'spider_id': spider_id,
                       'job_id': job_id,
                       }
            )

        # return the extension object
        return ext


