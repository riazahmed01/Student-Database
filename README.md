# Student-Database
Mini student database project using MySQL and Pandas

## Motivation 
### Why did you pick this database?

We picked the student database because we are students ourselves. It will be easy to relate to and work with. We worked collaboratively to figure out our approach to making the database. First we worked on a rough sketch of the ER Diagrams as it will help us plan and understand what we need to include in our database. Then we made the MySQL tables (projectcreatetables.sql). Then we divided up the work between each team member to make a function to perform tasks for each table, studentFunction(), classesFunction() and AAGFunction(). Check the report for more details.

### Logic of the database you created: relations, their attributes, constraints, etc.

The tables in the database is always designed to have a primary key. The table students has a primary key ID that auto increments as the table is populated. The table classes also has a primary key ID that auto increments as the table is populated. This makes sure that even if there are students or classes with different names, they will never be confused by the system. Lastly, attendanceandgrades table has 2 foreign keys being used as primary keys at the same time. The composite key consists of studentID that references the ID in students table and classID that references the ID in classes table. These two keys are made as the foreign keys to introduce a relationship between the attendance rate, the grades, the class, and the student. Since a student can only attend a specific class at a time, it makes sense to make them composite keys. This is the main relationship between the student and class. The relationship of attendance rate and grades to both of these variables is that a student has those data after they finish attending a class for that semester. The student is graded and also the number of times they have attended classes is analyzed and tabulated as data in the attendanceandgrades table.

### List the modules that the program includes (headers, helper functions, etc.) and explain what functions they have. Explain what tables / relations your database is built on.

❖ import mysql.connector
- We are using import mysql.connector because we are connecting our python program to the database we created in MySQL Workbench. There we have the tables for students, classes, and attendenceAndgrades.
  
❖ import os
- We are using the import os module because we implemented a condition in our main function, which helps the user to quit the program after they are finished performing their task in the table.
  
❖ import pandas as pd
- We are using the import pandas as pd module because in the assignment task we are required to implement a way to import a csv file by the user request for each tables. To do that we needed to use pandas. So now, when the user enters the location of their csv file in our program, their record gets added to the appropriate tables in the database on MySQL.

## Database tables
The tables we have in our database are the student table, classes table, and attendanceAndgrades table. In the student table, there is an ID column which is the primary key and it is auto-incremented. This means that the ID will be in the order of input by the user. Then there is a first name, last name, and email column for the students, which are strings inputs in the program. In the classes table, we have class ID, which is also auto-incremented and it is the primary key of that table as well. There is also a class name, which the user will input as a string. For example, the class name can be “Math 201.” Finally, we have the attendanceAndGrades table, which has int columns of student ID, class ID, class attendance rate, and class grades. In this table, the primary keys are student ID and class ID, and each is referenced as a foreign key to the student table and classes table. For example, student ID references the ID from the student table, and class ID references the ID from the class table. The attendance rate will be considered in percent form in the program.
