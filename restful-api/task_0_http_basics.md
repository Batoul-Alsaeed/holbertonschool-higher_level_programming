# 📡 RESTful API - Task 0: Basics of HTTP/HTTPS

## 🔍 HTTP vs HTTPS

| Feature       | HTTP                          | HTTPS                            |
|---------------|-------------------------------|----------------------------------|
| Encryption    | ❌ No encryption               | ✅ Encrypted via SSL/TLS         |
| Port          | 80                            | 443                              |
| Certificate   | Not required                  | Requires SSL certificate         |
| Use Cases     | Public websites, non-sensitive data | Secure websites, logins, payments |

> 🔐 The "S" in HTTPS stands for **Secure**. It protects against eavesdropping and tampering.

---

## 📤 Structure of HTTP Request

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

---

## 📥 Structure of HTTP Response

```
HTTP/1.1 200 OK
Date: Sat, 14 Jun 2025 12:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 305

<html>...page content...</html>
```

> Use browser dev tools → Network tab → Reload → Click on first request → See headers.

---

## 🧾 Common HTTP Methods

| Method   | Description                      | Example Use Case                 |
|----------|----------------------------------|----------------------------------|
| **GET**  | Retrieve data                    | Fetch a webpage or API data      |
| **POST** | Submit data to create a resource | Register a new user              |
| **PUT**  | Update an existing resource      | Update user profile information  |
| **DELETE** | Remove a resource              | Delete a blog post               |

---

## 📊 Common HTTP Status Codes

| Status Code | Description          | Example Scenario                                |
|-------------|----------------------|-------------------------------------------------|
| **200 OK**  | Request succeeded    | Successfully fetched a webpage                  |
| **201 Created** | Resource created | Account registered via form submission          |
| **301 Moved Permanently** | Redirect | Page moved to a new URL                         |
| **404 Not Found** | Resource missing | User requested a non-existent page              |
| **500 Internal Server Error** | Server failed | Server error during request processing         |

---

## 📘 Summary

- **HTTP** is fast but not secure. **HTTPS** is secure and recommended for all modern websites.
- HTTP messages have a clear structure with methods, headers, and response codes.
- Understanding status codes and request methods is essential when consuming or creating APIs.

---

📎 *This task is part of the Holberton RESTful API project - June 2025.*
