from contextlib import asynccontextmanager

import uvicorn
from database.connection import Settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.events import event_router
from routes.users import user_router

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=lifespan)

# Registra as origem que podem consumir a API.
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rotas
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
