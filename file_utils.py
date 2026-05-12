import os
from pathlib import Path


def load_env_file(dotenv_path=".env"):
    """Loads environment variables from a .env file.

    Args:
        dotenv_path (str): Path to the .env file.
    """
    path = Path(dotenv_path)
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value




def load_file(file_path):
    """Loads the content of a file.

    Args:
        file_path (str): Path to the file to be loaded.

    Returns:
        str: Content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path, data):
    """Writes data to a file.

    Args:
        file_path (str): Path to the file where data will be written.
        data (str): Data to be written to the file.
    """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(data)
