import unittest

from scrapy.conf import settings
from scrapy.exceptions import NotConfigured

from scrapylogentries.extension import LogentriesExtension


settings.overrides['LOGENTRIES_TOKEN'] = ''


class TestLogentriesExtension(unittest.TestCase):

    def setUp(self):
        self.extension = LogentriesExtension()

    def test_unconfigured_init(self):
        with self.assertRaises(NotConfigured):
            self.extension = LogentriesExtension(settings={})

