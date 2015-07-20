import logging

class LogentriesAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):

        msg = "[spider={spider_name} spider_id={spider_id} job_id={job_id}]".format(self.extra)
        return msg, kwargs