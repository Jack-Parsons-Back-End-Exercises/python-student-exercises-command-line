from person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, firstName, lastName, cohort, specialty, slackHandle=""):
        super().__init__(firstName, lastName, cohort)
        self.specialty = specialty
        # self.firstName = firstName
        # self.lastName = lastName
        # self.cohort = cohort
        # self.slackHandle = ""
        # self.specialty = specialty

    def assignExercise(self, student, exercise):
        student.exercises.add(exercise)
