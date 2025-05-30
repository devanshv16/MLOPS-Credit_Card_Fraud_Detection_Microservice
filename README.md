# 🚀 Credit Card Fraud Detection Microservice

[![CI](https://github.com/devanshv16/MLOPS-Credit_Card_Fraud_Detection_Microservice/actions/workflows/ci.yml/badge.svg)](https://github.com/devanshv16/MLOPS-Credit_Card_Fraud_Detection_Microservice/actions/workflows/ci.yml)

[![CD](https://github.com/devanshv16/MLOPS-Credit_Card_Fraud_Detection_Microservice/actions/workflows/cd.yml/badge.svg)](https://github.com/devanshv16/MLOPS-Credit_Card_Fraud_Detection_Microservice/actions/workflows/cd.yml)

---

## 📝 Overview

This project is a **containerized microservice** that predicts fraudulent transactions in credit card data using a trained **scikit-learn** machine learning model.  
The application exposes a **FastAPI** web service, fully automated with **CI/CD** via GitHub Actions and deployed as a Docker image to Docker Hub.

---

## 🛠️ Tech Stack

- **FastAPI** – RESTful API framework  
- **scikit-learn** – for building the ML model  
- **pandas & numpy** – data manipulation  
- **joblib** – model serialization  
- **pytest** – unit testing  
- **Docker** – containerization  
- **GitHub Actions** – CI/CD automation  
- **Docker Hub** – hosting Docker images  

---

## 🔄 CI/CD Workflows

### ✅ Continuous Integration (CI)

- Runs on **pushes** and **pull requests** to `main`  
- Installs Python dependencies  
- Runs automated tests with `pytest`  
- Reports test and linting results  

### 🚀 Continuous Deployment (CD)

- Runs on **pushes** to `main`  
- Builds the Docker image for the FastAPI microservice  
- Tags the image  
- Pushes it to Docker Hub  

---

## 🚀 Getting Started

### ⚙️ Prerequisites

- **Python 3.12+**  
- **Docker** installed  
- **GitHub & Docker Hub accounts** (for CD)

---

### 💻 1️⃣ Clone the Repository

```bash
git clone https://github.com/devanshv16/MLOPS-Credit_Card_Fraud_Detection_Microservice.git
cd MLOPS-Credit_Card_Fraud_Detection_Microservice
```

### 🐍 2️⃣ Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate    # On Windows
```

### 📦 3️⃣ Install Python Dependencies

```bash
make install
```

### 🧪 4️⃣ Run the Tests

```bash
make test
```

### 🚀 5️⃣ Run the Application Locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🐳 Running with Docker

### 🏗️ 1️⃣ Build the Docker Image

```bash
docker build -t fraud-detection-api .
```

### 🚀 2️⃣ Run the Docker Container

```bash
docker run -p 8000:8000 fraud-detection-api
```

## 🔍 API Usage

### 📥 Example Request Body

```
{
  "features": [-1.99658302, -0.69424232, -0.04407492, ...]
}
```

### 📤 Example Response

```
{
  "prediction": 0,
  "fraud_probability": 0.1234,
  "status": "Not Fraud"
}
```



