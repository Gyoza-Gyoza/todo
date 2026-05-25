from fastapi import FastAPI
from todo import todoFuncs
from Reefvive import Reefvive

app = FastAPI()

app.include_router(todoFuncs.router)
app.include_router(Reefvive.router)