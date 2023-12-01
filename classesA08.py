import json
from datetime import date, datetime

FILE_NAME: str = "EmployeeRatings.json"
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
employees: list = []  # a table of employee data
menu_choice = ''

# Define Classes
class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name.capitalize()

    @first_name.setter
    def first_name(self, value):
        if value.isalpha():
            self._first_name = value
        else:
            raise ValueError("The first name cannot be alphanumeric. Please re-enter the first name.")

    @property
    def last_name(self) -> str:
        return self._last_name.capitalize()

    @last_name.setter
    def last_name(self, value):
        if value.isalpha():
            self._last_name = value
        else:
            raise ValueError("The last name cannot be alphanumeric. Please re-enter the last name.")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    def __init__(self, employee_first_name: str, employee_last_name: str, review_date: str, review_rating: int) -> None:
        super().__init__(first_name=employee_first_name, last_name=employee_last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self) -> str:
        return self._review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            self._review_date = value
        except ValueError:
            raise ValueError("Please enter review date as YYYY-MM-DD")

    @property
    def review_rating(self) -> int:
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        try:
            value = int(value)
            if value in {1, 2, 3, 4, 5}:
                self._review_rating = value
            else:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError as e:
            print(f"Error setting rating: {e}")

    def __str__(self) -> str:
        return f"{super().__str__()} has been reviewed on {self.review_date} with a rating of {self.review_rating}"