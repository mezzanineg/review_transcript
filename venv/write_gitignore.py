gitignore_content = """# Ambienti virtuali
venv/
.env

# File compilati da Python
__pycache__/
*.py[cod]
*.so

# File di log
*.log

# File di sistema
.DS_Store
Thumbs.db

# VS Code
.vscode/

# Cartella static
static/
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)

print(".gitignore generato correttamente.")
