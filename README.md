Finance Dashboard Backend

Overview

This project is a backend system built for a finance dashboard application. It allows users to manage financial records such as income and expenses, while enforcing role-based access control.

The system is designed to demonstrate backend fundamentals including API design, authentication, authorization, data modeling, and aggregation logic.


Features

Authentication & Security

* JWT-based authentication
* Secure password hashing using `pbkdf2_sha256`
* Swagger UI login (Authorize button)

User & Role Management

* Create users with roles:

  * Admin → Full access
  * Analyst → Read + analytics
  * Viewer → Read-only
* Role-based access control enforced at API level

Financial Records

* Create, read financial records
* Supports:

  * Amount
  * Type (income / expense)
  * Category
  * Date
  * Notes

Dashboard APIs

* Total income
* Total expenses
* Net balance


Tech Stack

* FastAPI (Backend framework)
* SQLAlchemy (ORM)
* SQLite (Database)
* JWT (python-jose) (Authentication)
* Passlib (Password hashing)


Project Structure

```
finance-backend/
│
├── security.py          # JWT logic
├── crud.py              # Database operations
├── database.py          # DB setup
├── dependencies.py      # Auth & role checks
├── models.py            # DB models
├── schemas.py           # Pydantic schemas
├── main.py              # App entry point
│
└── routers/
    ├── auth.py          # Login API
    ├── user.py          # User APIs
    ├── records.py       # Financial records
    └── dashboard.py     # Summary APIs
```

Setup Instructions

1. Clone the repository

```
git clone <your-repo-link>
cd finance-backend
```

2. Create virtual environment

```
python -m venv finance
finance\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the server

```
uvicorn main:app --reload
```

API Documentation

Once the server is running:

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Authentication Flow (Swagger)

1. Create a user (`/users`)
2. Click Authorize 
3. Enter:
   * username
   * password
4. Click Authorize
5. Access protected APIs

Example Usage

Create User

```json
{
  "username": "naga",
  "password": "naga@123",
  "role": "admin"
}
```

Login

Use Swagger Authorize button

 Assumptions

* Authentication is simplified using JWT
* SQLite is used for ease of setup
* No frontend included
* No refresh tokens (basic auth flow)


Design Decisions

* Used **role-based access control** via FastAPI dependencies
* Separated concerns into:

  * routers
  * services (crud)
  * security layer
* Chose pbkdf2 over bcrypt due to compatibility stability
* Designed APIs for clarity and maintainability


Possible Improvements

* Pagination & filtering
* Refresh tokens
* Soft delete support
* Deployment (Render / Railway)
* Unit testing

Conclusion

This project focuses on building a clean, maintainable backend with proper authentication, authorization, and financial data handling. The goal was to prioritize clarity, correctness, and structured design over unnecessary complexity.
