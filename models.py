from pydantic import BaseModel

class MessageRequest(BaseModel):
    platform: str
    sender: str
    message: str
    language: str = 'en'


class AppointmentRequest(BaseModel):
    client_name: str
    phone_number: str
    email: str
    country: str
    datetime: str
    language: str = 'en'


class PaymentRequest(BaseModel):
    client_name: str
    phone_number: str
    email: str
    country: str
    amount: float
    currency: str
    language: str = 'en'

class LanguageChangeRequest(BaseModel):
    user_id: str
    new_language: str
