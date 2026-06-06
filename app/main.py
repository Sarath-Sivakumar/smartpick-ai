from app.retriever import retrieve
from app.generator import generate_response
from models.request import UserRequest
from fastapi import FastAPI

app = FastAPI(title="SmartPick AI")


@app.post("/recommend")
def getRecommendation(request: UserRequest):
	results = retrieve(request.query)
	answer = generate_response(
    	request.query,
    	results
	)
	return answer
