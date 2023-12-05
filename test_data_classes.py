# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_data_classes
# # Description: A test collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, created file
# ------------------------------------------------------------------------------------------------- #

import unittest
from processing_classes import Person, Employee

class TestPerson(unittest.TestCase):
    #works
    def test_person_init(self):
        person = Person('sabrina', 'fechtner')
        self.assertEqual("Sabrina", person.first_name)
        self.assertEqual('Fechtner', person.last_name)
    #stalls unless you include the commented out section in processing_classes.py
    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person('123', 'Fechtner')
        with self.assertRaises(ValueError):
            person = Person('Sabrina', '123')
    #works
    def test_person_str(self):
        person = Person("Sabrina", "Fechtner")
        self.assertEqual(str(person), "Sabrina Fechtner")


class TestEmployee(unittest.TestCase):
    #works
    def test_employee_init(self):
        employee = Employee('sabrina', 'fechtner', '2000-01-01', 5)
        self.assertEqual("Sabrina", employee.first_name)
        self.assertEqual('Fechtner', employee.last_name)
        self.assertEqual('2000-01-01', employee.review_date)
        self.assertEqual(5, employee.review_rating)
    #stalls unless you include the commented out section in processing_classes.py
    def test_employee_review_date_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Sabrina", "Fechtner", "invalid_review_date", 5)
    #stalls unless you include the commented out section in processing_classes.py
    def test_employee_review_rating_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Sabrina", "Fechtner", "2000-01-01", 0)
    #works
    def test_employee_str(self):
        employee = Employee("Sabrina", "Fechtner", "2000-01-01", 5)
        self.assertEqual(str(employee), "Sabrina Fechtner has been reviewed on 2000-01-01 with a rating of 5")


if __name__ == "__main__":
    unittest.main()