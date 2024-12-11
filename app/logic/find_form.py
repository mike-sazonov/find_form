from typing import Union

from app.db.db import db

async def get_form_name_or_none(form_obj: dict) -> Union[str, None]:
    """
    Принимает словарь с типизированными полями формы.
    В случае совпадения с шаблоном в БД, возвращает имя шаблона.
    В ином случае возвращает None.
    """
    all_forms = db.all()
    checking_form = set((k, v) for k, v in form_obj.items())
    for form in all_forms:
        if "name" in form.keys():
            name = form.pop("name")
            form_set = set((k, v) for k, v in form.items())
            if form_set and form_set.issubset(checking_form):
                return name
        else:
            continue
    return None

