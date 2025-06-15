# RESTful API Project – Holberton School by Tuwaiq Academy

A hands-on project to explore RESTful API principles using Python, from raw HTTP interactions to secure, token-based authentication with Flask.

---

## 📌 Tasks Overview

| Task | Title                         | Description                          |
|------|-------------------------------|--------------------------------------|
| 0    | HTTP/HTTPS Basics             | Understand request/response flow and status codes. |
| 1    | curl API Requests             | Send GET/POST requests from the CLI. |
| 2    | Python API Interaction        | Use `requests` to fetch and save JSON data. |
| 3    | Simple API with `http.server` | Serve endpoints with plain Python.   |
| 4    | Flask API                     | Create dynamic endpoints with Flask. |
| 5    | API Security & Auth           | Add Basic Auth + JWT with role checks. |

---

## ⚙️ How to Run

### Task 2:
```bash
python3 main_02_requests.py
```

### Task 3:
```bash
python3 task_03_http_server.py
```

### Task 4:
```bash
flask --app task_04_flask.py run
```

### Task 5:
```bash
flask --app task_05_basic_security.py run
```

---

## 🔐 Highlights (Task 5)
- Passwords hashed with Werkzeug.
- JWT tokens issued on login.
- Role-based route protection (`/admin-only`).

---

✅ All tasks tested and completed successfully.

📁 Repo: `holbertonschool-higher_level_programming/restful-api`  
🎓 Part of the Holberton School curriculum – RESTful API module
by Batoul Alsaeed ♥ 
