from person import NSSPerson

class Student(NSSPerson):

    def __init__(self, firstName, lastName, cohort, slackHandle=""):
        super().__init__(firstName, lastName, cohort)
        self.exercises = set()