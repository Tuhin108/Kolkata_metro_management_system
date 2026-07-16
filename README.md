# Kolkata Metro Booking & Verification System

A high-performance transit routing, booking, and system verification platform. It demonstrates a dual-database design utilizing **PostgreSQL** for transactional operational data (bookings, configurations, heartbeats) and **SQLite** for static metro graph topology and vault keys.

## Features

1. **Dual-Database Gatekeeper**: Checks credentials across PostgreSQL and SQLite database layers, verifies the background worker heartbeat, and performs AES-256 decryption of the system clearance code.
2. **Dijkstra Metro Routing**: Computes shortest-path itineraries across multi-line metro networks (Green and Blue lines), accounting for travel time, fares, and line transfers at interchange nodes (Esplanade).
3. **Automated Ticket Lifecycle**: A background cron worker automatically sweeps database bookings to mark expired tickets based on timestamps.
4. **Transit Ticket Dashboard**: Complete ticket dashboard showing active/expired statistics, listing bookings, and rendering css-based mock QR codes.

---

## Directory Structure

```text
kolkata-metro-assessment/
├── backend/
│   ├── app/
│   │   ├── main.py (FastAPI application entry point)
│   │   ├── core/
│   │   │   ├── config.py (Pydantic BaseSettings config loader)
│   │   │   └── security.py (AES key derivation & decryption)
│   │   ├── api/
│   │   │   └── routes.py (FastAPI route controllers)
│   │   ├── services/
│   │   │   ├── graph_engine.py (Dijkstra routing logic)
│   │   │   └── unlock_service.py (Gatekeeper system validation)
│   │   ├── db/
│   │   │   ├── postgres_client.py (PostgreSQL clients & schemas)
│   │   │   ├── sqlite_client.py (SQLite client connection)
│   │   │   └── init_sqlite.py (SQLite database graph initializer)
│   │   └── worker/
│   │       └── cron_scheduler.py (Heartbeat and ticket cleaner worker)
│   ├── requirements.txt
│   └── .env (Local defaults)
├── frontend/
│   ├── src/
│   │   ├── App.jsx (Main container)
│   │   ├── components/ (Dashboard, RouteSelector, SystemStatus)
│   │   ├── services/api.js (Axios API connection)
│   │   └── index.css (Tailwind rules)
│   ├── package.json
│   └── vite.config.js
├── database_setup/
│   └── postgres_init.sql (Postgres schemas & Key A seed)
├── TASK.md (Candidate requirements)
└── README.md (This setup document)
```

---

## Prerequisites

Before starting, ensure you have the following installed on your machine:
- **Node.js** (v18 or higher) & **npm**
- **Python** (v3.9 or higher) & **pip**
- **PostgreSQL** database server running locally

---

## Setup Instructions

### 1. Database Setup

#### PostgreSQL Configuration
1. Start your local PostgreSQL server.
2. Create a database named `kolkata_metro`:
   ```sql
   CREATE DATABASE kolkata_metro;
   ```
3. Execute the schema initialization script:
   ```bash
   psql -h localhost -U postgres -d kolkata_metro -f database_setup/postgres_init.sql
   ```
   *(Adjust username `-U` and host `-h` options as needed for your local setup).*

#### SQLite Configuration
Database alraedy initialized

---

### 2. Backend Installation & Start

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Verify/configure environment settings in `.env` if your local Postgres connection credentials differ from the defaults.
5. Start the backend development server using uvicorn:
   ```bash
   python3 -m uvicorn app.main:app --reload --port 8000
   ```
   The backend API will run at `http://localhost:8000`. Swagger documentation is available at `http://localhost:8000/docs`.

---

### 3. Frontend Installation & Start

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install Node packages:
   ```bash
   npm install
   ```
3. Start the Vite React development server:
   ```bash
   npm run dev
   ```
   The React application will launch at `http://localhost:5173`.
