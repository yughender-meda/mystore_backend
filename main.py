import models
import user_ops
from fastapi import FastAPI
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication

app = FastAPI()
app.include_router(user_ops.router)
app.include_router(authentication.router)

# in order to handlew the cross origin requests
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"welcome": "mystore"}


models.Base.metadata.create_all(engine)
