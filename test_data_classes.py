# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_data_classes
# # Description: A test collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, created file
# ------------------------------------------------------------------------------------------------- #

import unittest
from processing_classes import Person, Employee


# Define Classes
class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person=Person('sabrina', 'fechtner')
        self.assertEqual("Sabrina", person.first_name)
        self.assertEqual('Fechtner', person.last_name)

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee = Employee('sabrina', 'fechtner','2000-01-01',5)
        self.assertEqual("Sabrina", employee.first_name)
        self.assertEqual('Fechtner', employee.last_name)
        self.assertEqual('2000-01-01', employee.review_date)
        self.assertEqual(5, employee.review_rating)


if __name__ == "__main__":
    unittest.main()
