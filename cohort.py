class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = set()
        self.instructors = set()

    def enroll(self, student):
        self.students.add(student)

    def assignToClass(self, instructor):
        self.instructors.add(instructor)