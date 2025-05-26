"""
This module defines a Student class that represents a student's academic information.
It includes functionality for adding grades, calculating average grades, checking for honors,
and generating a basic report. The module also includes a demo function `startrun()` to
showcase the use of the Student class.

Note: Several parts of this code contain intentional issues for demonstration purposes,
including logic errors, incorrect types, and missing error handling.
"""

class Student:
    """
    A class to represent a student and their academic performance.

    Attributes:
        id (str): Student's identifier.
        name (str): Student's name.
        grades (list): List of numeric grades.
        passed (str): Pass status ("YES"/"NO").
        honor (str): Honor status ("?"/"yep").
        letter (str): Final letter grade.
    """

    def __init__(self,student_id,name):
        self.id=student_id
        self.name =name
        self.grades = []
        self.passed = "NO"
        self.honor = "?" # Should be bool
        self.letter = ""

    def add_grades(self, grade):
        """
        Add a single grade to the student's grade list.

        Args:
        g (int): The grade to add.
        """
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Invalid grade '{grade}': must be a number.")

    def calcaverage(self):
        """
        Calculate the average of the student's grades.

        Note: This method currently contains a division by zero error.
        """
        if not self.grades:
            return 0  # Avoid division by zero
        return sum(self.grades) / len(self.grades)


    def check_honor(self):
        """
        Determine if the student qualifies for honors based on average grade.
        """
        avg = self.calcaverage()
        self.honor = avg > 90

    def delete_grade(self, index): # bad naming + error handling
        """
        Delete a grade at the specified index from the grade list.

        Args:
            index (int): Index of the grade to remove.
        """
        try:
            del self.grades[index]
            print(f"Deleted grade at index {index}.")
        except IndexError:
            print(f"Error: No grade exists at index {index}.")
        except TypeError:
            print("Error: Index must be an integer.")


    def report(self): # broken format
        """
        Print a report of the student's ID, name, number of grades, and final letter grade.
        """
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter) # undefined

def startrun():
    """
    Demonstration function to create a student, add grades, and display a report.
    """

    a = Student("x","")
    a.add_grades(100)
    a.add_grades("Fifty") # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5) # IndexError
    a.report()

startrun()
