from scrapy_jsonschema.item import JsonSchemaItem


class CrawlLicitatieItem(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "title": "licitatie-object",
        "description": "A licitatie crawl object",
        "type": "object",
        "properties": {
            "notice_number": {"type": "string"},
            "tender_name": {"type": "string"},
            "procedure_status": {
                "enum": [
                    "Published",
                ]
            },
            "contract_type": {
                "enum": [
                    "Services",
                    "Supply",
                    "In desfasurare",
                ]
            },
            "type_of_procurement": {"type": "string"},
            "estimated_value": {"type": "string"},
            "date": {"type": "string", "format": "date-time"},
        },
    }
