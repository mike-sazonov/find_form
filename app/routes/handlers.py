from typing import Union

from fastapi import APIRouter, Request, Body

from app.logic.validation import validate_fields
from app.logic.find_form import get_form_name_or_none

router = APIRouter()


@router.post("/get_form")
async def get_form(form: dict = Body()) -> Union[dict, str]:
    validate_form = await validate_fields(form)
    form_name = await get_form_name_or_none(validate_form)
    return (validate_form, form_name)[bool(form_name)]
