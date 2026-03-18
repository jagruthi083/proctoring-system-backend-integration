from fastapi import FastAPI
from app.api import router
import uvicorn

app = FastAPI(
    title="Proctoring System Backend Integration"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
