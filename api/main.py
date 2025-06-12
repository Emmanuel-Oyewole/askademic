from fastapi import FastAPI
from .controllers.root import router as root_router

app = FastAPI(
    title="Askademic API",
    description="**AskAdemic** is an AI-powered chatbot 🤖🤖 that leverages a **Retrieval-Augmented Generation (RAG)** system to assist university students in their studies.",
    version="1.0.0",
)

app.include_router(root_router)
