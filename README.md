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

#### 🟢 Sample input (non-fraud):

```
{
  "features": [-1.996583023457193, -0.6942423209592997, -0.04407492457044802, 1.6727734992241512, 0.973365514375461, -0.245116583542522, 0.34706794516190337, 0.19367893831762997, 0.0826372794108694, 0.33112778320993075, 0.08338554524255039, -0.540407035731003, -0.6182957177945313, -0.9960989219768981, -0.3246101863270036, 1.6040138389062166, -0.5368328685192514, 0.24486345402090123, 0.030769932602201018, 0.4962820266510568, 0.3261180160164486, -0.024923364961491876, 0.38285443833968436, -0.17691133433749112, 0.1105069205607409, 0.24658544296942114, -0.3921704315485548, 0.33089162264871697, -0.06378115069750527, 0.24496426337017338]
}
```
#### ✅ Actual class: 0

#### 🔴 Sample input (fraud):
```
{
  "features": [-1.9880335064229064, -1.1804949993102363, 1.182090047722563, -1.0617300869716224, 2.8236466837005083, -0.3783300250128723, -1.0707639267914904, -2.051091174150703, 1.1651997398363183, -2.5214029040986268, -2.5460601633856528, 3.1370608012117063, -2.9022302309609254, -0.5980491690305911, -4.474526340615316, 0.4257816967283722, -1.3018492707953606, -3.332081883544079, -0.020070359338237996, 0.5122060101961796, 0.16462143239107585, 0.7041747700338853, -0.048297305735367994, -0.7449823410376103, 0.5286886995039123, 0.08540402550199126, 0.3687891918240997, 0.6469881991317432, -0.43406055922163245, -0.35322939296682354]
}
```
####⚠️ Actual class: 1



### 📤 Example Response

```
{
  "prediction": 0,
  "fraud_probability": 0.1234,
  "status": "Not Fraud"
}
```



