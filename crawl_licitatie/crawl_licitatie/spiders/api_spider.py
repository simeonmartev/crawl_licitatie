import scrapy
import json

from ..items import CrawlLicitatieNotice


class APISpider(scrapy.Spider):
    name = "api_spider"

    def start_requests(self):
        url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en",
            "Accept-Encoding": "gzip, deflate",
            "Culture": "en-US",
            "Authorization": "Bearer null",
            "RefreshToken": "null",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "http://www.e-licitatie.ro",
            "Connection": "keep-alive",
            "Referer": "http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1",
        }
        body = {
            "sysNoticeTypeIds": [2],
            "sortProperties": [],
            "pageSize": 5,
            "hasUnansweredQuestions": "false",
            "startPublicationDate": "2022-03-31T12:39:11.929Z",
            "startTenderReceiptDeadline": "2022-04-30T12:39:11.930Z",
            "sysProcedureStateId": 2,
            "pageIndex": 0,
        }

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            method="POST",
            headers=headers,
            body=json.dumps(body),
            encoding="utf-8",
        )

    def parse(self, response):
        notices = json.loads(response.body)
        for notice in notices["items"]:
            item = CrawlLicitatieNotice(
                notice_id=notice["noticeId"],
                notice_number=notice["noticeNo"],
                tender_name=notice["contractTitle"],
                procedure_status=notice["sysNoticeState"]["text"],
                contract_type=notice["sysProcedureState"]["text"],
                type_of_procurement=notice["sysAcquisitionContractType"][
                    "text"
                ],
                estimated_value=notice["estimatedValueExport"].replace(
                    " RON", ""
                ),
                datetime=notice["noticeStateDate"],
            )
            yield item
