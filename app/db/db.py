from tinydb import TinyDB


db = TinyDB('db.json')


# db.insert_multiple([
#     {},
#     {"name": "Mike"},
#     {"user_email": "email"},
#     {"name": "date, phone, email, text", "order_date": "date", "user_phone": "phone", "user_email": "email", "user_text": "text"},
#     {"name": "phone_email_and_date", "user_phone": "phone", "user_email": "email", "user_date": "date"},
#     {"name": "email_and_text", "user_email": "email", "user_text": "text"},
#     {"name": "email_and_date", "user_date": "date", "user_email": "email"},
#     {"name": "phone_and_text", "user_text": "text", "user_phone": "phone"},
#     {"name": "phone_and_date", "user_phone": "phone", "user_date": "date"},
#     {"name": "date", "order_date": "date"},
#     {"name": "email", "user_email": "email"},
#     {}
# ])

