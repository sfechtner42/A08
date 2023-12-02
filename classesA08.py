import json
from datetime import date, datetime
from typing import TextIO, List

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
    """
    A class representing person data
    Properites:
        -first_name(str): the person's first name
        -last_name(str): the person's last name
    ChangeLog
        -RRoot, 1.1.2030: Created class
        -Sabrina Fechtner, 11.30.2023 added exception handling
    """

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
    """
    A class representing employee data.

    Properties:
        -first_name(str):The employee's first name
        -last_name(str): The employee's last name
        -review_date(str): the date of the employee review
        -review_rating(int): the review employee rating (1-5)
    ChangeLog:
        -RRoot, 1.1.2030: Created the class
        -Sabrina Fechtner, 11.30.2023: Added Exceptions
    """

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


# File Processing Functions
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Sabrina Fechtner 12.1.2023 Incorporated Class into A08
    """

    @staticmethod
    def read_data_from_file(file_name: str) -> List[Employee]:
        """ This function reads previous JSON file with employee data

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated Function

        :param file_name: string data with the name of the file to read from
        :return: employee data as a list
        """
        file: TextIO = None
        json_data = []
        employees: list[Employee] = []
        employee_type: object
        employee_data: list
        try:
            with open(file_name, "r") as file:
                employee_data = json.load(file)
                print("Data successfully loaded from the file.")
            for row in employee_data:
                employee = Employee(row["first_name"],
                                    row["last_name"],
                                    row["review_date"],
                                    row["review_rating"]
                                    )
                employees.append(employee)

        except FileNotFoundError:
            print("File not found, creating it...")
            employee_object = employee_type()
            employee_object.first_name = "DefaultFirstName"
            employee_object.last_name = "DefaultLastName"
            employee_object.review_date = "1900-01-01"
            employee_object.review_rating = 3
            with open(file_name, "w") as file:
                json.dump(employee_object, file)
            print("File created successfully.")

        except json.JSONDecodeError as e:
            print(f"Invalid JSON file: {e}. Resetting it...")
            # Resetting employee_data with an empty list
            employee_data = []
            with open(file_name, "w") as file:
                json.dump(employee_data, file)
            print("File reset successfully.")

        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")

        return employees

    @staticmethod
    def write_data_to_file(file_name: str, employee_data: list) -> list[Employee]:
        """ This function writes employee and review data to JSON file

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated Function
        Sabrina Fechtner, 11.24.2023, Pulled into A07
        :param: file name = JSON file and roster = student data
        :return: None
        """
        file: TextIO = None
        try:
            json_data: list[dict[str, str, str]] = []
            for employee in employee_data:
                json_data.append({
                    "employee_first_name": employee.first_name,
                    "employee_last_name": employee.last_name,
                    "review_date": employee.review_date,
                    "review_rating": employee.review_rating
                }
                )
            with open(file_name, "w") as file:
                json.dump(json_data, file)
                print("Data successfully written to the file.")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data


# Present and Process the data
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.4.2030,Added a function to display custom error messages
    Sabrina Fechtner 12.1.23, Incorporated in A08
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 12.1.2023, Incorporated into A08
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print(f"An unexpected error occurred: {error}")

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06

        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function incorporates user choice from menu

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06
        :return: User Choice
            """
        choice = "0"
        try:
            choice = input("What would you like to do?: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Only Enter 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_employee_data(employee_data: list[Employee]):
        """ This function shows the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06

        :return: None
        """
        print("\nThe current data is:")
        for employee in employee_data:
            employee_first_name = employee.first_name
            employee_last_name = employee.last_name
            employee_review_date = employee.review_date
            employee_review_rating = employee_review_rating
            print(employee_first_name,employee_last_name, employee_review_date, employee_review_rating )

    @staticmethod
    def input_student_data(employee_data: list = None) -> List[Employee]:
        """
        This function incorporates user choice from the menu

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 12.1.2023, pulled in A08

        :param: employee_data: list of dictionary rows to be filled with input data
        :return: list
        """
        while True:
            # Create an instance of Student with valid initial values
            employee = Employee("", "", "", "")

            employee_first_name: str = input("Please enter first name: ")
            employee_last_name: str = input("Please enter last name: ")
            review_date: str = input("Enter Review Date (YYYY-MM-DD): ")
            review_rating = int(input("Enter Employee Rating (1-5): "))

            try:
                employee.first_name = employee_first_name
                employee.last_name = employee_last_name
                employee.review_date = review_date
                employee.review_rating = review_rating

                # Create a new instance with validated properties
                #employee = Employee(first_name, last_name, review_date, review_rating)
                employee_data.append(employee)

                print(
                    f"You recorded: {employee.first_name} {employee.last_name} has been reviewed on {review_date} with a rating of {review_rating}.")
                break  # if registration is successful
            except ValueError as e:
                IO.output_error_messages(f"Error recording employee data: {e}")

        return employee_data
