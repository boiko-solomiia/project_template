from app.io.input import (
    input_from_console,
    read_from_file_builtin,
    read_from_file_pandas,
)
from app.io.output import output_to_console, write_to_file_builtin

def main():
    console_text = input_from_console()
    builtin_text = read_from_file_builtin("data/input.txt")
    pandas_text = read_from_file_pandas("data/input.csv")

    output_to_console("Text from console")
    output_to_console(console_text)

    output_to_console("\nText from file (built-in Python)")
    output_to_console(builtin_text)

    output_to_console("\nText from file (pandas)")
    output_to_console(pandas_text)

    result_text = (
        "Text from console\n"
        f"{console_text}\n\n"
        "Text from file (built-in Python)\n"
        f"{builtin_text}\n\n"
        "Text from file (pandas)\n"
        f"{pandas_text}\n"
    )

    write_to_file_builtin("data/output.txt", result_text)


if __name__ == '__main__':
    main()
