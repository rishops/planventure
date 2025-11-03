# Data Model: User Authentication

**Date**: 2025-11-03

## Entities

### User

Represents a user of the application.

**Fields**:

- `id`: Integer, Primary Key
- `email`: String, Unique, Not Nullable
- `password_hash`: String, Not Nullable

**Relationships**:

- None for this feature.

**Validation Rules**:

- `email` must be a valid email format.
- `password` must meet complexity requirements (to be defined in the implementation).