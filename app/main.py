from fastapi import FastAPI
from app.database import Base, engine
from app.routes import usuarios

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(usuarios.router)