# Accounts API Documentation

Base URL: `/api/accounts/`

---

## Endpoints Overview

| Endpoint                       | Method | Description                                | Permissions  |
|--------------------------------|--------|--------------------------------------------|-------------|
| `/api/accounts/register/`       | POST   | Register a new user                         | Public      |
| `/api/accounts/tokens/`         | POST   | Obtain JWT access and refresh tokens       | Public      |
| `/api/accounts/tokens/refresh/` | POST   | Refresh JWT access token                    | Public      |

---

## 1. User Registration

**Request:**  

```http
POST /api/accounts/register/
Content-Type: application/json
```

**JSON Body Example:**

```json
{
  "username": "johndoe",
  "password": "strongpassword123"
}
```

**Response Example:**

```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "role": null,
    "links": {
      "self": "/users/1/",
      "orders": "/users/1/orders/"
    }
  },
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

**Notes:**

- `role` will be `null` by default unless assigned by an admin.
- Password is write-only and will not be returned.

---

## 2. Obtain JWT Tokens

**Request:**

```http
POST /api/accounts/tokens/
Content-Type: application/json
```

**JSON Body Example:**

```json
{
  "username": "johndoe",
  "password": "strongpassword123"
}
```

**Response Example:**

```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "role": null,
    "links": {
      "self": "/users/1/",
      "orders": "/users/1/orders/"
    }
  },
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

**Notes:**

- The `access` token is used for authenticated requests.
- The `refresh` token is used to obtain a new `access` token when it expires.

---

## 3. Refresh JWT Token

**Request:**

```http
POST /api/accounts/tokens/refresh/
Content-Type: application/json
```

**JSON Body Example:**

```json
{
  "refresh": "<jwt_refresh_token>"
}
```

**Response Example:**

```json
{
  "access": "<new_jwt_access_token>"
}
```

---

## Additional Notes

- All endpoints are public for registration and token management.
- The `role` field is optional for users; it is primarily assigned by admins.
- JWT tokens include the user's role in their payload.
- Use the `access` token in the `Authorization` header for authenticated requests:

```http
Authorization: Bearer <jwt_access_token>
```
