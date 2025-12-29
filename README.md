<div align="center">

# 🏗️ mkarchi

![mkarchi logo](assets/logo.png)

**Design your architecture once, apply it anywhere**

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/mkarchi?period=total&units=international_system&left_color=black&right_color=green&left_text=downloads)](https://pepy.tech/projects/mkarchi)
[![PyPI version](https://img.shields.io/pypi/v/mkarchi)](https://pypi.org/project/mkarchi/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/SoufyanRachdi/mkarchi?style=social)](https://github.com/SoufyanRachdi/mkarchi)

[Documentation](https://mkarchi.vercel.app/) • [Latest Version](https://mkarchi.vercel.app/version) • [FAQ](https://mkarchi.vercel.app/faq) • [Community](https://mkarchi.vercel.app/community)

</div>

---

## 🌟 What is mkarchi?

**mkarchi** (make architecture) is a powerful command-line tool that generates complete project structures from simple tree-format text files. With v0.1.7, you can also reverse-engineer your existing projects back into mkarchi format — making project scaffolding and documentation effortless.

<div align="center">

![mkarchi diagram](assets/diagram.png)

</div>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 📋 Generation
- 📁 **Create directories** from tree structures
- 📄 **Generate files** with or without content
- ✍️ **Content embedding** using `(begincontenu)` tags
- 🎯 **Indentation preservation** for Python, YAML, JSON
- 💬 **Comments support** in structure files

</td>
<td width="50%">

### 🔄 Reverse Engineering
- 🔄 **Generate mkarchi files** from existing projects
- 🚫 **Smart `.gitignore`** integration (NEW v0.1.7)
- ⚡ **Improved performance** and error handling
- 🚀 **Fast, simple**, and AI-friendly
- 📦 **Reusable templates** for any project

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Installation

```bash
pip install mkarchi
```

<details>
<summary>📦 Alternative Installation Methods</summary>

**Install from source:**
```bash
git clone https://github.com/SoufyanRachdi/mkarchi.git
cd mkarchi
pip install -e .
```

**Run as module (no installation):**
```bash
git clone https://github.com/SoufyanRachdi/mkarchi.git
cd mkarchi
python -m mkarchi apply structure.txt
```

</details>

### Create Your First Project

**1. Create a structure file** (`structure.txt`):

```text
my_project/
├── src/
│   ├── main.py(begincontenu)
│   │   def main():
│   │       print("Hello, World!")
│   │
│   │   if __name__ == "__main__":
│   │       main()
│   (endcontenu)
│   └── utils.py
├── tests/
│   └── test_main.py
├── README.md(begincontenu)
│   # My Project
│
│   This is an awesome project!
│   (endcontenu)
└── requirements.txt(begincontenu)
    pytest>=7.0.0
    requests>=2.28.0
(endcontenu)
```

**2. Apply the structure:**

```bash
mkarchi apply structure.txt
```

**3. See the magic ✨**

```
🚀 Creating structure from structure.txt...

📁 Created directory: my_project
📁 Created directory: my_project/src
📄 Created file with content: my_project/src/main.py
📄 Created file: my_project/src/utils.py
📁 Created directory: my_project/tests
📄 Created file: my_project/tests/test_main.py
📄 Created file with content: my_project/README.md
📄 Created file with content: my_project/requirements.txt

✅ Architecture created successfully!
```

---

## 📖 Commands

```bash
# Apply a structure file to create project
mkarchi apply structure.txt

# Generate structure file from current directory
mkarchi give

# Generate without file contents
mkarchi give -c

# Save to custom file
mkarchi give myproject.txt

# Get help
mkarchi --help

# Check version
mkarchi --version
```

---

## 🔄 Reverse Engineering with `mkarchi give`

Generate mkarchi syntax from your existing project structure.

### Default Behavior

```bash
mkarchi give
```

✅ Generates `structure.txt`  
✅ Includes file contents  
✅ Respects `.gitignore` automatically  

### Without File Contents

```bash
mkarchi give -c
```

### Custom Output File

```bash
mkarchi give -c myproject.txt
```

### 🚫 Smart `.gitignore` Integration (v0.1.7)

mkarchi automatically reads your `.gitignore` and excludes:
- `node_modules/`, `venv/`, `__pycache__/`
- `.git/` directories
- Build artifacts and cache files
- Binary files and dependencies

**Example `.gitignore`:**
```
node_modules/
*.pyc
__pycache__/
.env
```

Running `mkarchi give` automatically skips all these files! 🎉

---

## 📝 Structure File Syntax

### Directories
Directories must end with `/`:

```text
my_folder/
├── subfolder/
└── another_folder/
```

### Empty Files
Files without content tags are created empty:

```text
my_folder/
├── empty_file.txt
└── config.json
```

### Files with Content
Use `(begincontenu)` and `(endcontenu)`:

```text
script.py(begincontenu)
    def hello():
        print("Hello, World!")
(endcontenu)
```

### Indentation Preservation
Indentation is automatically preserved:

```text
utils.py(begincontenu)
    def greet(name):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello, World!")
(endcontenu)
```

**Result (`utils.py`):**
```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
```

### Comments
Use `#` for comments:

```text
project/
├── src/          # Source code
│   └── main.py   # Entry point
└── tests/        # Tests
```

---

## 🎯 Use Cases

<table>
<tr>
<td width="33%">

### ⚡ Rapid Scaffolding
Spin up new projects in seconds with predefined templates.

</td>
<td width="33%">

### 🤖 AI Integration
Perfect for AI-generated project structures and code scaffolding.

</td>
<td width="33%">

### 📦 Reusable Templates
Create once, reuse everywhere. Share templates with your team.

</td>
</tr>
<tr>
<td width="33%">

### 🧩 Microservices
Set up multiple services with consistent structure:
```bash
mkarchi apply service1.txt
mkarchi apply service2.txt
```

</td>
<td width="33%">

### 📘 Documentation
Generate clean project documentation:
```bash
mkarchi give docs.txt
```

</td>
<td width="33%">

### 🎓 Tutorials
Create step-by-step project structures for teaching and learning.

</td>
</tr>
</table>

---

## 🔧 Advanced Example: Python Project

```text
python_project/
├── src/
│   ├── __init__.py
│   ├── main.py(begincontenu)
│   │   """Main application module."""
│   │
│   │   def main():
│   │       print("Starting application...")
│   │       return 0
│   │
│   │   if __name__ == "__main__":
│   │       main()
│   (endcontenu)
│   └── config.py(begincontenu)
│       """Configuration module."""
│   
│       DEBUG = True
│       VERSION = "0.1.0"
│   (endcontenu)
├── tests/
│   ├── __init__.py
│   └── test_main.py(begincontenu)
│       import pytest
│       from src.main import main
│
│       def test_main():
│           """Test main function."""
│           assert main() == 0
│   (endcontenu)
├── .gitignore(begincontenu)
│   __pycache__/
│   *.pyc
│   .pytest_cache/
│   venv/
│   (endcontenu)
├── setup.py(begincontenu)
│   from setuptools import setup, find_packages
│
│   setup(
│       name="my-project",
│       version="0.1.0",
│       packages=find_packages(),
│       install_requires=[
│           "pytest>=7.0.0",
│       ],
│   )
│   (endcontenu)
└── README.md(begincontenu)
    # Python Project
    
    A well-structured Python project template.
(endcontenu)
```

---

## 🆕 What's New in v0.1.7?

<table>
<tr>
<td width="33%" align="center">

### 🚫 `.gitignore` Support
Automatically respects `.gitignore` patterns

</td>
<td width="33%" align="center">

### ⚡ Performance Boost
Faster processing and optimized traversal

</td>
<td width="33%" align="center">

### 🐛 Bug Fixes
Enhanced error handling and Unicode support

</td>
</tr>
</table>

**[View full changelog →](https://mkarchi.vercel.app/version)**

**[Learn more about v0.1.7 →](https://mkarchi.vercel.app/learn/0.1.7)**

---

## 📚 Documentation & Resources

<div align="center">

| Resource | Description |
|----------|-------------|
| [📖 Documentation](https://mkarchi.vercel.app/) | Complete guide and tutorials |
| [🔄 Version History](https://mkarchi.vercel.app/version) | All releases and updates |
| [📘 v0.1.7 Guide](https://mkarchi.vercel.app/learn/0.1.7) | Latest version features |
| [📗 v0.1.6 Guide](https://mkarchi.vercel.app/learn/0.1.6) | Previous version features |
| [❓ FAQ](https://mkarchi.vercel.app/faq) | Frequently asked questions |
| [👥 Community](https://mkarchi.vercel.app/community) | Join the community |
| [📧 Contact](https://mkarchi.vercel.app/contact) | Get in touch |

</div>

---

## 🤝 Contributing

Contributions are welcome! We appreciate your help in making mkarchi better.

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🐛 Issues & Support

Found a bug or have a feature request?

- 🐛 [Report an issue](https://github.com/SoufyanRachdi/mkarchi/issues)
- 💬 [Join our community](https://mkarchi.vercel.app/community)
- 📧 [Contact us](https://mkarchi.vercel.app/contact)

---

## ⭐ Star Us!

If you find **mkarchi** useful, please consider giving it a ⭐ on [GitHub](https://github.com/SoufyanRachdi/mkarchi)!

---

<div align="center">

### Made with ❤️ by [Soufyan Rachdi](https://github.com/SoufyanRachdi)

[![GitHub](https://img.shields.io/badge/GitHub-SoufyanRachdi-black?logo=github)](https://github.com/SoufyanRachdi)
[![Website](https://img.shields.io/badge/Website-mkarchi-blue)](https://mkarchi.vercel.app/)

**[Documentation](https://mkarchi.vercel.app/)** • **[Community](https://mkarchi.vercel.app/community)** • **[Contact](https://mkarchi.vercel.app/contact)**

</div>
