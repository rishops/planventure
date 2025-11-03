# Quickstart Guide

This guide explains how to set up and run the application after the initial API setup.

## Prerequisites

- Python 3.11+
- pip

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** in the `planventure-api` directory with the following content:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY='your-secret-key'
    JWT_SECRET_KEY='your-jwt-secret-key'
    SQLALCHEMY_DATABASE_URI='sqlite:///planventure.db'
    ```

## Running the Application

```bash
flask run
```