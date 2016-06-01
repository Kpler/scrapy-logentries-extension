# -*- coding: utf-8; -*-
import unittest
from mock import Mock, patch

from scrapy.exceptions import NotConfigured

from scrapylogentries.extension import LogentriesExtension


class TestLogentriesExtension(unittest.TestCase):

    def test_unconfigured_init(self):
        crawler = Mock()
        crawler.settings = {'LOGENTRIES_TOKEN': None, }

        with self.assertRaises(NotConfigured):
            self.extension = LogentriesExtension.from_crawler(crawler)

    @patch('scrapylogentries.extension.LogentriesHandler')
    def test_configured_init(self, handler):
        token = 'azertyuiop123456789'
        crawler = Mock()
        crawler.settings = {'LOGENTRIES_TOKEN': token, }

        extension = LogentriesExtension.from_crawler(crawler)

        handler.assert_called_once_with(token)
        extension.handler


# vim: syntax=python:sws=4:sw=4:et:
