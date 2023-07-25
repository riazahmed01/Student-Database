USE testdb;

CREATE TABLE students (
    ID INT auto_increment,
    firstName VARCHAR(100),
    lastName VARCHAR(100),
    email VARCHAR(255),
    PRIMARY KEY (ID)
);

CREATE TABLE classes (
    ID INT auto_increment,
    className VARCHAR(100),
    PRIMARY KEY (ID)
);

CREATE TABLE attendanceAndGrades (
    studentID INT,
    classID INT,
    classAttendanceRate INT,
    classGrade INT,
    PRIMARY KEY (studentID, classID),
    FOREIGN KEY (studentID) REFERENCES students(ID),
    FOREIGN KEY (classID) REFERENCES classes(ID)
);