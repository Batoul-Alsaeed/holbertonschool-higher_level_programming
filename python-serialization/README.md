# 📦 Python Serialization Project

Welcome to the **Python Serialization** project from Holberton School by Tuwaiq Academy.
This project explores how to serialize and deserialize data using multiple formats like **JSON**, **Pickle**, **CSV**, **XML**, and how to apply serialization in **network communication**.

---

## 📚 What I Learn

* ✅ Difference between **marshaling** and **serialization**
* ✅ Using Python's built-in modules: `json`, `pickle`, `csv`, and `xml.etree.ElementTree`
* ✅ Converting data between formats (CSV → JSON, dict → XML, etc.)
* ✅ Sending serialized data over a network (client/server)

---

## 🧐 Tasks Overview

### 0️⃣ Basic JSON Serialization

Serialize a Python dictionary to a JSON file and load it back.

```python
serialize_and_save_to_file(data, "data.json")
load_and_deserialize("data.json")
```

---

### 1️⃣ Pickling Custom Classes

Serialize and deserialize a custom Python class using `pickle`.

```python
obj = CustomObject("John", 25, True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
```

---

### 2️⃣ CSV to JSON

Read a CSV file and convert it to JSON format.

```python
convert_csv_to_json("data.csv")
# Output saved as data.json
```

---

### 3️⃣ XML Serialization

Serialize a dictionary into XML and then read it back.

```python
serialize_to_xml(data, "data.xml")
deserialize_from_xml("data.xml")
```

---

### 4️⃣ Networking with Serialization (Advanced)

Client-server app using `socket` to send and receive serialized JSON dictionaries.

```python
start_server()   # runs in a thread
send_data({"name": "Alice", "age": 30})
```

---

## 📁 Project Structure

```
python-serialization/
│
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
├── task_04_net.py
└── README.md
```

---

## 🛠️ Requirements

* Python 3.6+
* Standard libraries only (no external dependencies)

---

## ✅ Author

Project by [Batoul Alsaeed](https://github.com/Batoul-Alsaeed)
Part of Holberton School curriculum.

---

## 📌 Notes

* Use `pickle` **only for internal trusted data** (security risk with external files).
* For network communication or APIs, prefer `JSON`.
* XML is still used in legacy systems and complex data structures.
