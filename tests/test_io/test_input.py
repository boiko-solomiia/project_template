import os
import unittest

from app.io.input import read_from_file_builtin, read_from_file_pandas


class TestInputFunctions(unittest.TestCase):

    def test_read_from_file_builtin_correct_text(self):
        with open("test_builtin.txt", "w", encoding="utf-8") as file:
            file.write("Hello builtin")

        result = read_from_file_builtin("test_builtin.txt")
        self.assertEqual(result, "Hello builtin")

        os.remove("test_builtin.txt")

    def test_read_from_file_builtin_empty_file(self):
        with open("empty.txt", "w", encoding="utf-8") as file:
            file.write("")

        result = read_from_file_builtin("empty.txt")
        self.assertEqual(result, "")

        os.remove("empty.txt")

    def test_read_from_file_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin("missing.txt")

    def test_read_from_file_pandas_one_line(self):
        with open("test_pandas_one.csv", "w", encoding="utf-8") as file:
            file.write("Hello pandas")

        result = read_from_file_pandas("test_pandas_one.csv")
        self.assertIn("Hello pandas", result)

        os.remove("test_pandas_one.csv")

    def test_read_from_file_pandas_many_lines(self):
        with open("test_pandas_many.csv", "w", encoding="utf-8") as file:
            file.write("row1\nrow2\nrow3")

        result = read_from_file_pandas("test_pandas_many.csv")
        self.assertIn("row1", result)
        self.assertIn("row2", result)
        self.assertIn("row3", result)

        os.remove("test_pandas_many.csv")

    def test_read_from_file_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas("missing.csv")


if __name__ == "__main__":
    unittest.main()