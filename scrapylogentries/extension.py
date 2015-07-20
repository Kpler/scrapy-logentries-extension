import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)

class LogentriesExtension(object):

    def __init__(self, token):
        self.token = token
        from logentries import LogentriesHandler
        import logging

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

        # return the extension object
        return ext