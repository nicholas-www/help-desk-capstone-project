# HelpDesk API Documentation

---

## Overview

The **HelpDesk API** allows you to manage users, tickets, and responses. All endpoints are RESTful and use **token authentication**.

* **Base URL:** `/api/`
* **Authentication:** Token-based
* **Content-Type:** `application/json`

---

## Authentication

### Obtain Token

**POST** `/api/token/`

**Request body:**

```json
{
  "email": "example@email.com",
  "password": "your_password"
}
```

**Response body:**

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "example@email.com",
    "token": "your_token"
}
```

### Login

**POST** `/api/login/`

**Request body:**

```json
{
  "email": "example@email.com",
  "password": "your_password"
}
```

**Response body:**

```json
{
  "token": "your_token",
  "id": 1,
  "first_name": "John",
  "last_name": "Doe"
}
```

### Logout

**POST** `/api/logout/`

**Headers:**

```
Authorization: Token your_token
```

**Response:**

```json
{
  "detail": "Successfully logged out."
}
```

---

## Users

### Register Customer

**POST** `/api/register/customer/`

**Request body:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "date_of_birth": "YYYY-MM-DD",
  "password": "your_password",
  "password2": "your_password"
}
```

**Response body:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "date_of_birth": "YYYY-MM-DD"
}
```

### Register Agent

**POST** `/api/register/agent/`
**Permissions:** Admin only

**Request body and response:** Same as Customer Registration.

### List Users

**GET** `/api/accounts/`
**Permissions:** Admin only

**Response:**

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "date_of_birth": "YYYY-MM-DD",
    "is_agent": false
  }
]
```

---

## Tickets

### List Tickets

**GET** `/api/tickets/`
**Permissions:** Agents only

**Query parameters (filtering):** `is_resolved`, `created_at`

**Response:**

```json
[
  {
    "id": 1,
    "title": "Cannot login",
    "description": "User cannot login to the portal",
    "status": "open",
    "is_resolved": false,
    "ticket_images": [],
    "ticket_response": []
  }
]
```

### List User Tickets

**GET** `/api/accounts/{id}/tickets/`
**Permissions:** Users only, cannot be agents

**Response:** Same format as Ticket List.

### Create Ticket

**POST** `/api/tickets/create/`
**Permissions:** Customers only

**Request body:**

```json
{
  "title": "Issue title",
  "description": "Detailed description",
  "ticket_images": ["image_url1", "image_url2"]
}
```

**Response:** Returns created ticket with images.

### Retrieve Ticket

**GET** `/api/tickets/{id}/`
**Permissions:** Agents only

**Response:** Ticket object as in list.

---

## Ticket Responses

### Create Response

**POST** `/api/tickets/{ticket_id}/respond/`

**Permissions:** Agents only

**Request body:**

```json
{
  "message": "Resolution message"
}
```

**Response:**

```json
{
  "message": "Ticket resolved successfully"
}
```

**Rules:**

* Cannot respond if ticket is already resolved
* Response `title` auto-prefixed with ticket title

### List Responses (via Ticket)

Included in ticket endpoints under `ticket_response` field.

---

## Filtering & Pagination

* Filter tickets: `/api/tickets/?is_resolved=false&created_at=2025-08-28`
* Pagination: Default page size 10, use `?page=2` for next page.

---

## Error Codes

| Code | Meaning                              |
| ---- | ------------------------------------ |
| 400  | Bad request / validation error       |
| 401  | Unauthorized / missing token         |
| 403  | Forbidden / insufficient permissions |
| 404  | Resource not found                   |
| 500  | Internal server error                |
