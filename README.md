# 🎬 WikiBoxd — NoSQL Movie Platform

## 📌 Overview

**WikiBoxd** is a NoSQL-based web application inspired by platforms like *Letterboxd*, designed for managing and exploring movie-related content.

The project is developed as part of the *Basi di Dati II* course and focuses on modeling and implementing a data-intensive system using **MongoDB**.

The application allows users to interact with a movie catalog and associated data, supporting typical operations found in content management platforms.

---

## 🧠 Dataset

The project is based on the **MovieLens Latest Small dataset**, provided by the GroupLens Research Group:
https://grouplens.org/datasets/movielens/latest/

The dataset includes:

* users (`userId`)
* movies (`movieId`, `title`, `genres`)
* ratings (`userId`, `movieId`, `rating`, `timestamp`)
* tags (`userId`, `movieId`, `tag`, `timestamp`)

To better simulate a real-world scenario, the dataset is extended with additional synthetic data.

---

## 🗄️ Database Design

The system follows a **document-oriented model** using MongoDB.

### Collections

* **Users**
* **Movies**
* **Reviews**
* **Watchlist**
* **Lists**
* **List_Movies**

### Design Approach

* Relationships between collections are handled through referencing
* Selective denormalization is applied when beneficial for performance
* Aggregation pipelines (`$lookup`) are used to combine data across collections

---

## 🔗 Queries & Data Access

The system supports operations that combine data from multiple collections, enabling the construction of composite views and aggregated results.

---

## 🖥️ Application Stack

* **Database:** MongoDB
* **Backend:** Flask (Python)
* **Frontend:** HTML + CSS + Bootstrap
* **Containerization:** Docker Compose
* **Data Processing:** Jupyter Notebook + Python scripts

---

## 📂 Project Structure

```text
WikiBoxd-BD2/
├── app/                  # Flask application
│   ├── app.py
│   └── Dockerfile
├── notebooks/            # Data exploration and prototyping
├── scripts/              # Import, seed, and utility scripts
├── data/                 # Raw and synthetic datasets
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## 🔄 Development Workflow

The project follows a Git-based workflow using issues, branches, pull requests, and reviews, as required by the course.

---

## 🐳 Running WikiBoxd with Docker

### 1️⃣ Build and start the application

From the project root, run:

```bash
docker compose up --build
```

This command starts:

* `mongo` → MongoDB database
* `app` → WikiBoxd Flask application

The application will be available at:

```text
http://localhost:5000
```

---

### 2️⃣ Stop the application

```bash
docker compose down
```

To remove containers and volumes:

```bash
docker compose down -v
```

---
