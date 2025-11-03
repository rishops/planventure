<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
    - PRINCIPLE_1_NAME → I. Python Best Practices
    - PRINCIPLE_2_NAME → II. Secure Libraries
    - PRINCIPLE_3_NAME → III. Testing
    - PRINCIPLE_4_NAME → IV. Framework
    - PRINCIPLE_5_NAME → V. Database
- Added sections:
    - VI. Authentication
    - VII. Password Management
    - VIII. API Structure
    - IX. Development Practice
- Removed sections: None
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md
    - ✅ .specify/templates/spec-template.md
    - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Planventure Constitution

## Core Principles

### I. Python Best Practices
All code must adhere to PEP 8 and prioritize clarity, simplicity, and maintainability.

### II. Secure Libraries
Only use well-maintained, secure, and trusted libraries and packages. Vulnerability scanning is mandatory.

### III. Testing
All new features and bug fixes must be accompanied by comprehensive unit tests using the `unittest` framework.

### IV. Framework
The application will be built using the Flask framework.

### V. Database
SQLAlchemy is the designated ORM for all database interactions. For development, SQLite is the standard database.

### VI. Authentication
Authentication must be implemented using JSON Web Tokens (JWT) via the `Flask-JWT-Extended` library.

### VII. Password Management
Passwords must be securely hashed using `bcrypt`.

### VIII. API Structure
The API will be organized into modular, reusable components using Flask Blueprints.

### IX. Development Practice
All API routes must be protected by default. Public access is an exception and must be explicitly declared and justified.

## Governance

All development activities, including code reviews and automated checks, must enforce compliance with this constitution. Any deviation requires a formal exemption approved by the project lead.

**Version**: 1.0.0 | **Ratified**: 2025-11-03 | **Last Amended**: 2025-11-03