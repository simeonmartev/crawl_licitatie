from dateutil import parser
from ...model.notices import NoticeModel


class CrawlLicitatiePipeline:
    def process_item(self, item, spider) -> NoticeModel:
        notice = item
        notice["datetime"] = parser.parser(item["datetime"])
        notice = NoticeModel.create(**notice)
        return notice
