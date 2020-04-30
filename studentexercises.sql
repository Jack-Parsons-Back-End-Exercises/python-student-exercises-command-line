CREATE TABLE Cohort (
	CohortId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	CohortName TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
	StudentId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId INT,
	FOREIGN KEY (CohortId) REFERENCES Cohort (CohortId)
);

CREATE TABLE Instructor (
	InstructorId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	InstructorSpecialty TEXT NOT NULL UNIQUE,
	CohortId INT,
	FOREIGN KEY (CohortId) REFERENCES Cohort (CohortId)
);

CREATE TABLE Exercise (
	ExerciseId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ExerciseName TEXT NOT NULL UNIQUE,
	ExerciseLanguage TEXT NOT NULL
);

CREATE TABLE AssignedExercise (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId INT,
	ExerciseId INT,
	FOREIGN KEY (StudentId) REFERENCES Student (StudentId),
	FOREIGN KEY (ExerciseId) REFERENCES Exercise (ExerciseId)
);

INSERT INTO Cohort (CohortName)
		VALUES('Day Cohort 38');

INSERT INTO Cohort (CohortName)
		VALUES('Day Cohort 37');

INSERT INTO Cohort (CohortName)
		VALUES('Evening Cohort 10');


INSERT INTO Exercise (ExerciseName, ExerciseLanguage)
		VALUES('Keahua Arboretum', 'CSharp');

INSERT INTO Exercise (ExerciseName, ExerciseLanguage)
		VALUES('ChickenMonkey', 'Python');

INSERT INTO Exercise (ExerciseName, ExerciseLanguage)
		VALUES('Welcome To Nashville', 'JavaScript');

INSERT INTO Exercise (ExerciseName, ExerciseLanguage)
		VALUES('Nutshell', 'JavaScript');

INSERT INTO Exercise (ExerciseName, ExerciseLanguage)
		VALUES('Car Dealership', 'Python');

INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, InstructorSpecialty)
		VALUES('Jisie', 'David', '@jisiedavid', 1, 'Pickling Mangoes');

INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, InstructorSpecialty)
		VALUES('Adam', 'Sheaffer', '@spudzmcnasty', 1, 'Slapping The Bass');

INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, InstructorSpecialty)
		VALUES('Bryan', 'Nilsen', '@bryguy', 1, 'High Fives');

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Jack', 'Parsons', '@jcksnparsons', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Cooper', 'Nichols', '@coopnichols', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Landon', 'Morgan', '@landonmorgan', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Sophia', 'Candiani', '@sofiacandiani', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Roxanne', 'Nasraty', '@roxien', 3);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Bito', 'Mann', '@bitomann', 2);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
	VALUES ('Matt', 'Blagg', '@mattblagg', 2);

SELECT * FROM Exercise;

INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(1, 2);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(1, 1);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(2, 1);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(2, 3);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(3, 4);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(3, 2);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(4, 1);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(4, 5);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(5, 5);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(5, 3);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(6, 1);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(6, 4);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(7, 2);
INSERT INTO AssignedExercise(StudentId, ExerciseId)
	VALUES(7, 3);

DELETE FROM AssignedExercise WHERE AssignedExercise.StudentId = 1 AND AssignedExercise.ExerciseId = 3;

SELECT s.FirstName, s.LastName, e.ExerciseName
	FROM Student s LEFT JOIN Exercise e LEFT JOIN AssignedExercise WHERE AssignedExercise.ExerciseId = e.ExerciseId AND AssignedExercise.StudentId = s.StudentId;

