# 🚀 Customer Management API (FastAPI)

A simple FastAPI CRUD application for managing customers using an in-memory data store.
This project uses Pydantic models (no dataclasses) and a flat folder structure for simplicity.

# 📁 Project Structure

```
app/
├── main.py          # FastAPI app & routes
├── Customer.py      # Pydantic schema (API + internal model)
├── service.py       # Business logic
├── repo.py          # Data repository (in-memory)
└── __pycache__/     # Ignored

```

# 🛠️ Tech Stack

 - Python 3.9+

 - FastAPI

 - Pydantic

 - Uvicorn

# ⚙️ Setup & Installation

1️⃣ Clone the repository

```

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```

2️⃣ Create a virtual environment

```

python -m venv myenv


```

# Activate it:

### Windows

```

myenv\Scripts\activate

```


### Linux / macOS

```

source myenv/bin/activate

```

3️⃣ Install dependencies

```

pip install fastapi uvicorn

```

4️⃣ Run the application

```

uvicorn app.main:app --reload

```

# 📘 API Documentation (Swagger)

Once running, open:

```

Swagger UI
👉 http://127.0.0.1:8000/docs

ReDoc
👉 http://127.0.0.1:8000/redoc

```

# 📌 Data Model

Customer Schema

```
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true
}

```

# 🔗 API Endpoints

➕ Create Customer

   - POST /customers/

Request Body

```

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true
}

```


Response

```

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true
}

```


###  Status Codes

```

201 Created

```


📥 Get All Customers

```

GET /customers/

```

Response

```

[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "active": true
  }
]

```


🔍 Get Customer by ID

```

GET /customers/{customer_id}

```


Response

```

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true
}

```

Errors

```

404 Customer not found

```

✏️ Update Customer

```

PUT /customers/{customer_id}

```

Request Body

```

{
  "id": 1,
  "name": "John Updated",
  "email": "john.updated@example.com",
  "active": false
}

```

Response

```

{
  "message": "Updated successfully"
}

```

Errors

```
400 ID mismatch

404 Customer not found

```

❌ Delete Customer

```

DELETE /customers/{customer_id}

```

Response

```

{
  "message": "Deleted successfully"
}

```

Errors

```

404 Customer not found

```

## 🧠 Design Notes

- Uses Pydantic models as both schema and internal data object

- No database (data stored in memory)

- Flat project structure for learning & simplicity

- Easily extendable to SQLAlchemy or MongoDB later


