import json


def safe_json_serialize_deserialize(data: any, **kwargs) -> dict:
    """
    Utility function that safely serializes unserializable fields in
    'data' as str and returns back the deserialized version

    Typically useful for serializing datetime.datetime or datetime.date
    Properly handle values if particular values for a key look incorrect
    """
    json_string = json.dumps(data, default=str, **kwargs)
    return json.loads(json_string)

def handle_and_filter_page(page_of_records: list, handler: callable) -> list:
    valid_records = []
    for record in page_of_records:
        data = handler(record)
        if data is not None:
            valid_records.append(data)

    return valid_records

def safe_get(obj, default_value, *keys):
    for key in keys:
        try:
            obj = obj[key]
        except:
            return default_value
    return obj
