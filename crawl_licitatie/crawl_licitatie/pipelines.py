from dateutil import parser
from model.notices import NoticeModel
from pprint import pprint


class CrawlLicitatiePipeline:
    def process_item(self, item, spider) -> NoticeModel:
        # __import__("ipdb").set_trace()
        notice = NoticeModel.create(**item)
        pprint(notice)
        return notice
