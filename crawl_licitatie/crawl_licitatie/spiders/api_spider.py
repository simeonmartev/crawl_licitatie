from pprint import pprint
import scrapy
import json

from ..items import CrawlLicitatieItem


class APISpider(scrapy.Spider):
    name = "api_spider"

    def start_requests(self):
        url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": " uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Culture": "en-US",
            "Authorization": "Bearer null",
            "RefreshToken": "null",
            "HttpSessionID": "D49CB35C-0AA5-4E04-8C83-5FED8946BF4E",
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
        noticeses = json.loads(response.body)
        for notice in noticeses["items"]:
            item = CrawlLicitatieItem(
                notice_number=notice["noticeNo"],
                tender_name=notice["contractTitle"],
                procedure_status=notice["sysNoticeState"]["text"],
                contract_type=notice["sysProcedureState"]["text"],
                type_of_procurement=notice["sysAcquisitionContractType"][
                    "text"
                ],
                estimated_value=notice["estimatedValueExport"],
                date=notice["noticeStateDate"],
            )
            yield item
