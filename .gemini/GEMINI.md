# Planventure Project Overview

This document provides a high-level overview of the Planventure project, including its architecture, technology stack, and key development guidelines.

## Important Documents

- **Development Guidelines:** @../GEMINI.md
- **Project Constitution:** @../.specify/memory/constitution.md

## Project Type

REST API backend for a planning/travel application (Planventure).

## Tech Stack

- **Language:** Python 3.11+
- **Framework:** Flask
- **Database:** SQLAlchemy with SQLite for development
- **Authentication:** JWT using Flask-JWT-Extended
- **Password Hashing:** bcrypt
- **CORS:** Flask-CORS
- **Environment Variables:** python-dotenv

## Architecture

- The application is structured using Flask Blueprints to create a modular and reusable API.
- Current blueprints include `auth` and `trips`.
- The main application is created in `planventure-api/app.py`.

## Commands

- **Run application:** `cd planventure-api && python app.py`
### Run Tests
```
  cd planventure-api
  source venv/bin/activate
  python3 -m unittest discover tests
```
If virtual environment named venv is not initialized, run `python3 -m venv venv` inside `planventure-api` directory.
