from scrapy_jsonschema.item import JsonSchemaItem


class CrawlLicitatieNotice(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "title": "licitatie-notice",
        "description": "A licitatie crawl notice",
        "type": "object",
        "properties": {
            "notice_id": {"type": "string"},
            "notice_number": {"type": "string"},
            "tender_name": {"type": "string"},
            "procedure_status": {"type": "string"},
            "contract_type": {"type": "string"},
            "type_of_procurement": {"type": "string"},
            "estimated_value": {"type": "number", "minimum": 0},
            "datetime": {"type": "string", "format": "date-time"},
        },
        "required": [
            "notice_id",
            "notice_number",
            "tender_name",
            "procedure_status",
            "contract_type",
            "type_of_procurement",
            "estimated_value",
            "datetime",
        ],
    }
