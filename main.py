from fastapi import FastAPI
from database import Base, engine
from routers import user, records, dashboard, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(records.router)
app.include_router(dashboard.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Finance Backend Running"}