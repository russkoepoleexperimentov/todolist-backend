from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .models.database import Base, engine

from .routing.task import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)