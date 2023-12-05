# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-presentation_classes
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, modified to only show IO class
# ------------------------------------------------------------------------------------------------- #

from typing import TextIO, List
from processing_classes import Employee

class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    RRoot,1.4.2030,Added a function to display custom error messages
    Sabrina Fechtner 11.17.23, Incorporated in A06
    Sabrina Fechtner 11.24.23, Pulled into A07
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays error messages to the user
        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06
        Sabrina Fechter, 11.24.2023, Pulled into A07
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
        Sabrina Fechtner, 11.25.2023 Pulled into A07
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
    def output_employee_data(employee_data: List[Employee]):
        """ This function shows the first name, last name, review date, and rating from the user
        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06
        :return: None
        """
        print("\nThe current data is:")
        for employee in employee_data:
            if employee.review_rating in {1, 2, 3, 4, 5}:
                if employee.review_rating == 5:
                    message = "{} {} is rated as 5 (Leading)"
                elif employee.review_rating == 4:
                    message = "{} {} is rated as 4 (Strong)"
                elif employee.review_rating == 3:
                    message = "{} {} is rated as 3 (Solid)"
                elif employee.review_rating == 2:
                    message = "{} {} is rated as 2 (Building)"
                elif employee.review_rating == 1:
                    message = "{} {} is rated as 1 (Not Meeting Expectations)"

                print(message.format(employee.first_name, employee.last_name))
            else:
                raise ValueError("Rating must be between 1 and 5.")
    @staticmethod
    def input_employee_data(employee_data: List[Employee]) -> List[Employee]:
        """
        This function incorporates user choice from the menu
        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated into A06
        Sabrina Fechtner, 11.24.2023, pulled in A07
        :return: None
        """
        while True:
            # Get user input
            employee_first_name: str = input("Please enter first name: ")
            employee_last_name: str = input("Please enter last name: ")
            review_date: str = input("Enter Review Date (YYYY-MM-DD): ")
            review_rating: int = input("Enter Employee Rating (1-5): ")

            try:
                employee = Employee(employee_first_name, employee_last_name, review_date, review_rating)
                employee_data.append(employee)

                print(
                    f"{employee.first_name} {employee.last_name} has been reviewed on {employee.review_date} with a rating of {employee.review_rating}.")

                break  # If registration is successful
            except ValueError as e:
                IO.output_error_messages(f"Error recording employee data: {e}")

        return employee_data
if __name__ == "__main__":
    print("This class is not meant to be run!")