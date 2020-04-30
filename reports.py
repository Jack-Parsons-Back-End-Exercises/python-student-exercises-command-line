import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor

class StudentExerciseReports():

    """Methods for reports on the Student Exercises Database"""

    def __init__(self):
        self.db_path = "/Users/jcksnparsons/workspace/python/python-student-exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row [0], row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT s.StudentId,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.CohortName
            FROM Student s
            JOIN Cohort c on s.CohortId = c.CohortId
            ORDER BY s.CohortId
            """)

            all_students = db_cursor.fetchall()

            [print(student) for student in all_students]

    def all_cohorts(self):

        """Retrives list of all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row [0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.CohortId,
                c.CohortName
            FROM Cohort c
            ORDER BY c.CohortId""")

            all_cohorts = db_cursor.fetchall()

            [print(cohort) for cohort in all_cohorts]

    def all_exercises(self):

        """Retrives list of all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.ExerciseId,
                e.ExerciseName,
                e.ExerciseLanguage
            FROM Exercise e
            ORDER BY e.ExerciseId""")

            all_exercises = db_cursor.fetchall()

            [print(exercise) for exercise in all_exercises]

    def javascript_exercises(self):

        """Retrieves just the JavaScript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exerciseId,
                e.ExerciseName,
                e.ExerciseLanguage
            FROM Exercise e
            WHERE e.ExerciseLanguage = 'JavaScript'""")

            js_exercises = db_cursor.fetchall()

            [print(exercise) for exercise in js_exercises]

    def python_exercises(self):

        """Retrieves just the Python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exerciseId,
                e.ExerciseName,
                e.ExerciseLanguage
            FROM Exercise e
            WHERE e.ExerciseLanguage = 'Python'""")

            python_exercises = db_cursor.fetchall()

            [print(exercise) for exercise in python_exercises]

    def csharp_exercises(self):

        """Retrieves just the C# exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exerciseId,
                e.ExerciseName,
                e.ExerciseLanguage
            FROM Exercise e
            WHERE e.ExerciseLanguage = 'CSharp'""")

            csharp_exercises = db_cursor.fetchall()

            [print(exercise) for exercise in csharp_exercises]

    def all_instructors(self):

        """Retrieves all of the instructors"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[0], row[1], row[2], row[4], row[5], row[6]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.InstructorId,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                c.CohortName,
                i.InstructorSpecialty
            FROM Instructor i
            JOIN Cohort c on i.CohortId = c.CohortId
            ORDER BY i.CohortId""")

            all_instructors = db_cursor.fetchall()

            [print(instructor) for instructor in all_instructors]

reports = StudentExerciseReports()
reports.all_instructors()