from contextlib import asynccontextmanager

from fastapi import FastAPI

from auth.routes import router as auth_router
from llm.inference import clear_predictor, set_predictor
from llm.routes import router as llm_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    set_predictor()
    yield
    clear_predictor()


app = FastAPI(title="Mental Disorder Detection API", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(llm_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Disorder Detection API"}
