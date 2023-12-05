# ------------------------------------------------------------------------------- #
# Title: Assignment08- Test Processing Classes Module
# Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# RRoot, 1.5.2030, Created Script
# Sabrina Fechtner, 12.4.2023, Modified for A08
# ------------------------------------------------------------------------------- #
import unittest
import tempfile
import json
from processing_classes import FileProcessor, Employee

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.file_processor = FileProcessor()

    def tearDown(self):
        self.temp_file.close()

    def test_read_data_from_file(self):
        sample_data = [
            {"employee_first_name": "John", "employee_last_name": "Doe", "review_date": "2023-01-01", "review_rating": 3},
            {"employee_first_name": "Alice", "employee_last_name": "Smith", "review_date": "2023-02-01", "review_rating": 4},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)


        loaded_data = self.file_processor.read_data_from_file(self.temp_file_name)

        self.assertEqual(len(loaded_data), len(sample_data))
        self.assertEqual(loaded_data[0].first_name, "John")
        self.assertEqual(loaded_data[1].last_name, "Smith")

    def test_write_data_to_file(self):
        # Create some sample employee objects
        sample_employees = [
            Employee("John", "Doe", "2023-01-01", 3),
            Employee("Alice", "Smith", "2023-02-01", 4),
        ]

        FileProcessor.write_data_to_file(self.temp_file_name, sample_employees)

        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["employee_first_name"], "John")
        self.assertEqual(file_data[1]["employee_last_name"], "Smith")

if __name__ == "__main__":
    unittest.main()
