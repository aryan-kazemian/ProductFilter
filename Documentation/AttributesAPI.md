# Attributes API Documentation

Base URL: `/api/attributes/`

---

## Endpoints Overview

| Model   | List / Create URL           | Detail URL                     | Permissions |
|---------|----------------------------|--------------------------------|-------------|
| Country | `/countries/`              | `/countries/<id>/`            | GET: Public, POST: Admin |
| Color   | `/colors/`                 | `/colors/<id>/`               | GET: Public, POST: Admin |
| Gender  | `/genders/`                | `/genders/<id>/`              | GET: Public, POST: Admin |
| Age     | `/ages/`                   | `/ages/<id>/`                 | GET: Public, POST: Admin |
| Season  | `/seasons/`                | `/seasons/<id>/`              | GET: Public, POST: Admin |
| Tag     | `/tags/`                   | `/tags/<id>/`                 | GET: Public, POST: Admin |

---

## 1. Country

**List / Create:** `GET / POST /api/attributes/countries/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/countries/<id>/`

**Create JSON Example:**

```json
{
  "name": "United States"
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "United States",
  "slug": "united-states"
}
```

---

## 2. Color

**List / Create:** `GET / POST /api/attributes/colors/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/colors/<id>/`

**Create JSON Example:**

```json
{
  "name": "Red",
  "color": "#FF0000"
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "Red",
  "color": "#FF0000",
  "slug": "red"
}
```

---

## 3. Gender

**List / Create:** `GET / POST /api/attributes/genders/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/genders/<id>/`

**Create JSON Example:**

```json
{
  "name": "male"
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "male",
  "slug": "male"
}
```

---

## 4. Age

**List / Create:** `GET / POST /api/attributes/ages/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/ages/<id>/`

**Create JSON Example:**

```json
{
  "name": "Child",
  "min_age": 3,
  "max_age": 12
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "Child",
  "min_age": 3,
  "max_age": 12,
  "slug": "child"
}
```

---

## 5. Season

**List / Create:** `GET / POST /api/attributes/seasons/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/seasons/<id>/`

**Create JSON Example:**

```json
{
  "name": "Summer"
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "Summer",
  "slug": "summer"
}
```

---

## 6. Tag

**List / Create:** `GET / POST /api/attributes/tags/`  
**Detail:** `GET / PATCH / PUT / DELETE /api/attributes/tags/<id>/`

**Create JSON Example:**

```json
{
  "name": "New Arrival"
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "New Arrival",
  "slug": "new-arrival"
}
```

---

## Notes

- `GET` requests are public and available to all users.  
- `POST`, `PUT`, `PATCH`, `DELETE` are restricted to **admin users only**.  
- `slug` is automatically generated based on the `name`.  
- Use `Authorization: Bearer <jwt_access_token>` header for admin actions.  

