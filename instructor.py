from person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, id, first, last, handle, cohort, specialty):
        super().__init__(id, first, last, handle, cohort)
        self.specialty = specialty

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.cohort}'s instructor.'"