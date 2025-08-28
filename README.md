# HelpDesk API

## Overview

**HelpDesk API** is a Django REST Framework application for managing users, tickets, and responses in a support system.
It supports token-based authentication and role-based access for normal users, agents, and admins.

* **Backend:** Django 5.x + DRF
* **Database:** PostgreSQL
* **Authentication:** Token Authentication

---

## Base URL

```
http://127.0.0.1:8000/api/
```

* All requests must include the `Content-Type: application/json` header.
* Authentication is via Token.

---

## Authentication

### Obtain Token

**POST** `/api/token/`

**Request body:**

```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

**Response:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "user@example.com",
  "token": "abc123def456"
}
```

**Usage**

Include the token in your headers for all authenticated requests:

```
Authorization: Token abc123def456
```

---

## User Endpoints

### Register Customer

**POST** `/api/register/customer/`

**Request body:**

```json
{
  "email": "customer@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1990-01-01",
  "password": "password123",
  "password2": "password123"
}
```

**Response:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "customer@example.com",
  "date_of_birth": "1990-01-01"
}
```

### Register Agent

**POST** `/api/register/agent/` (Admin only)

**Request body:**

```json
{
  "email": "agent@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "date_of_birth": "1985-05-12",
  "password": "password123",
  "password2": "password123"
}
```

**Response:**

```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "email": "agent@example.com",
  "date_of_birth": "1985-05-12"
}
```

### Login

**POST** `/api/login/`

**Request body:**

```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

**Response:**

```json
{
  "token": "abc123def456",
  "id": 1,
  "first_name": "John",
  "last_name": "Doe"
}
```

### List All Users

**GET** `/api/accounts/` (Admin only)

**Response:**

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "user@example.com",
    "is_agent": false,
    "date_of_birth": "1990-01-01"
  }
]
```

---

## Tickets Endpoints

### Create Ticket

**POST** `/api/tickets/create/`

**Request body:**

```json
{
  "title": "Issue with login",
  "description": "I cannot login with my credentials",
  "ticket_images": []
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Issue with login",
  "description": "I cannot login with my credentials",
  "sender": 1,
  "is_resolved": false,
  "created_at": "2025-08-28T12:00:00Z",
  "ticket_images": []
}
```

### List Tickets (Agents only)

**GET** `/api/tickets/`

**Response:**

```json
[
  {
    "id": 1,
    "title": "Issue with login",
    "description": "I cannot login",
    "sender": 2,
    "is_resolved": false,
    "created_at": "2025-08-28T12:00:00Z",
    "ticket_images": [],
    "ticket_response": null
  }
]
```

### User's Tickets

**GET** `/api/accounts/<user_id>/tickets/`

**Response:**

```json
[
  {
    "id": 1,
    "title": "Issue with login",
    "description": "I cannot login",
    "is_resolved": false,
    "created_at": "2025-08-28T12:00:00Z",
    "ticket_images": [],
    "ticket_response": null
  }
]
```

### Ticket Detail

**GET** `/api/tickets/<ticket_id>/`

**Response:**

```json
{
  "id": 1,
  "title": "Issue with login",
  "description": "I cannot login",
  "is_resolved": false,
  "created_at": "2025-08-28T12:00:00Z",
  "ticket_images": [],
  "ticket_response": null
}
```

---

## Responses Endpoints

### Respond to Ticket (Agents only)

**POST** `/api/tickets/<ticket_id>/respond/`

**Request body:**

```json
{
  "message": "We have reset your password. Try logging in again."
}
```

**Response:**

```json
{
  "message": "Ticket resolved successfully"
}
```

---

## Running the Project

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Add your `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

3. Run migrations and start server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit the API docs at:

```
http://127.0.0.1:8000/api/docs/
```

---

## Contributing

1. Fork the repo
2. Create a branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License
