from datetime import datetime
import re


DATE_FORMAT = ['%d.%m.%Y', '%Y-%m-%d']
PHONE_PATTERN = r" 7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}"
EMAIL_PATTERN = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

async def get_type(obj: dict):
    for key, value in obj.items():
        for d_format in DATE_FORMAT:
            try:
                datetime.strptime(value, d_format)
                obj[key] = "date"
            except ValueError:
                pass
        if obj[key] == "date":
            continue
        elif re.fullmatch(PHONE_PATTERN, value):
            obj[key] = "phone"
        elif re.fullmatch(EMAIL_PATTERN, value):
            obj[key] = 'email'
        else:
            obj[key] = 'text'
    return obj
