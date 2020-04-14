class Student:

    def __init__(self, firstName, lastName, cohort):
        self.firstName = firstName
        self.lastName = lastName
        self.slackHandle = ""
        self.cohort = cohort
        self.exercises = set()