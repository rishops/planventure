# Tasks: Trip Management

**Input**: Design documents from `/specs/003-trip-management/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `planventure-api/`, `tests/` at repository root

## Phase 1: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T001 [P] Create a new blueprint for trips in `planventure-api/trips/routes.py`.
- [x] T002 [P] Register the trips blueprint in `planventure-api/app.py`.
- [x] T003 [P] Add `Trip` and `Itinerary` models to `planventure-api/models.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 2: User Story 1 - Create a new trip (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to create a new trip so that I can start planning my travels.

**Independent Test**: A user can create a new trip with a name, start date, and end date. The trip is saved and associated with their account.

### Implementation for User Story 1

- [x] T004 [US1] Implement the `POST /trips` endpoint in `planventure-api/trips/routes.py` to create a new trip.
- [x] T005 [US1] Add a function to generate a default itinerary when a trip is created in `planventure-api/trips/routes.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 3: User Story 2 - View all my trips (Priority: P2)

**Goal**: As a user, I want to view a list of all my trips so that I can see my travel history and select a trip to view or edit.

**Independent Test**: A user can see a list of all the trips they have created.

### Implementation for User Story 2

- [x] T006 [US2] Implement the `GET /trips` endpoint in `planventure-api/trips/routes.py` to retrieve all trips for the authenticated user.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 4: User Story 3 - View a single trip (Priority: P2)

**Goal**: As a user, I want to view the details of a single trip, including its default itinerary.

**Independent Test**: A user can select a trip from their list and see its details.

### Implementation for User Story 3

- [x] T007 [US3] Implement the `GET /trips/<trip_id>` endpoint in `planventure-api/trips/routes.py` to retrieve a single trip.

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently.

---

## Phase 5: User Story 4 - Update a trip (Priority: P3)

**Goal**: As a user, I want to update the details of a trip, such as its name, start date, or end date.

**Independent Test**: A user can edit the details of an existing trip.

### Implementation for User Story 4

- [x] T008 [US4] Implement the `PUT /trips/<trip_id>` endpoint in `planventure-api/trips/routes.py` to update a trip.

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently.

---

## Phase 6: User Story 5 - Delete a trip (Priority: P3)

**Goal**: As a user, I want to delete a trip so that I can remove it from my travel history.

**Independent Test**: A user can delete a trip they own.

### Implementation for User Story 5

- [x] T009 [US5] Implement the `DELETE /trips/<trip_id>` endpoint in `planventure-api/trips/routes.py` to delete a trip.

**Checkpoint**: All user stories should now be functional.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T010 [P] Add error handling for all endpoints in `planventure-api/trips/routes.py`.
- [x] T011 [P] Ensure all endpoints in `planventure-api/trips/routes.py` require a valid JWT token.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Foundational (Phase 1)**: No dependencies - can start immediately. BLOCKS all user stories.
- **User Stories (Phase 2-6)**: All depend on Foundational phase completion.
- **Polish (Phase 7)**: Depends on all desired user stories being complete.

### User Story Dependencies

- All user stories can be implemented independently after the Foundational phase is complete.

### Parallel Opportunities

- All Foundational tasks marked [P] can run in parallel.
- Once the Foundational phase is complete, all user stories can be worked on in parallel.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Foundational
2. Complete Phase 2: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently

### Incremental Delivery

1. Complete Foundational → Foundation ready
2. Add User Story 1 → Test independently
3. Add User Story 2 → Test independently
4. ... and so on.
