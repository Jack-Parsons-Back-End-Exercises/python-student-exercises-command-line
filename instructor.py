class Instructor():

    def __init__(self, id, first, last, handle, cohort, specialty):
        self.id = id
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort
        self.specialty = specialty

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.cohort}'s instructor.'"