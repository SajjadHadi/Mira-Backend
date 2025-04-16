![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)
![Pycharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![HuggingFace](https://img.shields.io/badge/-HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black)

# 🧠 Mental Disorder Detection API

A **FastAPI** backend for detecting mental disorders using a fine-tuned language model. It provides secure user authentication and mental disorder predictions from user-submitted statements, storing all data in a **MySQL** database. Built with **Docker** and optimized for **GPU-accelerated inference** via **NVIDIA CUDA**.

Explore the models compatible with this project in my [HuggingFace repository](https://huggingface.co/sajjadhadi).

---

## 🚀 Features

- 🔐 **Authentication**: Secure registration and login with JWT tokens.
- 📈 **Prediction**: Predict mental disorders based on user statements at `/llm/predict`.
- 📜 **Statement History**: View past predictions per user with `/llm/statements`.
- 🗃️ **Persistent Storage**: Uses MySQL with `users` and `statements` tables.
- 🐳 **Containerized**: Fully Dockerized for easy deployment.

---

## ⚙️ Setup Guide

### ✅ Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose
- An NVIDIA GPU (for LLM inference)
- A Hugging Face account (for model access)
- Git

---

### 🛠️ Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mdd-backend.git
cd mdd-backend
```

#### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
APP_PORT=8000

# MySQL
MYSQL_USER=mdd_user
MYSQL_PASSWORD=mdd_password
MYSQL_DATABASE=mdd_db
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_ROOT_PASSWORD=root_password

# Hugging Face / Model
HF_TOKEN=your_huggingface_token
BASE_MODEL=Qwen/Qwen2.5-0.5B
FINE_TUNED_MODEL=sajjadhadi/Mental-Disorder-Detection-Qwen2.5-0.5B-v1

# Auth
JWT_SECRET=your_jwt_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

🔒 Make sure `MYSQL_HOST` is set to `mysql` to match the Docker service name.

#### 3. Build and Run the Project

```bash
docker-compose up --build
```

- FastAPI will be available at: [http://localhost:8000](http://localhost:8000)
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Verify Setup

To check if the database and tables are created:

```bash
docker exec -it mdd-backend_mysql_1 mysql -u mdd_user -p mdd_db -e "SHOW TABLES;"
```

Expected output:

```
+-------------------+
| Tables_in_mdd_db  |
+-------------------+
| alembic_version   |
| statements        |
| users             |
+-------------------+
```

---

## 📡 API Usage

### 🔐 Register

```http
POST /auth/register
Content-Type: application/json

{
  "username": "user",
  "password": "pass"
}
```

### 🔑 Login

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user&password=pass
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 🧠 Predict Disorder

```http
POST /llm/predict
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "statement": "I feel anxious and tired"
}
```

### 📜 Get Statements (Paginated)

```http
GET /llm/statements?page=1&per_page=10
Authorization: Bearer <JWT_TOKEN>
```

---

## ⚠️ Notes

- Make sure NVIDIA drivers are installed to enable GPU support.
- To reset the database:

```bash
docker-compose down -v
```

---

## 📬 Contact

For issues or feature requests, feel free to open an issue on the GitHub repository.
