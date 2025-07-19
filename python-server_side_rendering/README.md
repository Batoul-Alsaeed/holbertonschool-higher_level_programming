# Python - Server-Side Rendering with Flask
> ✨by **Batoul Alsaeed**

This mini-project explores how to build server-rendered web pages using **Flask** and **Jinja2**, and how to load dynamic content from **JSON**, **CSV**, and **SQLite** sources.

---

## 🚀 Features

| Task | Description |
|------|-------------|
| `0`  | Generate personalized invitations from a template file using Python string replacement |
| `1`  | Build a Flask app serving static HTML with reusable header/footer templates |
| `2`  | Render dynamic lists from JSON using Jinja loops and conditionals |
| `3`  | Load and filter product data from either a JSON or CSV file using query parameters |
| `4`  | Extend the app to read data from a SQLite database (`products.db`) and display it via Jinja |

---

## 🗂️ Data Sources

- ✅ `items.json`
- ✅ `products.json`
- ✅ `products.csv`
- ✅ `products.db` (SQLite)

---

## Technologies Used

- Python 3
- Flask
- Jinja2
- SQLite
- JSON & CSV modules

---

## 🖥️ How to Run Locally

```bash
# 1. Create and populate the SQLite DB
python3 create_db.py

# 2. Run the Flask server
python3 task_04_db.py

# 3. Visit in your browser
http://localhost:5000/products?source=sql
```

---

## 🧪 Sample URLs

- `/products?source=json`
- `/products?source=csv`
- `/products?source=sql`
- `/products?source=sql&id=2`
- `/products?source=xml` → (shows error)

---
