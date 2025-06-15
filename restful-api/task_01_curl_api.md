# 🧰 RESTful API - Task 1: Consume data from an API using curl

## 🎯 Objective

- Install and verify `curl`.
- Use curl to fetch and post data from/to a REST API.
- Use headers and HTTP methods (GET, POST) via command line.
- Understand API responses and status codes.

---

## ✅ Step-by-Step Instructions

### 1. Check curl installation
```bash
curl --version
```

---

### 2. Fetch HTML content from a webpage
```bash
curl http://example.com
```

---

### 3. Fetch posts from a public API (GET)
```bash
curl https://jsonplaceholder.typicode.com/posts
```
Example response (truncated):
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere...",
    "body": "quia et suscipit..."
  }
]
```

---

### 4. Fetch only response headers (HEAD)
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
Example output:
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: max-age=43200
```

---

### 5. Make a POST request
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
Simulated response:
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

---

## 💡 Tips

- Use `-X` to specify HTTP methods like `POST`, `PUT`, `DELETE`.
- Use `-d` to send data with `POST`.
- Use `-I` to fetch only headers.
- Pipe the output through `jq` for readability:
```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```

---

## 📘 Summary

| Action | Command |
|--------|---------|
| Check curl version | `curl --version` |
| Fetch webpage | `curl http://example.com` |
| GET API data | `curl https://jsonplaceholder.typicode.com/posts` |
| Get headers only | `curl -I ...` |
| Send POST request | `curl -X POST -d ...` |

---

📎 *Part of the Holberton RESTful API Project – Task 1 – June 2025*
