# Brand API Usage

**Base URL:** `/api/brands/`

---

## 1. List all brands (GET)

* **URL:** `/api/brands/`
* **Method:** GET
* **Permissions:** Public
* **Request JSON:** None
* **Response JSON Example:**

```json
[
    {
        "id": 1,
        "name": "Nike",
        "slug": "nike"
    },
    {
        "id": 2,
        "name": "Adidas",
        "slug": "adidas"
    }
]
```

---

## 2. Create a new brand (POST)

* **URL:** `/api/brands/`
* **Method:** POST
* **Permissions:** Admin only
* **Request JSON (full):**

```json
{
    "name": "Puma"
}
```

* **Response JSON Example:**

```json
{
    "id": 3,
    "name": "Puma",
    "slug": "puma"
}
```

> Note: `slug` is generated automatically.

---

## 3. Retrieve brand detail (GET)

* **URL:** `/api/brands/<int:pk>/`
* **Method:** GET
* **Permissions:** Public
* **Request JSON:** None
* **Response JSON Example:**

```json
{
    "id": 1,
    "name": "Nike",
    "slug": "nike"
}
```

---

## 4. Update brand (PATCH / PUT)

* **URL:** `/api/brands/<int:pk>/`
* **Method PATCH:** Partial update (e.g., just name)
* **Method PUT:** Full update (all fields)
* **Permissions:** Admin only
* **PATCH JSON Example:**

```json
{
    "name": "Nike Updated"
}
```

* **PUT JSON Example:**

```json
{
    "name": "Nike Updated"
}
```

* **Response JSON Example:**

```json
{
    "id": 1,
    "name": "Nike Updated",
    "slug": "nike-updated"
}
```

> `slug` is automatically updated if `name` changes.

---

## 5. Delete brand (DELETE)

* **URL:** `/api/brands/<int:pk>/`
* **Method:** DELETE
* **Permissions:** Admin only
* **Request JSON:** None
* **Response JSON:** None (204 No Content)
