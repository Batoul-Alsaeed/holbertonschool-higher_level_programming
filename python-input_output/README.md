# Python - Input/Output

This project focuses on practicing file handling in Python and understanding basic serialization (JSON). You will learn how to read/write files, append content, and convert between Python objects and JSON format.

## 📚 What I learned:

- Opening, reading, writing, and appending to files
- Using `with` statement for file handling
- Reading files line by line
- Working with command-line arguments
- Converting Python data to JSON and back
- Serializing and deserializing Python objects
- Creating Pascal's Triangle
- Parsing logs from stdin

## 🧠 Key Concepts

- `open()`, `read()`, `write()`, `readlines()`
- `with` statement for safe file usage
- `json.dumps()`, `json.loads()`, `json.dump()`, `json.load()`
- `sys.argv` and `sys.stdin`
- Object-to-JSON conversion via `__dict__`

## 📁 Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Read and print a text file |
| `1-write_file.py` | Write text to a file |
| `2-append_write.py` | Append text to a file |
| `3-to_json_string.py` | Convert object to JSON string |
| `4-from_json_string.py` | Convert JSON string to object |
| `5-save_to_json_file.py` | Save object to file as JSON |
| `6-load_from_json_file.py` | Load object from JSON file |
| `7-add_item.py` | Save arguments to file (with load/save logic) |
| `8-class_to_json.py` | Convert class attributes to dict |
| `9-student.py` | Student class with serialization |
| `10-student.py` | Student class with selective serialization |
| `11-student.py` | Student class with reloading from JSON |
| `12-pascal_triangle.py` | Generate Pascal's Triangle |
| `100-append_after.py` | Insert text after matching line in file |
| `101-stats.py` | Parse log input from stdin and print stats |

## 🧪 How to run

```bash
chmod +x [main_file].py
./[main_file].py
```

Or redirect input to test:

```bash
cat log.txt | ./101-stats.py
```

## ✅ Requirements

- Python 3.8+
- No external modules allowed
- Followed PEP8 style guide
- Each script is executable and well documented

## ✍️ Author

> Written with ❤️ by Batoul Alsaeed
