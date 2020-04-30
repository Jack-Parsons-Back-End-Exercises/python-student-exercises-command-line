import sqlite3

class Student():

    def __init__(self, id, first, last, handle, cohort):
        self.id = id
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Cohort():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name

class Exercise():

    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} ({self.language})'

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

reports = StudentExerciseReports()
reports.all_exercises()