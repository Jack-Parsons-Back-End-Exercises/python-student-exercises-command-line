from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

celeb_tribute = Exercise("Celebrity Tribute", "HTML")
backend_capstone = Exercise("Back-end Capstone", "C#")
chicken_monkey = Exercise("ChickenMonkey", "Python")
command_line = Exercise("Student Exercises 1", "Python")

c38 = Cohort("Day Cohort 38")
c37 = Cohort("Day Cohort 37")
e9 = Cohort("Evening Cohort 9")

jack_parsons = Student("Jack", "Parsons", c38)
jack_parsons.slackHandle = "Jackson Parsons"
c38.enroll(jack_parsons)
matt_baker = Student("Matt", "Baker", c38)
matt_baker.slackHandle = "Matthew Baker"
c38.enroll(matt_baker)
adrian_garmendia = Student("Adrian", "Garmendia", c37)
adrian_garmendia.slackHandle = "Adrian Garmendia"
c37.enroll(adrian_garmendia)
dylan_rowe = Student("Dylan", "Rowe", e9)
dylan_rowe.slackHandle = "Dylan Rowe"
e9.enroll(dylan_rowe)

jisie = Instructor("Jisie", "David", c38, "Explaining things fast")
jisie.slackHandle="Jisie David"
c38.assignToClass(jisie)
adam = Instructor("Adam", "Sheaffer", c37, "Slappin da Bass")
adam.slackHandle="Spudz McNastee"
c37.assignToClass(adam)
andy = Instructor("Andy", "Collins", e9, "Sarcasm and Wizardry")
andy.slackHandle="AskingALot"
e9.assignToClass(andy)

for student in c38.students:
    jisie.assignExercise(student, command_line)
    jisie.assignExercise(student, chicken_monkey)

for student in c37.students:
    adam.assignExercise(student, backend_capstone)

for student in e9.students:
    andy.assignExercise(student, celeb_tribute)
    andy.assignExercise(student, chicken_monkey)

for exercise in jack_parsons.exercises:
    print(exercise.name)