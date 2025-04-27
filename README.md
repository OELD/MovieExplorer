# Movie Explorer

A fun, full-stack demo app that lets you browse and add movies.

## 📦 Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Vue 3 (via CDN)
- **Mobile:** Android (Kotlin + OkHttp)
- **Database:** SQLite
- **Containerized:** Docker & docker-compose
- **CI:** GitHub Actions

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Make
- Android Studio (optional, for mobile app)

---

## 🔧 Setup & Run

1. **Build and run services**

```bash
make up
```

2. **Seed the database**

```bash
make seed
```

3. **Open in browser**

- Frontend: [http://localhost:8080](http://localhost:8080)
- Backend API: [http://localhost:8000/movies](http://localhost:8000/movies)

---

## 📱 Run Mobile App

- Open `mobile/android-app/` in Android Studio
- Run the app on an emulator (remember: it uses `10.0.2.2` to talk to your host's localhost!)

---

## 📁 Project Structure

```
.
├── backend/              # FastAPI backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/             # Vue3 frontend (CDN)
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── data/                 # SQL schema
│   └── schema.sql
│
├── mobile/android-app/   # Android Kotlin app
│   └── (standard Android project files)
│
├── scripts/              # DB seed scripts
│   └── populate_db.py
│
├── .github/workflows/    # GitHub Actions CI configs
│   └── ci.yml
│
├── docker-compose.yml
├── Makefile
├── README.md
└── LICENSE
```

---

## ⚙️ CI/CD

GitHub Actions runs:

- **Backend:** install deps & smoke-test DB schema.
- **Frontend:** placeholder (CDN-based, no build step).

---

## 📝 License

MIT License © 2025 OELD
