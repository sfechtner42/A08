
from typing import List

import processing_classes
from processing_classes import Employee
import presentation_classes


# Define Constants
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

# Define Variables
employees: List = []  # a table of employees data
menu_choice = ''

# Main Program
employees: List[Employee] = processing_classes.FileProcessor.read_data_from_file(file_name=FILE_NAME)

while True:
    presentation_classes.IO.output_menu(menu=MENU)

    menu_choice = presentation_classes.IO.input_menu_choice()

    if menu_choice == "1":  # Show current employee rating data
        presentation_classes.IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "2":  # Enter new employee rating data
        employees = presentation_classes.IO.input_employee_data(employee_data=employees)
        continue

    elif menu_choice == "3":  # Save data to a file
        processing_classes.FileProcessor.write_data_to_file(file_name=FILE_NAME, employee_data=employees)
        continue

    elif menu_choice == "4":  # Exit the program
        break  # out of the while loop
