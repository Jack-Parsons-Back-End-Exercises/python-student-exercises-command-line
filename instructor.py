class Instructor:

    def __init__(self, firstName, lastName, cohort, specialty):
        self.firstName = firstName
        self.lastName = lastName
        self.cohort = cohort
        self.slackHandle = ""
        self.specialty = specialty

    def assignExercise(self, student, exercise):
        student.exercises.add(exercise)
