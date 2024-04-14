import os

project_structure = [
    ".github/workflows/.gitkeep",
    "src/data",
    "notebooks",
    "config/settings.ini",
    "logs/app.log",
    "models/.gitkeep",
    "src/__init__.py",
    "utils/__init__.py",
    ".gitignore",
    "template.py",
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
