from fastapi import APIRouter, Request
from fastapi.params import Depends

router = APIRouter()


@router.post("/get_form")
async def get_form(form: Request):
    return form.query_params