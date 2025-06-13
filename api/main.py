from contextlib import asynccontextmanager
from typing import AsyncGenerator
import logging

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorDatabase as AsyncDB



from src.database.init_db import MongoDB

from src.controllers.root import router as root_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Connect to MongoDB
    await MongoDB.initialize_db()
    logger.info("✅✅Connected to MongoDB")
    print("✅✅ Connected to MongoDB")

    yield
    # Close MongoDB connection
    await MongoDB.close()
    logger.info("✅✅Closed MongoDB Connection")
    print("✅✅ Closed MongoDB Connection")


app = FastAPI(
    title="Askademic API",
    description="**AskAdemic** is an AI-powered chatbot 🤖🤖 that leverages a **Retrieval-Augmented Generation (RAG)** system to assist university students in their studies.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_router)
