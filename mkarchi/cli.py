import os
import sys
import re

def parse_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    stack = []
    
    for line in lines:
        if not line.strip():
            continue
        
        tree_match = re.search(r'[├└]', line)
        
        if tree_match:
            indent = tree_match.start()
            if indent == 0:
                level = 0
            else:
                level = (indent // 4)
            
            name_match = re.search(r'[├└]\s*─+\s*(.+)', line)
            if name_match:
                name = name_match.group(1).strip()
            else:
                continue
        else:
            level = 0
            name = line.strip()
        
        is_dir = name.endswith("/")
        name = name.rstrip("/")
        
        stack = stack[:level + 1]
        stack.append(name)
        path = os.path.join(*stack)
        
        if is_dir:
            os.makedirs(path, exist_ok=True)
            print(f"📁 Created directory: {path}")
        else:
            dir_path = os.path.dirname(path)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            with open(path, "a"):
                pass
            print(f"📄 Created file: {path}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "apply":
        print("Usage: mkarchi apply structure.txt")
        sys.exit(1)
    
    structure_file = sys.argv[2]
    
    if not os.path.exists(structure_file):
        print(f"❌ File not found: {structure_file}")
        sys.exit(1)
    
    print(f"🚀 Creating structure from {structure_file}...\n")
    parse_tree(structure_file)
    print("\n✅ Architecture created successfully!")

if __name__ == "__main__":
    main()
