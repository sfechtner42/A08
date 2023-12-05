# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Assigment 8
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.5.2023, Amended for A08
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for valid employee data
        with patch('builtins.input', side_effect=['John', 'Doe', '2000-01-01', '5']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Doe')
            self.assertEqual(self.employee_data[0].review_date, '2000-01-01')
            self.assertEqual(self.employee_data[0].review_rating, 5)

        # Simulate user input for invalid employee data
        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid', '6']):
            with self.assertRaises(StopIteration):
                IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()
