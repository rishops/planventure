# Quickstart for Trip Management API

This guide provides instructions on how to use the Trip Management API endpoints.

## Authentication

All endpoints require a valid JSON Web Token (JWT) to be included in the `Authorization` header of the request.

`Authorization: Bearer <YOUR_JWT>`

## Endpoints

### Create a new trip

- **POST** `/trips`

**Request Body:**

```json
{
  "name": "My Awesome Trip",
  "start_date": "2025-12-01",
  "end_date": "2025-12-10"
}
```

### Get all trips

- **GET** `/trips`

### Get a single trip

- **GET** `/trips/<trip_id>`

### Update a trip

- **PUT** `/trips/<trip_id>`

**Request Body:**

```json
{
  "name": "My Updated Awesome Trip",
  "start_date": "2025-12-02",
  "end_date": "2025-12-11"
}
```

### Delete a trip

- **DELETE** `/trips/<trip_id>`
