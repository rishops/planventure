# Data Model for Trip Management

This document defines the data models for the Trip Management feature.

## Trip Model

Represents a user's trip.

| Field | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| name | String | Not Null |
| start_date | Date | Not Null |
| end_date | Date | Not Null |
| user_id | Integer | Foreign Key to users.id, Not Null |

## Itinerary Model

Represents the itinerary for a trip.

| Field | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| day | Integer | Not Null |
| activities | String | |
| trip_id | Integer | Foreign Key to trips.id, Not Null |
