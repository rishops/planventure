# Building the Planventure API with Spec-Driven Development (SDD)

This guide will walk you through creating a Flask-based REST API with SQLAlchemy and JWT authentication using the `spec-kit` methodology to ensure a structured, consistent, and efficient development process powered by Gemini Code Assist.

## Prerequisites

- Python 3.8 or higher
- nodejs v18+ / npm v10+
- Gemini CLI Companion Mode
- Git installed
- `uv` package manager - https://docs.astral.sh/uv/
- `spec-kit` CLI installed
- Bruno API Client (for testing API endpoints) (optional)

## The Spec-Driven Development (SDD) Workflow

We will replace ad-hoc prompting with a structured workflow that turns specifications into the source of truth. The core cycle is:
1.  **Specify**: Define *what* the feature should do in a structured `spec.md`.
2.  **Plan**: Translate the spec into a technical `plan.md`, outlining *how* it will be built.
3.  **Tasks**: Break the plan down into a concrete, executable `tasks.md`.
4.  **Implement**: Execute the tasks to generate the code.

## Step 1: Project Initialization and Constitution

### Clone the repository
```
git clone https://github.com/rishops/planventure.git
```
>Make sure you are on `api-start` (default) branch

### Initialize the Project
First, bootstrap the project with the `spec-kit` framework.

```sh
uvx --from git+https://github.com/github/spec-kit.git specify init --here
```

or if you are using specify cli
```sh
specify init --here
```

And select `Gemini CLI`

### Define the Project Constitution
Before writing any code, we define the project's architectural principles. In the GCA chat, define the constitution.

**Prompt:**
```
/speckit.constitution Establish the project principles based on the following:
- Best python coding practises
- Using secure libraries and packages
- **Testing**: unittest
- **Framework**: Flask
- **Database**: SQLAlchemy with SQLite for development
- **Authentication**: JWT (Flask-JWT-Extended)
- **Password Management**: bcrypt for hashing
- **API Structure**: Use Flask Blueprints for modular routes.
- **Development Practice**: All routes must be protected by default, with exceptions made explicit.
```

Collaborate with the Gemini CLI/Code Assist to establish these principles in the generated `.specify/memory/constitution.md` file.

## Step 2: Foundational API Setup

Instead of building the entire authentication feature at once, let's first lay the foundation by configuring the core libraries.

### Specify the Setup
This specification will handle the initial configuration of Flask, SQLAlchemy, and JWT.

**Prompt:**
```
/speckit.specify

Feature: Initial API Setup

This feature will configure the basic Flask application with database and authentication libraries. It should include:
- Integration of Flask-SQLAlchemy.
- Integration of Flask-JWT-Extended.
- Basic configuration in app.py for SQLAlchemy and JWT.
- Update requirements.txt with the necessary packages.
```

### Plan the Implementation
Provide technical direction for setting up the core components.

**Prompt:**
```
/speckit.plan

Technical Direction: Update app.py to initialize Flask-SQLAlchemy and JWTManager. Add Flask-SQLAlchemy, Flask-JWT-Extended, bcrypt, and python-dotenv to requirements.txt.
```

### Generate, Implement, and Install
The AI will now generate the tasks, implement them, and then you can install the new dependencies.

**Prompts:**
```
/speckit.tasks
```
```
/speckit.implement
```

### Install Dependencies and Configure Environment
Install the new packages and create your local environment file by copying the existing sample.

```bash
pip install -r requirements.txt
cp planventure-api/.sample.env planventure-api/.env
```

Your local configuration is now ready in `planventure-api/.env`. You can edit this file to change your `JWT_SECRET_KEY` or other settings. It is already in `.gitignore` and will not be committed.

## Step 3: The User Authentication Feature

Now that the app is configured, we can build the user model and authentication endpoints.

### Specify the Feature
This spec focuses on user registration and login functionality.

**Prompt:**
```
/speckit.specify

Feature: User Authentication System

This feature will handle user registration and login. It should include:
- A User model with email and password_hash fields.
- Utility functions for password hashing and verification using bcrypt.
- A registration endpoint that validates email and hashes passwords.
- A login endpoint that verifies credentials and returns a JWT token.
- A database initialization script to create tables.
```

### Plan the Implementation
Translate the spec into a technical plan.

**Prompt:**
```
/speckit.plan

Technical Direction: Create a User model in a new `models.py` file. Create password utility functions in a `utils.py` file. Create a dedicated 'auth' blueprint for the routes. Generate an `init_db.py` script to create the database tables based on the defined models.
```

### Generate and Implement Tasks
The AI will break the plan into a list of executable tasks and then implement them.

**Prompts:**
```
/speckit.tasks
```
```
/speckit.implement
```

### Initialize Database & Test
Create the database tables and test the new endpoints.
```bash
python init_db.py
```
(optional)
Use the Bruno API Client to test the `/auth/register` and `/auth/login` endpoints as described in the original `PROMPTS.md` to verify the implementation.

## Step 4: The Trips Feature

Now, we repeat the cycle for the trips functionality.

### Specify, Plan, Task, Implement
**1. Specify the Trips Feature:**
```
/speckit.specify

Feature: Trip Management

This feature allows authenticated users to perform CRUD operations on their trips. It should include:
- A Trip model linked to a user.
- Endpoints to create, read, update, and delete trips.
- A function to generate a default itinerary when a trip is created.
```

**2. Plan the Implementation:**
```
/speckit.plan

Technical Direction: Create a 'trips' blueprint. The Trip model should include destination, dates, and an itinerary, and be added to `models.py`. All routes must require a valid JWT token for access.
```

**3. Generate and Implement Tasks:**
```
/speckit.tasks
```
```
/speckit.implement
```
This generates the `Trip` model, the `trips` blueprint with all CRUD routes, and integrates the itinerary generation logic.

### Update Database and Test
Run the database initialization script again to add the `trip` table.
```bash
python init_db.py
```
Use Bruno to test the protected trip endpoints, ensuring you include the JWT token in the `Authorization` header.

## Step 5: Finalize API

### Specify Core API Features
Group finalization tasks like CORS and health checks into a single specification.

**Prompt:**
```
/speckit.specify

Feature: Core API Finalization

This includes final setup for production readiness:
- Configure CORS to allow access from a React frontend.
- Add a public `/health` endpoint for monitoring.
```

### Plan, Task, Implement
Run the workflow to add the necessary configurations.

**Prompt:**
```
/speckit.plan

Technical Direction: Use Flask-CORS for the configuration and apply it to the main Flask app instance in app.py. The health check endpoint should be a simple route returning a JSON response.
```

**Prompts:**
```
/speckit.tasks
```
```
/speckit.implement
```
This will update `app.py` with CORS configuration and the new `/health` route.

## Conclusion

By using the Spec-Driven Development workflow, you have built the same API but with a more robust, documented, and consistent process. The specifications, plans, and tasks serve as living documentation, and the constitutional approach ensures all code adheres to your project's core principles. This method streamlines development, reduces ambiguity, and makes the project easier to maintain and scale.
