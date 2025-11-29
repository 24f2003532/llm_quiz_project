from pydantic import BaseModel

class QuizInput(BaseModel):
    email: str
    secret: str
    url: str
