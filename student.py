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

        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id=student_id
        self.name =name
        self.grades = []
        self.passed = "NO"
        self.honor_roll = False
        self.letter_grade = ""

    def add_grades(self, grade):
        """
        Add a single grade to the student's grade list.

        Args:
        g (int): The grade to add.
        """
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(float(grade))
        else:
            print(f"Invalid grade '{grade}': must be a number between 0 and 100.")


    def calcaverage(self):
        """
        Calculate the average of the student's grades.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def assign_letter_grade(self):
        """
        Assigns a letter grade (A–F) based on average.
        Also updates pass/fail status and honor roll flag.
        """
        avg = self.calcaverage()

        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        self.passed = "Passed" if avg >= 60 else "Failed"
        self.honor_roll = avg >= 90

    def remove_grade_by_index(self, index):
        """
        Removes a grade by its index.

        Args:
            index (int): The index to remove.
        """
        try:
            removed = self.grades.pop(index)
            print(f"Removed grade {removed} at index {index}.")
        except IndexError:
            print(f"Error: No grade at index {index}.")
        except TypeError:
            print("Error: Index must be an integer.")

    def remove_grade_by_value(self, value):
        """
        Removes a grade by its value.

        Args:
            value (float): The grade to remove.
        """
        try:
            self.grades.remove(value)
            print(f"Removed grade: {value}")
        except ValueError:
            print(f"Error: Grade value {value} not found.")
        except TypeError:
            print("Error: Grade value must be a number.")

    def check_honor(self):
        """
        Determine if the student qualifies for honors based on average grade.
        """
        avg = self.calcaverage()
        self.honor_roll = avg > 90

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


    def report(self):
        """
        Prints a formatted summary report of the student.
        """
        self.assign_letter_grade()  # Ensure latest calculations
        avg = self.calcaverage()

        print("\n====== STUDENT REPORT ======")
        print(f"ID           : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Grades       : {self.grades}")
        print(f"Grades Count : {len(self.grades)}")
        print(f"Average      : {avg:.2f}")
        print(f"Letter Grade : {self.letter_grade}")
        print(f"Status       : {self.passed}")
        print(f"Honor Roll   : {'Yes' if self.honor_roll else 'No'}")
        print("============================\n")

def start_run():
    """
    Demonstration of student system functionality.
    """

    s = Student("1001", "Jordan Smith")

    s.add_grades(95)
    s.add_grades(89.5)
    s.add_grades(102)         # Invalid
    s.add_grades(-10)         # Invalid
    s.add_grades("Ninety")    # Invalid

    s.remove_grade_by_index(10)     # Invalid
    s.remove_grade_by_value(50.0)   # Not found

    s.remove_grade_by_value(89.5)   # Valid

    s.report()


if __name__ == "__main__":
    start_run()
