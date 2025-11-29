from fastapi import FastAPI, HTTPException, Request
import json
from .config import STUDENT_EMAIL, STUDENT_SECRET
from .solver.models import QuizInput
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.post("/")
async def handle_quiz(request: Request):

    raw = await request.body()
    print("RAW BODY:", raw)
    data = json.loads(raw.decode())
    print("PARSED DATA:", data)

    quiz_req = QuizInput(**data)
    print("QUIZ REQ:", quiz_req)

    if quiz_req.secret != STUDENT_SECRET:
        raise HTTPException(403, "Invalid secret")
    if quiz_req.email != STUDENT_EMAIL:
        raise HTTPException(403, "Invalid email")

    chain_req = quiz_req

    from app.solver.solve import solve
    result = await solve(chain_req)

    return {"status": "completed", "result": result}
