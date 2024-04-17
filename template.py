import os

project_structure = [
    ".github/workflows/.gitkeep",
    "api",
    "artifacts/",
    "config/settings.ini",
    "logs/app.log",
    "src/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",
    ".gitignore",
    "dockerfile",
    "main.py",
    "README.md",
    "requirements.txt",
]

# Function to create directories
def create_directories(directories):
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    create_directories(project_structure)
    print("Project structure added to the existing directory!")
