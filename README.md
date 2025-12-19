🏗️ mkarchi
mkarchi (make architecture) is a command-line tool that creates project structures from tree-format files. It allows you to define your entire project structure in a simple text file and generate it instantly, including files with pre-written content.
✨ Features

📁 Create directories from tree structure
📄 Create empty files instantly
✍️ Create files with content using intuitive { } syntax
🎯 Preserve indentation automatically (perfect for Python, YAML, etc.)
💬 Support comments in structure files
🚀 Fast and simple - one command to build your entire project

📦 Installation
Option 1: Install from source
bashgit clone https://github.com/yourusername/mkarchi.git
cd mkarchi
pip install -e .
Option 2: Run as module (no installation)
bashgit clone https://github.com/yourusername/mkarchi.git
cd mkarchi
python -m mkarchi apply structure.txt
🚀 Quick Start
1. Create a structure file
Create a file called structure.txt:
my_project/
├── src/
│   ├── main.py{
│   │   def main():
│   │       print("Hello, World!")
│   │   
│   │   if __name__ == "__main__":
│   │       main()
│   │   }
│   └── utils.py{
│   │   def helper():
│   │       return "Helper function"
│   │   }
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
2. Run mkarchi
bashmkarchi apply structure.txt
3. See the magic! ✨
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
📖 Usage
Basic Commands
bash# Create structure from file
mkarchi apply structure.txt

# Show help
mkarchi --help

# Show version
mkarchi --version
Structure File Format
Create Directories
Directories must end with /:
my_folder/
├── subfolder/
└── another_folder/
Create Empty Files
Files without braces are created empty:
my_folder/
├── empty_file.txt
└── config.json
Create Files with Content
Use { } syntax to add content:
my_folder/
├── script.py{
│   print("Hello!")
│   print("This is Python code")
│   }
└── README.md{
    # Title
    Content here
    }
Indentation Preservation
The tool automatically preserves relative indentation:
utils.py{
│   def greet(name):
│       if name:
│           print(f"Hello, {name}!")
│       else:
│           print("Hello, World!")
│   }
Result in utils.py:
pythondef greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
Comments
Use # to add comments in your structure file:
project/
├── src/          # Source code directory
│   └── main.py   # Main entry point
└── tests/        # Test directory
🎯 Use Cases
Quick Prototyping
bash# Create a new Flask project structure in seconds
mkarchi apply flask_template.txt
Template Projects
bash# Share project templates with your team
mkarchi apply team_template.txt
Documentation
bash# Create example project structures for tutorials
mkarchi apply tutorial_structure.txt
Microservices
bash# Set up multiple service structures quickly
mkarchi apply microservice1.txt
mkarchi apply microservice2.txt
🔧 Advanced Examples
Python Project with Tests
python_project/
├── src/
│   ├── __init__.py
│   └── main.py{
│   │   """Main module."""
│   │   
│   │   def main():
│   │       print("Starting application...")
│   │   }
├── tests/
│   ├── __init__.py
│   └── test_main.py{
│   │   import pytest
│   │   from src.main import main
│   │   
│   │   def test_main():
│   │       assert main() is None
│   │   }
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
Web Project Structure
web_project/
├── public/
│   ├── index.html{
│   │   <!DOCTYPE html>
│   │   <html>
│   │   <head>
│   │       <title>My Site</title>
│   │   </head>
│   │   <body>
│   │       <h1>Welcome!</h1>
│   │   </body>
│   │   </html>
│   │   }
│   └── style.css{
│   │   body {
│   │       font-family: Arial, sans-serif;
│   │       margin: 0;
│   │       padding: 20px;
│   │   }
│   │   }
└── src/
    └── app.js{
    │   console.log('App initialized');
    │   }
🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🐛 Issues
Found a bug or have a feature request? Please open an issue on GitHub Issues.
⭐ Show Your Support
If you find this tool useful, please consider giving it a star on GitHub!
📧 Contact

GitHub: @SoufyanRachdi
Email: soufyanrachdiii@gmail.com


Made with ❤️ by Soufyan Rachdi
