# ASKADEMIC

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)


# Overview

**AskAdemic** is an AI-powered chatbot that leverages a **Retrieval-Augmented Generation (RAG)** system to assist university students in their studies.  

Designed with a focus on **efficiency** and **time management**, AskAdemic offers intelligent, context-aware support to streamline learning and academic research.

### Key Features

-  AI-driven chatbot support  
-  Uses RAG to provide accurate, up-to-date responses  
-  Tailored for university-level study needs  
-  Prioritizes efficiency and effective time management  

---

AskAdemic helps students make the most of their study sessions by providing just-in-time information, personalized guidance, and smart learning support.

---

## Problem Statement

Many university students struggle to **revise what they studied earlier in the semester**, especially as exams approach. The overwhelming amount of material and limited time make it challenging to recall key concepts and prepare effectively.

## Our Solution: AskAdemic

**AskAdemic** is designed to solve this problem by making revision **easy, focused, and efficient**. It leverages a **Retrieval-Augmented Generation (RAG)** system to intelligently answer questions based on the materials students have previously studied.

Whether it's lecture notes, textbooks, or past questions, AskAdemic retrieves relevant content and generates accurate responses, helping students revise with confidence — just when it matters most.

## Target Audience

This project is **tailored for university students**, with the goal of supporting academic success across diverse institutions.  

The **Minimum Viable Product (MVP)** will initially be deployed for **Ahmadu Bello University (ABU), Zaria Nigeria**, serving as a pilot to refine the experience before expanding to other universities.

## Tech Stack


1. [**UV**](https://github.com/astral-sh/uv) – Python dependency manager  
2. [**Docker / Docker Compose**](https://www.docker.com/) – Containerization for consistent environments  
3. [**Pinecone**](https://www.pinecone.io/) – Vector database for semantic search and document retrieval  
4. [**Google Gemini**](https://deepmind.google/models/gemini/) – Chat model for natural language responses  
5. [**FastAPI**](https://fastapi.tiangolo.com/) – High-performance backend framework in Python  
6. [**LlamaIndex**](https://docs.llamaindex.ai/) – Used to implement the RAG pipeline  
7. [**MongoDB**](https://www.mongodb.com/) – NoSQL database for storing user sessions, metadata, and documents  
8. [**Jupyter Notebook**](https://jupyter.org/) – For experimentation, prototyping, and research

---
### Local Setup Instructions


1. **Clone the Repository**
    ```bash
    git clone https://github.com/Emmanuel-Oyewole/askademic.git
    cd api
    ```
2. **Build and Strat the Docker-Compose Service**
    Create .env file in  `api/`
     ```bash
    docker-compose up --build
     ```
3. **Navigate to the Docs URL***
    ```bash
    http://localhost:8081/docs
    ```
4. **Stop the Docker Containers**
    ```bash
    docker-compose down
    ```
