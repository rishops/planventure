# Quickstart: User Authentication

**Date**: 2025-11-03

This document provides a quick overview of how to use the User Authentication feature.

## API Endpoints

### Register

- **POST** `/auth/register`
- **Description**: Registers a new user.
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "message": "User created successfully."
  }
  ```

### Login

- **POST** `/auth/login`
- **Description**: Authenticates a user and returns an access token.
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "<your_access_token>"
  }
  ```

## Database Initialization

To create the necessary database tables, run the following command from the `planventure-api` directory:

```bash
python init_db.py
```