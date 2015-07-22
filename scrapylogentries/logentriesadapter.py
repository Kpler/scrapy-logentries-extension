import logging

class LogentriesAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):

        msg = "[spider={spider_name} spider_id={spider_id} job_id={job_id}]".format(self.extra)
        return msg, kwargs






class ScrapingHubFilter(logging.Filter):

    def __init__(self, extra):
        self.extra = extra

    def filter(self, record):
        record.project_id = self.extra.get('project_id')
        record.spider_id = self.extra.get('spider_id')
        record.job_id = self.extra.get('job_id')
        return True

