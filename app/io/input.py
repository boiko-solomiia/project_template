import pandas as pd

def input_from_console():
    """Read text input from the console."""
    return input("Enter text from console: ")

def read_from_file_builtin(file_path):
    """Read data from a file using built-in Python tools."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_from_file_pandas(file_path):
    """Read data from a file using the pandas library."""
    df = pd.read_csv(file_path)
    return df.to_string(index=False)