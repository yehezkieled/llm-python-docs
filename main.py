from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat")
def chat(msg: Message):
    response = f"You said: {msg.user_input}"
    return {"response": response}

# @app.get("/")
# def root():
#     return {"Hello": "World"}
