# ------------------------------------------------------------------------------- #
# Title: Assignment08- Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.4.2023, Modified for A08
# ------------------------------------------------------------------------------- #
import unittest
import tempfile
import json
#import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        self.temp_file.close()

    def test_read_data_from_file(self):
        sample_data = [
            {"FirstName": "DefaultFirstName", "LastName": "DefaultLastName", "Review Date": 1900-01-01, "Review Rating": 3}
                ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        FileProcessor.read_data_from_file(self.temp_file_name, self.employee_data)

        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].gpa, 3.8)

    def test_write_data_to_file(self):
        # Create some sample student objects
        sample_students = [
            data.Student("John", "Doe", 3.5),
            data.Student("Alice", "Smith", 3.8),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_data_to_file(self.temp_file_name, sample_students)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_students))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["GPA"], 3.8)

if __name__ == "__main__":
    unittest.main()
