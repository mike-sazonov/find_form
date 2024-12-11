from datetime import datetime
import re

# patterns:
DATE_FORMATS = ['%d.%m.%Y', '%Y-%m-%d']
PHONE_PATTERN = r"\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}"
EMAIL_PATTERN = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

async def validate_fields(form_obj: dict) -> dict:
    """
    Принимает из конечной точки /get_form
    словарь с именами и данными формы,
    валидирует поля и возвращает словарь с именами
    и типами полей
    """
    for key, value in form_obj.items():
        for d_format in DATE_FORMATS:
            try:
                datetime.strptime(value, d_format)
                form_obj[key] = "date"
            except ValueError:
                pass
            except TypeError:
                return {"message": "values must be a string!"}
        if form_obj[key] == "date":
            continue
        elif re.fullmatch(PHONE_PATTERN, value):
            form_obj[key] = "phone"
        elif re.fullmatch(EMAIL_PATTERN, value):
            form_obj[key] = 'email'
        else:
            form_obj[key] = 'text'
    return form_obj
