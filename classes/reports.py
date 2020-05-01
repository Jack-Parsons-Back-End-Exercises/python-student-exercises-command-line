import sqlite3
from .student import Student
from .instructor import Instructor
from .cohort import Cohort
from .exercise import Exercise

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

            [print(instructor) for instructor in all_instructors],
    
    def exercises_with_students(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.ExerciseId,
	            e.ExerciseName,
	            s.StudentId,
	            s.FirstName,
            	s.LastName
            FROM Exercise e
            JOIN AssignedExercise ae on ae.ExerciseId = e.ExerciseId
            JOIN Student s on s.StudentId = ae.StudentId""")

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

    def students_with_exercises(self):

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT s.StudentId,
	            s.FirstName,
	            s.LastName,
	            e.ExerciseId,
	            e.ExerciseName
            FROM Student s
	        JOIN AssignedExercise ae ON ae.StudentId = s.StudentId
	        JOIN Exercise e ON ae.ExerciseId = e.ExerciseId""")

            data = db_cursor.fetchall()

            for row in data:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')

    def exercises_assigned_instructors(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.InstructorId,
	            i.FirstName,
	            i.LastName,
	            e.ExerciseId,
	            e.ExerciseName
            FROM Instructor i
	        JOIN AssignedExercise ae ON ae.InstructorId = i.InstructorId
	        JOIN Exercise e ON ae.ExerciseId = e.ExerciseId""")

            data = db_cursor.fetchall()

            for row in data:
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    if exercise_name not in instructors[instructor_name]:
                        instructors[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors.items():
                print(f'{instructor_name} has assigned:')
                for exercise in exercises:
                        print(f'\t* {exercise}')