from sys import path as python_path
from os import path, getcwd

def init_context():
    python_path.insert(0, path.abspath(path.join(path.dirname(__file__), "..")))