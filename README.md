# Inventory Management System

## Overview

Inventory Management System built using FastAPI, React, PostgreSQL, Docker, and Docker Compose.

The application supports:

* Product Management
* Customer Management
* Order Management
* Inventory Tracking
* Dashboard Analytics

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL

### Frontend

* React
* Vite
* Axios

### DevOps

* Docker
* Docker Compose

---

## Features

### Product Management

* Create Product
* View Products
* Update Product
* Delete Product
* Search Products
* Pagination

### Customer Management

* Create Customer
* View Customers
* Delete Customer

### Order Management

* Create Order
* View Orders
* Inventory Validation
* Automatic Inventory Deduction
* Automatic Order Total Calculation

### Dashboard

* Total Products
* Total Customers
* Total Orders
* Low Stock Products

---

## Project Structure

inventory-management-system/

├── backend/

├── frontend/

├── docker-compose.yml

└── README.md

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run migrations:

```bash
alembic upgrade head
```

Start server:

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Docker Setup

```bash
docker compose up --build
```

Backend:

http://localhost:8000/docs

Frontend:

http://localhost:5173

---

## API Endpoints

### Products

* POST /products
* GET /products
* GET /products/{id}
* PUT /products/{id}
* DELETE /products/{id}

### Customers

* POST /customers
* GET /customers
* GET /customers/{id}
* DELETE /customers/{id}

### Orders

* POST /orders
* GET /orders
* GET /orders/{id}
* DELETE /orders/{id}

### Dashboard

* GET /dashboard

---