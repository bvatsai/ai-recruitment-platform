# Enterprise AI Recruitment Platform

## Overview

A production-oriented AI Recruitment Platform being built step-by-step using Python, FastAPI, PostgreSQL, SQLAlchemy, and Local LLMs.

### Project Goals
- Help job seekers improve their resumes
- Help recruiters identify the best candidates
- AI-powered resume parsing and skill extraction
- Semantic job matching using embeddings and RAG
- Agentic AI recruitment assistant

---

## Current Progress

### ✅ Phase 1 - Python Foundations
- Python Fundamentals
- Object-Oriented Programming
- Project Structure
- Git & Virtual Environments

### ✅ Phase 2 - Backend Architecture
- FastAPI
- REST APIs
- Layered Architecture
  - Router
  - Service
  - Repository
- Dependency Injection
- Pydantic Request & Response Models

### ✅ Phase 3 - Database Layer
- PostgreSQL
- SQLAlchemy ORM
- Database Sessions
- ORM Relationships
- CRUD Operations
- Alembic Database Migrations

### ✅ Phase 4 - Resume Management
- Candidate Management
- Profile Management
- Resume Upload API
- PDF Storage
- Resume Replacement
- PDF Text Extraction (pypdf)

---

## 🚧 Upcoming Phases

### ⏳ Phase 5 - AI Resume Understanding
- Ollama Integration
- Local LLM
- Resume Information Extraction
- Skills Extraction
- Experience Extraction
- Education Extraction

### ⏳ Phase 6 - Semantic Search
- Embeddings
- Vector Database
- Resume Search
- Job Matching
- Recommendation Engine

### ⏳ Phase 7 - Agentic AI Recruitment
- LangGraph
- Multi-Agent Workflow
- AI Recruiter
- Interview Recommendation
- Candidate Evaluation

### ⏳ Phase 8 - Production Deployment
- Docker
- Authentication
- Logging
- Monitoring
- Deployment

---

## Current Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

### AI
- pypdf
- Ollama *(Upcoming)*
- LangChain *(Upcoming)*
- LangGraph *(Upcoming)*

### Tools
- Git
- VS Code

---

## Current Architecture

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

## Current Features

- Candidate Management
- Profile Management
- Resume Upload
- PDF Storage
- Automatic Resume Replacement
- PDF Text Extraction
- Clean Layered Architecture
- Dependency Injection
- Repository Pattern
- Service Pattern

---

## Roadmap

- [x] Backend Foundation
- [x] Database Integration
- [x] Resume Upload
- [x] Resume Text Extraction
- [ ] Local LLM Integration
- [ ] Resume Information Extraction
- [ ] Embeddings
- [ ] Vector Search
- [ ] Job Matching
- [ ] RAG
- [ ] LangGraph Agents
- [ ] Production Deployment