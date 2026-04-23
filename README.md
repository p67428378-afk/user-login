# Vehicle Insurance Premium Calculator

This project is a full-stack application that calculates vehicle insurance premiums based on a variety of factors. It includes a FastAPI backend and a React frontend.

## Application Architecture

- **Backend**: FastAPI (Python)
- **Frontend**: React (Vite)
- **Database**: PostgreSQL (or SQLite for local testing)

The application is designed with a microservice-oriented architecture. The backend provides a RESTful API for premium calculation, while the frontend offers a user-friendly interface for insurance agents.

### High-Level Diagram

```mermaid
graph TD
    A[Frontend - React] --> B{API Gateway};
    B --> C[Backend - FastAPI];
    C --> D[Database - PostgreSQL];
```

## Project Structure

```
.
├── backend
│   ├── api
│   │   └── v1
│   │       └── premium_calculation.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── hooks
│   │   ├── pages
│   │   └── services
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── tests
    ├── conftest.py
    └── test_premium_calculation.py
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- git

## Setup Instructions

### Backend

1.  Navigate to the `backend` directory.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file and add the `DATABASE_URL` (e.g., `DATABASE_URL=postgresql://user:password@host:port/database`). If not provided, it will use a local SQLite database.
6.  Start the server: `uvicorn main:app --reload`

### Frontend

1.  Navigate to the `frontend` directory.
2.  Install the dependencies: `npm install`
3.  Start the development server: `npm run dev`

## API Documentation

### POST /api/v1/premium-calculation/

Calculates the insurance premium.

**Request Body:**

```json
{
  "customer_id": "string",
  "policy_id": "string",
  "vehicle_type": "string",
  "vehicle_make": "string",
  "vehicle_model": "string",
  "age_band": "string",
  "safety_features": [
    "string"
  ],
  "years_no_claim": 0
}
```

**Response:**

```json
{
  "policy_id": "string",
  "calculated_premium": 0
}
```

## Running Tests

### Backend

Navigate to the `backend` directory and run:

```bash
pytest
```

### Frontend

Navigate to the `frontend` directory and run:

```bash
npm test
```
