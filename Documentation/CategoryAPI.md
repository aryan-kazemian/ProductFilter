# Category API Documentation

Base URL: `/api/categories/`

---

## Endpoints Overview

| Endpoint               | Method | Description                         | Permissions          |
|------------------------|--------|-------------------------------------|-------------------|
| `/api/categories/`     | GET    | List all categories                 | Public             |
| `/api/categories/`     | POST   | Create a new category               | Admin only         |
| `/api/categories/<id>/` | GET    | Retrieve category detail            | Public             |
| `/api/categories/<id>/` | PUT    | Update a category (full update)    | Admin only         |
| `/api/categories/<id>/` | PATCH  | Update a category (partial update) | Admin only         |
| `/api/categories/<id>/` | DELETE | Delete a category                  | Admin only         |

---

## 1. List Categories

**Request:**  

```http
GET /api/categories/
```

**Response Example:**

```json
[
  {
    "id": 1,
    "name": "Shoes",
    "slug": "shoes",
    "parent": null
  },
  {
    "id": 2,
    "name": "Running Shoes",
    "slug": "running-shoes",
    "parent": 1
  }
]
```

---

## 2. Create Category (Admin Only)

**Request:**  

```http
POST /api/categories/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "Sneakers",
  "parent": 1
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Sneakers",
  "slug": "sneakers",
  "parent": 1
}
```

---

## 3. Retrieve Category Detail

**Request:**  

```http
GET /api/categories/3/
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Sneakers",
  "slug": "sneakers",
  "parent": 1
}
```

---

## 4. Update Category (Admin Only)

### PUT (Full Update)

**Request:**

```http
PUT /api/categories/3/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "Casual Sneakers",
  "parent": 1
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Casual Sneakers",
  "slug": "casual-sneakers",
  "parent": 1
}
```

### PATCH (Partial Update)

**Request:**

```http
PATCH /api/categories/3/
Content-Type: application/json
Authorization: Bearer <admin_token>
```

**JSON Body Example:**

```json
{
  "name": "Sport Sneakers"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "Sport Sneakers",
  "slug": "sport-sneakers",
  "parent": 1
}
```

---

## 5. Delete Category (Admin Only)

**Request:**

```http
DELETE /api/categories/3/
Authorization: Bearer <admin_token>
```

**Response:**  

```http
204 No Content
```

---

**Notes:**

- `slug` is automatically generated from the `name` field and must be unique.
- `parent` is optional and allows hierarchical categories.
- Only admin users can create, update, or delete categories.
