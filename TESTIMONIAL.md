# TESTIMONIAL

## Overview

This assessment involved understanding an unfamiliar full-stack codebase consisting of a React + Vite frontend, FastAPI backend, PostgreSQL, and SQLite databases. My approach was to first get the project running successfully before implementing the missing functionality.

## Project Understanding

I began by setting up both frontend and backend environments, configuring the databases, and verifying all dependencies. After understanding the project architecture and SQLite schema, I implemented the missing route-finding logic and integrated it with the frontend.

## Bugs Encountered

- SQLite database path was incorrect.
- CORS configuration prevented frontend communication.
- Frontend API endpoint required configuration.
- Route calculation logic inside the backend was incomplete.
- Backend response format did not match the frontend's expected API contract.

## Fixes Applied

- Corrected the SQLite database path.
- Updated CORS settings to allow the Vite frontend.
- Configured frontend environment variables.
- Implemented Dijkstra's shortest path algorithm using the existing SQLite metro graph.
- Modified the backend response structure to match the frontend API contract.
- Tested ticket booking, QR generation, and booking registry.

## Screenshots
<img width="1918" height="970" alt="Screenshot 2026-07-17 081349" src="https://github.com/user-attachments/assets/5a45abb0-b0d7-4e75-b13a-6a616fc0d18a" />
<img width="1918" height="977" alt="Screenshot 2026-07-17 081028" src="https://github.com/user-attachments/assets/feed629e-4fc3-4f6d-97cc-cc7519a8e494" />
<img width="1918" height="971" alt="Screenshot 2026-07-17 081302" src="https://github.com/user-attachments/assets/e9256675-1f69-47d9-98c0-ac7cfffda34d" />


## Challenges

The biggest challenge was understanding an unfamiliar codebase and maintaining compatibility between frontend and backend without changing the existing API endpoints.

## Assumptions

- Travel time is used as the optimization metric.
- Interchange edges are defined in the SQLite database.
- Existing database schema and station data remain unchanged.

## Future Improvements

If given additional time, I would:

- Improve the route visualization with clearer interchange indicators.
- Enhance UI responsiveness for mobile devices.

## Conclusion

The project was completed successfully with all required functionality working, including station listing, shortest route computation, ticket booking, and QR ticket generation.

## Ignored Files Present in Repo

Note: the following files are present in the repository but intentionally ignored by the repository `.gitignore`:

- `kolkata_metro_ticket_booking_app/frontend/package-lock.json`
- `kolkata_metro_ticket_booking_app/backend/.env`
