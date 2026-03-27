# Architecture Overview

OpenBrain is designed to be a modular, self-hosted AI platform.

## Core Engine
- `Model Loader`: Handles loading of Large Language Models (LLMs) with fallback support for CPU if a GPU is not available.
- `AI Engine`: The main interface for tokenization and inference using `transformers` and `auto-gptq`.
- `AI Router`: A keyword-based routing system that classifies user queries into categories (e.g., coding, math).

## Management System
- `API Key System`: Handles the generation, validation, and usage tracking of API keys.
- `Logging System`: Records every request's query, response, response time, and token usage.
- `Analytics Engine`: Processes logs to provide daily and total usage metrics.

## Frontend
- `Admin Dashboard`: A web interface built with HTML/TailwindCSS/JS for administrators to monitor the server and manage API keys.
