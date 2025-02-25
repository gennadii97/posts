from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from app.database import db_helper, Base
from app.api import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/users")


# app.include_router....


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
