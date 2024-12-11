from http.client import responses

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_date_phone_email_text():
    response = client.post("/get_form",
                           json={
                               "user_email": "test@test.com",
                               "user_text": "some_text",
                               "order_date": "2024-11-11",
                               "user_phone": "+7 111 222 33 44"
                           })
    assert response.json() == "date, phone, email, text"

def test_phone_email_date():
    response = client.post("/get_form",
                           json={
                               "user_phone": "+7 111 222 33 44",
                               "user_email": "test@test.com",
                               "user_date": "22.11.1997",
                           })
    assert response.json() == "phone_email_and_date"

def test_email_text():
    response = client.post("/get_form",
                           json={
                               "user_email": "abcd@yandex.ru",
                               "user_text": "Hello world!"
                           })
    assert response.json() == "email_and_text"

def test_email_date():
    response = client.post("/get_form",
                           json={
                               "user_date": "18.03.2016",
                               "user_email": "abcd@yandex.ru",
                           })
    assert response.json() == "email_and_date"

def test_phone_text():
    response = client.post("/get_form",
                           json={
                               "user_phone": "+7 953 777 66 55",
                               "user_text": "what's up",
                           })
    assert response.json() == "phone_and_text"

def test_phone_date():
    response = client.post("/get_form",
                           json={
                               "user_phone": "+7 953 777 66 55",
                               "user_date": "2024-12-11",
                           })
    assert response.json() == "phone_and_date"

def test_date():
    response = client.post("/get_form",
                           json={
                               "order_date": "2023-03-17",
                           })
    assert response.json() == "date"

def test_email():
    response = client.post("/get_form",
                           json={
                               "user_email": "mihailsazon@gmail.com",
                           })
    assert response.json() == "email"

def test_random_fields():
    response = client.post("/get_form",
                           json={
                               "rand_email": "test@test.com",
                               "rand_text": "some_text",
                               "rand_date": "2024-11-11",
                               "rand_phone": "+7 111 222 33 44"
                           })
    assert response.json() == {
        "rand_email": "email",
        "rand_text": "text",
        "rand_date": "date",
        "rand_phone": "phone"
    }

def test_wrong_values():
    response = client.post("/get_form",
                           json={
                               "field": 123
                           })
    assert response.json() == {"message": "values must be a string!"}