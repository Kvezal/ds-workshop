from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
import argparse
import asyncio
import os
from joblib import load

from model.model_api import ModelAPI
from predict import predict_csv_router  # noqa: E402



@asynccontextmanager
async def lifespan(instance: FastAPI):
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, 'ml', '0.0.1.pkl')
    model = await asyncio.to_thread(load, filename=model_path)
    instance.state.model = ModelAPI(model)
    try:
        yield
    finally:
        pass


app = FastAPI(lifespan=lifespan)

app.include_router(predict_csv_router, prefix="/api/predict", tags=["Предсказания на основе модели"])


@app.get('/health', tags=['Служебные endpoint-ы'])
def health():
    return { "status": "OK" }



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8000, type=int, dest='port')
    parser.add_argument('--host', default='0.0.0.0', type=str, dest='host')
    parser.add_argument('--dev', action='store_true', dest="reload")

    args = vars(parser.parse_args())

    uvicorn.run('main:app', **args)