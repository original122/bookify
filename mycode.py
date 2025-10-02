from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from services.messaging import handle_incoming_message
from services.appointments import book_appointment
from services.payments import process_payment
from services.translation import translate_text

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

class MessageRequest(BaseModel):
    platform: str  # 'email', 'whatsapp', 'sms'
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

@app.post("/message/reply")
def reply_message(req: MessageRequest):
    reply = handle_incoming_message(req.platform, req.sender, req.message, req.language)
    return {"reply": reply}


@app.post("/appointment/book")
def book(req: AppointmentRequest):
    confirmation = book_appointment(
        req.client_name,
        req.phone_number,
        req.email,
        req.country,
        req.datetime,
        req.language
    )
    return {"confirmation": confirmation}


@app.post("/payment/process")
def payment(req: PaymentRequest):
    result = process_payment(
        req.client_name,
        req.phone_number,
        req.email,
        req.country,
        req.amount,
        req.currency,
        req.language
    )
    return {"result": result}

@app.post("/language/change")
def change_language(req: LanguageChangeRequest):
    # Store user language preference (mocked)
    return {"message": f"Language changed to {req.new_language}"}
