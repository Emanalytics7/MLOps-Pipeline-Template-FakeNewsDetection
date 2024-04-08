import os

project_structure = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/utils",
    "tests",
    "api",
    "docker",
]

# Function to create directories
def create_directories(directories):
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    create_directories(project_structure)
    print("Project structure added to the existing directory!")
