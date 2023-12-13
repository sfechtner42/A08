# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Data_classes
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, modified to only show, class (person, employee)
# ------------------------------------------------------------------------------------------------- #

from datetime import datetime

# Define Data Classes
class Person:
    """
    A class representing person data.
    Properties:
        -first_name(str): the person's first name
        -last_name(str): the person's last name
    ChangeLog:
        -RRoot, 1.1.2030: Created class
        -Sabrina Fechtner, 12.1.2023 added exception handling
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name.capitalize()


    @first_name.setter
    def first_name(self, value):
        while True:
            if value.isalpha():
                self._first_name = value
                break
            else:
                # value = input("The first name cannot be alphanumeric. Please re-enter the first name: ")
                raise ValueError("Invalid entry First Name")

    @property
    def last_name(self) -> str:
        return self._last_name.capitalize()

    @last_name.setter
    def last_name(self, value):
        while True:
            if value.isalpha():
                self._last_name = value
                break
            else:
                #value = input("Invalid input. The last name cannot be alphanumeric. Please re-enter the last name: ")
                raise ValueError("Invalid entry Last Name")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    """
    A class representing person data.
    Properties:
        -first_name(str): the person's first name
        -last_name(str): the person's last name
    ChangeLog:
        -RRoot, 1.1.2030: Created class
        -Sabrina Fechtner, 12.1.2023 added exception handling
    """

    def __init__(self, employee_first_name: str, employee_last_name: str, review_date: str = None,
                 review_rating: int = None) -> None:
        super().__init__(first_name=employee_first_name, last_name=employee_last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self) -> str:
        return self._review_date

    @review_date.setter
    def review_date(self, value: str):
        while True:
            try:
                if datetime.strptime(value, "%Y-%m-%d"):
                    self._review_date = value
                    break
            except ValueError:
                # value = input("Invalid date format. Please enter a valid review date in the format YYYY-MM-DD: ")
                raise ValueError("Invalid date format")

    @property
    def review_rating(self) -> int:
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value):
        while True:
            try:
                input_value = int(value)
                if input_value in {1, 2, 3, 4, 5}:
                    self._review_rating = input_value
                    break
                else:
                    raise ValueError("Rating must be between 1 and 5.")
            except ValueError:
                # value = input("Invalid input. Rating must be in between 1-5. Please re-enter the rating: ")
                raise ValueError("Invalid review rating") from None

    def __str__(self) -> str:
        return f"{super().__str__()} has been reviewed on {self.review_date} with a rating of {self.review_rating}"

