# Componey API Documentation

Base URL: `/api/companies/`

---

## Endpoints Overview

| Endpoint                 | Method | Description                        | Permissions          |
|--------------------------|--------|------------------------------------|-------------------|
| `/api/companies/`        | GET    | List all companies                 | Public             |
| `/api/companies/`        | POST   | Create a new company               | Admin only         |
| `/api/companies/<id>/`   | GET    | Retrieve company detail            | Public             |
| `/api/companies/<id>/`   | PUT    | Update a company (full update)    | Admin only         |
| `/api/companies/<id>/`   | PATCH  | Update a company (partial update) | Admin only         |
| `/api/companies/<id>/`   | DELETE | Delete a company                  | Admin only         |

---

## 1. List Companies

**Request:**  

```http
GET /api/companies/
```

**Response Example:**

```json
[
  {
    "id": 1,
    "name": "NikeCo",
    "slug": "nikeco"
  },
  {
    "id": 2,
    "name": "AdidasCo",
    "slug": "adidasco"
  }
]
```

---

## 2. Create Company (Admin Only)

**Request:**  

```http
POST /api/companies/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "PumaCo"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "PumaCo",
  "slug": "pumaco"
}
```

---

## 3. Retrieve Company Detail

**Request:**  

```http
GET /api/companies/3/
```

**Response Example:**

```json
{
  "id": 3,
  "name": "PumaCo",
  "slug": "pumaco"
}
```

---

## 4. Update Company (Admin Only)

### PUT (Full Update)

**Request:**

```http
PUT /api/companies/3/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "Puma International"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Puma International",
  "slug": "puma-international"
}
```

### PATCH (Partial Update)

**Request:**

```http
PATCH /api/companies/3/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "Puma Global"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Puma Global",
  "slug": "puma-global"
}
```

---

## 5. Delete Company (Admin Only)

**Request:**

```http
DELETE /api/companies/3/
Authorization: Bearer <admin_token>
```

**Response:**  

```http
204 No Content
```

---

**Notes:**

- `slug` is automatically generated from the `name` field and must be unique.
- Only admin users can create, update, or delete companies.
- GET requests are public.
