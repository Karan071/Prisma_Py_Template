# FastAPI + Prisma Client Python + PostgreSQL Starter Template

This repository is a starter template for building Python web applications using **FastAPI**, **Prisma Client Python**, and **PostgreSQL**. It includes a pre-configured project structure, database connection setup, and tools for managing migrations and queries.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

---

## Features
- 🚀 **FastAPI**: High-performance Python framework for APIs.
- 🗄️ **Prisma Client Python**: Modern ORM with type-safe database queries.
- 🐘 **PostgreSQL**: Using Docker image.
- 🔧 **Environment Variables**: Simplified configuration with `.env`.
- 📜 **Migrations**: Prisma schema-based database migrations.

---

## Prerequisites

Ensure you have the following installed:
- **Python** (3.8 or higher)
- **PostgreSQL** (Latest version)
- **Node.js** (v16+ for Prisma CLI)

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/Karan071/Starter-template-Prisma-Py.git
cd your-repo
```

### Step 2: Set Up the Python Environment
  Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # mac users
.\venv\Scripts\activate # windows
```

### Step 3: Install the Python dependencies:
```bash
pip install -r requirements.txt
```

### Step 4: Run the docker.yaml file
```bash
  docker compose -f "docker-compose.yaml" up -d --build 
```

### Step 5: Generate the Prisma Client
```Bash
  npx prisma generate
```

### Step 6 : Apply Database Migrations
```Bash
npx prisma migrate dev --name init
```

### Step 7: Run the FastAPI Application
Start the FastAPI development server:
```Bash
uvicorn app.main:app --reload
```

Querying the Database
Use the Prisma Python client for database queries. Example:

python
```Bash
from prisma import Prisma

db = Prisma()
db.connect()

# Create a new post
post = db.post.create(
    data={
        "title": "Hello World",
        "content": "This is a test post.",
    }
)
print(post)

db.disconnect()
```

