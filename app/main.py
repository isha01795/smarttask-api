from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, task

app = FastAPI(title="SmartTask API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "SmartTask API running"}