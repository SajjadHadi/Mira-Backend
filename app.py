from contextlib import asynccontextmanager

from fastapi import FastAPI

from models.inference import get_predictor, clear_predictor

llm_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    llm_models["mdd_v1"] = get_predictor()
    yield
    llm_models.clear()
    clear_predictor()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    disorders = llm_models["mdd_v1"].predict("""About to start university freak outs This will be my third major attempt at starting a university degree. Each previous attempt i have had panic attacks and random freak outs which caused me to miss lectures and not submit work.

Basically the worry of failure holds me back. And the worry of worrying is holding me back. I keep expecting to fail and therefore fail. I have zero self esteem.

No idea why im posting this. Just scared and don't want to keep bothering my housemates with my nonsense.""")
    return disorders
