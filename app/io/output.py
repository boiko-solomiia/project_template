import pandas as pd

def output_to_console(text):
    """Output text to the console."""
    print(text)

def write_to_file_builtin(file_path, text):
    """Write data to a file using built-in Python tools."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def write_to_file_pandas(file_path, data):
    """Write data to a file using the pandas library."""
    df = pd.DataFrame({"text": [data]})
    df.to_csv(file_path, index=False)