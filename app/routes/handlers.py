from fastapi import APIRouter, Request

from app.logic.parse import get_type

router = APIRouter()


@router.post("/get_form")
async def get_form(form: Request):
    rez = await get_type(dict(form.query_params))
    return rez
