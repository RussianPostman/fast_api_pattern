from fastapi import FastAPI

from api_project.adapters.api.rates.router import rates_router
from api_project.adapters.db.settings import Settings

app = FastAPI()

a = Settings()

app.include_router(rates_router)


@app.get("/")
def test_end():
    return {"message": "Hello World"}
