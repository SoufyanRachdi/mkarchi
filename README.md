# 🏗️ mkarchi

mkarchi (make architecture) is a command-line tool that generates complete project structures from simple tree-format text files.  
Define your entire project architecture — folders, files, and even file contents — in one readable text file, then generate it instantly with a single command.

---

# ✨ Features

- 📁 Create directories from a tree structure  
- 📄 Create empty files automatically  
- ✍️ Create files with content using intuitive `{ }` syntax  
- 🎯 Preserve indentation (perfect for Python, YAML, JSON, etc.)  
- 💬 Support comments in structure files  
- 🚀 Fast & simple — build your whole project in one command  

---

# 📦 Installation

#### ✅ Recommended (via pip)

```bash
pip install mkarchi
```
Option 2: Install from source
```bash
git clone https://github.com/yourusername/mkarchi.git
cd mkarchi
pip install -e .
```
Option 3: Run as module (no installation)
```bash
git clone https://github.com/yourusername/mkarchi.git
cd mkarchi
python -m mkarchi apply structure.txt
```
---

# 🚀 Quick Start
#### 1️⃣ Create a structure file
Create a file called structure.txt:

```text
my_project/
├── src/
│   ├── main.py{
│   │   def main():
│   │       print("Hello, World!")
│   │
│   │   if __name__ == "__main__":
│   │       main()
│   }
│   └── utils.py{
│       def helper():
│           return "Helper function"
│   }
├── tests/
│   └── test_main.py
├── README.md{
│   # My Project
│
│   This is an awesome project!
│   }
└── requirements.txt{
    pytest>=7.0.0
    requests>=2.28.0
}
```
### 2️⃣ Run mkarchi
``` bash
mkarchi apply structure.txt
```
### 3️⃣ See the magic ✨
```text
Copy code
🚀 Creating structure from structure.txt...

📁 Created directory: my_project
📁 Created directory: my_project/src
📄 Created file with content: my_project/src/main.py
📄 Created file with content: my_project/src/utils.py
📁 Created directory: my_project/tests
📄 Created file: my_project/tests/test_main.py
📄 Created file with content: my_project/README.md
📄 Created file with content: my_project/requirements.txt

✅ Architecture created successfully!
```
---

# 📖 Usage
```bash
# Generate structure
mkarchi apply structure.txt

# Help
mkarchi --help

# Version
mkarchi --version
```
---

# 📄 Structure File Format
### 📁 Create Directories
Directories must end with /:

```text
Copy code
my_folder/
├── subfolder/
└── another_folder/
```
### 📄 Create Empty Files
Files without { } are created empty:

```text
my_folder/
├── empty_file.txt
└── config.json
```
### ✍️ Create Files with Content
Use { } to define file content:

```text
script.py{
    print("Hello!")
    print("This is Python code")
}
```
### 🎯 Indentation Preservation
mkarchi automatically preserves indentation:

```text

utils.py{
    def greet(name):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello, World!")
}
```
Result (utils.py):

```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
```
### 💬 Comments Support
Use # for comments in your structure file:

```text
project/
├── src/          # Source code
│   └── main.py   # Entry point
└── tests/        # Tests
```
# 🎯 Use Cases
#### ⚡ Quick Prototyping

#### 📦 Reusable project templates

#### 📘 Documentation & tutorials

#### 🧩 Microservices setup
```bash
Copy code
mkarchi apply service1.txt
mkarchi apply service2.txt
```
---
# 🔧 Advanced Example (Python Project)
```text
python_project/
├── src/
│   ├── __init__.py
│   └── main.py{
│       """Main module."""
│
│       def main():
│           print("Starting application...")
│   }
├── tests/
│   ├── __init__.py
│   └── test_main.py{
│       import pytest
│       from src.main import main
│
│       def test_main():
│           assert main() is None
│   }
├── setup.py{
│   from setuptools import setup, find_packages
│
│   setup(
│       name="my-project",
│       version="0.1.0",
│       packages=find_packages(),
│   )
│   }
└── README.md
```
---
# 🤝 Contributing
Contributions are welcome! 🚀

Fork the repository

Create a feature branch:

```bash
git checkout -b feature/amazing-feature
```
Commit your changes:

```bash
git commit -m "Add amazing feature"
```
Push to your branch:

```bash
git push origin feature/amazing-feature
```
Open a Pull Request

#### 📝 License
This project is licensed under the MIT License.
See the LICENSE file for details.

#### 🐛 Issues & Feedback
Found a bug or have a feature request?
Please open an issue on GitHub Issues.

#### ⭐ Support the Project
If you find mkarchi useful, please consider giving it a ⭐ on GitHub!

---
### ❤️ Made with passion by Soufyan Rachdi
