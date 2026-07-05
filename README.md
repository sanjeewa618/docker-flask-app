# Dockerized Flask Application

A simple Flask web application containerized using Docker. This project demonstrates the basics of Docker, including creating a Docker image and running the application inside a Docker container.

---

## 📌 Project Structure

```
docker-flask-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🚀 Technologies Used

- Python 3.14
- Flask
- Docker

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd docker-flask-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask application

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

## 🐳 Build Docker Image

```bash
docker build -t flask-app .
```

---

## ▶️ Run Docker Container

```bash
docker run -p 5000:5000 flask-app
```

Open:

```
http://localhost:5000
```

---

## 📖 Project Workflow

### Step 1 – Run the Flask Application

```bash
python app.py
```

The application runs locally using Python.

```
Python
   │
   ▼
Flask Application
```

---

### Step 2 – Build the Docker Image

```bash
docker build -t flask-app .
```

```
Project Files
      │
      ▼
 Docker Image
```

---

### Step 3 – Run the Docker Container

```bash
docker run -p 5000:5000 flask-app
```

```
Docker Image
      │
docker run
      ▼
Docker Container
      ▼
Running Web Application
```

The application is now running inside a Docker container.

---

## ✅ Result

- Flask application created successfully.
- Docker image built successfully.
- Docker container running successfully.
- Application accessible via `http://localhost:5000`.

---

## 👨‍💻 Author

**Your Name**