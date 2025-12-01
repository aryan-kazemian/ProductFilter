# Products API Documentation

Base URL: `/api/products/`

---

## Endpoints Overview

| Endpoint | HTTP Method | Description | Permissions |
|----------|------------|-------------|-------------|
| `/api/products/` | GET | List all products | Public |
| `/api/products/` | POST | Create new product | Admin only |
| `/api/products/<id>/` | GET | Retrieve a single product | Public |
| `/api/products/<id>/` | PUT / PATCH | Update a product | Admin only |
| `/api/products/<id>/` | DELETE | Delete a product | Admin only |

---

## Filters

The following query parameters are supported for **GET /api/products/**:

| Filter Parameter | Type | Description | Example |
|-----------------|------|-------------|---------|
| `min_price` | number | Minimum price | `?min_price=100` |
| `max_price` | number | Maximum price | `?max_price=500` |
| `category` | integer | Category ID | `?category=2` |
| `brand` | integer | Brand ID | `?brand=1` |
| `componey` | integer | Company ID | `?componey=3` |
| `color` | integer | Color ID | `?color=5` |
| `gender` | integer | Gender ID | `?gender=2` |
| `age` | integer | Age ID | `?age=1` |
| `season` | integer | Season ID | `?season=4` |
| `country` | integer | Country ID | `?country=2` |
| `tags` | list of integers | Tag IDs (comma separated) | `?tags=1,2,3` |
| `is_available` | boolean | Product availability | `?is_available=true` |
| `is_exciting` | boolean | Trending product | `?is_exciting=false` |
| `free_shipping` | boolean | Free shipping | `?free_shipping=true` |
| `has_gift` | boolean | Includes gift | `?has_gift=false` |
| `is_budget_friendly` | boolean | Budget friendly | `?is_budget_friendly=true` |
| `rating` | number | Exact rating | `?rating=5` |
| `search` | string | Search by name or description | `?search=shoes` |
| `ordering` | string | Order by field (prefix `-` for descending) | `?ordering=price` or `?ordering=-created_at` |

---

## Product List / Create

**GET /api/products/**

**Response Example:**

```json
[
  {
    "id": 1,
    "name": "Running Shoes",
    "description": "Comfortable shoes for daily running",
    "rating": 5,
    "expire_date": "2025-12-31",
    "category": 2,
    "is_available": true,
    "is_exciting": true,
    "free_shipping": true,
    "has_gift": false,
    "is_budget_friendly": false,
    "price": 150,
    "brand": 1,
    "componey": 3,
    "color": 5,
    "gender": 2,
    "age": 1,
    "season": 4,
    "country": 2,
    "tags": [1,2],
    "created_at": "2025-12-01T12:00:00Z",
    "updated_at": "2025-12-01T12:00:00Z"
  }
]
```

**POST /api/products/**

**Request Example:**

```json
{
  "name": "Running Shoes",
  "description": "Comfortable shoes for daily running",
  "rating": 5,
  "expire_date": "2025-12-31",
  "category": 2,
  "is_available": true,
  "is_exciting": true,
  "free_shipping": true,
  "has_gift": false,
  "is_budget_friendly": false,
  "price": 150,
  "brand": 1,
  "componey": 3,
  "color": 5,
  "gender": 2,
  "age": 1,
  "season": 4,
  "country": 2,
  "tags": [1,2]
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "Running Shoes",
  "description": "Comfortable shoes for daily running",
  "rating": 5,
  "expire_date": "2025-12-31",
  "category": 2,
  "is_available": true,
  "is_exciting": true,
  "free_shipping": true,
  "has_gift": false,
  "is_budget_friendly": false,
  "price": 150,
  "brand": 1,
  "componey": 3,
  "color": 5,
  "gender": 2,
  "age": 1,
  "season": 4,
  "country": 2,
  "tags": [1,2],
  "created_at": "2025-12-01T12:00:00Z",
  "updated_at": "2025-12-01T12:00:00Z"
}
```

---

## Product Detail

**GET /api/products/<id>/**

**Response Example:**

```json
{
  "id": 1,
  "name": "Running Shoes",
  "description": "Comfortable shoes for daily running",
  "rating": 5,
  "expire_date": "2025-12-31",
  "category": 2,
  "is_available": true,
  "is_exciting": true,
  "free_shipping": true,
  "has_gift": false,
  "is_budget_friendly": false,
  "price": 150,
  "brand": 1,
  "componey": 3,
  "color": 5,
  "gender": 2,
  "age": 1,
  "season": 4,
  "country": 2,
  "tags": [1,2],
  "created_at": "2025-12-01T12:00:00Z",
  "updated_at": "2025-12-01T12:00:00Z"
}
```

**PUT / PATCH /api/products/<id>/**

**Request Example (PATCH):**

```json
{
  "price": 120,
  "is_available": false
}
```

**Response Example:**

```json
{
  "id": 1,
  "name": "Running Shoes",
  "description": "Comfortable shoes for daily running",
  "rating": 5,
  "expire_date": "2025-12-31",
  "category": 2,
  "is_available": false,
  "is_exciting": true,
  "free_shipping": true,
  "has_gift": false,
  "is_budget_friendly": false,
  "price": 120,
  "brand": 1,
  "componey": 3,
  "color": 5,
  "gender": 2,
  "age": 1,
  "season": 4,
  "country": 2,
  "tags": [1,2],
  "created_at": "2025-12-01T12:00:00Z",
  "updated_at": "2025-12-01T12:30:00Z"
}
```

**DELETE /api/products/<id>/**

**Response Example:**

```json
{
  "detail": "Product deleted successfully."
}
```

---

## Notes

- Filters support both exact values (`category=1`) and multiple tags (`tags=1,2,3`).  
- Search is performed on `name` and `description` fields (`?search=shoes`).  
- Ordering fields: `price`, `rating`, `created_at` (`?ordering=-price` for descending).  
- All create/update/delete operations require admin privileges.  
- `is_exciting`, `is_available`, `free_shipping`, `has_gift`, `is_budget_friendly` are boolean flags.  

