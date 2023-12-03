# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_data_classes
# # Description: A test collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, created file
# ------------------------------------------------------------------------------------------------- #

import unittest
from processing_classes import Person


# Define Classes
class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person=Person('Sabrina', 'Fechtner')
        self.assertEqual("Sabrina", person.first_name)
        self.assertEqual('Fechtner', person.last_name)



if __name__ == "__main__":
    unittest.main()
