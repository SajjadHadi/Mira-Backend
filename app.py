import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import router as auth_router
from db import check_database
from llm.inference import clear_predictor, set_predictor
from llm.routes import router as llm_router
from migrations.runner import run_migrations

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_migrations()
    check_database()
    set_predictor()
    yield
    clear_predictor()


app = FastAPI(title="Mental Disorder Detection API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # <-- Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(llm_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Disorder Detection API"}
