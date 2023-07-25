# -*- coding: utf-8 -*-

############################################################ File Name: studentDatabase-mainCode.py ################################################################
############################################################ By: Abir Das, Derrick Duller and Riaz Ahmed ###########################################################
################################################################## Version 1.0 and using Python 3.9 ################################################################ 

import mysql.connector
import os
import pandas as pd

# This program requires mySQL python connector to be installed in the system to interact with the mySQL database
# This program requires python Pandas to be installed in the system to interact with the CSV file


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Babu6654",
    database = "testdb"
    )
mycursor = mydb.cursor()

# Please note that the mySQL connection will be successful if you use your own credentials of mySQL workbench


# This is the student function, which ask the user for what they want perform on the student table
def studentFunction():
    print("\n Students Table: \n 1. Add Values \n 2. Delete Values \n 3. Display Table \n 4. Make your own Select Query for students table \n 5. Read CSV File to populate students table \n 6. Back to Main Menu")
    studentChoice = input("Enter corresponding number task to be done: ")
    if (studentChoice == '1'): # When user inputs '1' the following will be executed to add values on the student table. When the task is done the program reruns the function 
        try:
            studentfName = str(input("Enter student first name: "))
            studentlName = str(input("Enter student last name: "))
            studentEmail = str(input("Enter students email: "))
            mycursor.execute("INSERT INTO students (firstName, lastName, email) VALUES (%s, %s, %s)", (studentfName, studentlName, studentEmail))
            mydb.commit()
            print("\n Adding values done")
            studentFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            studentFunction()
    elif (studentChoice == '2'): # When use inputs '2' the following will be executed to delete values from student table. When the task is done the program reruns the function
        try:
            print("Student Table (ID (PK), FirstName, LastName, Email)")
            studentID = int(input("Enter Student ID of the student you want deleted: "))
            deleteSQL = "DELETE FROM students WHERE ID = '%d'" % (studentID)
            mycursor.execute(deleteSQL)
            mydb.commit()
            print("Deleting values done")
            studentFunction()
        except:
            print("Error Occured! Please check if your input is correct")
    elif (studentChoice == '3'): # When user inputs '3' the following will be executed to display table. When the task is done the program reruns the function
        try:
            print("Contents of the table: \n")
            mycursor.execute("SELECT * from students")
            studentData = mycursor.fetchall()
            print("Student Table (ID (PK), FirstName, LastName, Email)")
            for row in studentData:
                print(row)
            mydb.commit()
            studentFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            studentFunction()
    elif (studentChoice == '4'): # When use inputs '4' the following will be executed to make their own query. When the task is done the program reruns the function
        try:
            print("SELECT (a) FROM students WHERE (b)")
            print("Enter proper sql query for python mysqldb")
            studentQueryA = str(input("Enter query phrase for (a): "))
            studentQueryB = str(input("Enter query phrase for (b): "))
            fullSQL = "SELECT %s FROM students WHERE %s" % (studentQueryA,studentQueryB)
            mycursor.execute(fullSQL)
            studentQData = mycursor.fetchall()
            print("Data Requested: ")
            for row in studentQData:
                print(row)
            mydb.commit()
            studentFunction()
        except:
            print("Error Occured! Please check if your input is correct.")
            studentFunction()
    elif (studentChoice == '5'): # When use inputs '5' the following will be executed to import the csv file. When the task is done the program reruns the function
        try:
            studentCSVfile = str(input("Enter file directory of csv file for students table: "))
            empdata = pd.read_csv(studentCSVfile, index_col=False, delimiter = ',')
            empdata.head()
            for i,row in empdata.iterrows():
                sql = "INSERT INTO students (firstName, lastName, email) VALUES (%s,%s,%s)"
                mycursor.execute(sql, tuple(row))
                print("Record inserted")
                mydb.commit()
            studentFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            studentFunction()
    elif (studentChoice == '6'): # When use inputs '6' the following will be executed to go to the main menu.
        mainFunc()
    else: # if the if condition is not met the following will print and rerun the function
        print("Invalid Input. Try again!")
        studentFunction()
    
def classesFunction():
    print("\n Classes Table: \n 1. Add Values \n 2. Delete Values \n 3. Display Table \n 4. Make your own Select Query for classes table \n 5. Read CSV File to populate classes table \n 6. Back to Main Menu")
    classesChoice = input("Enter corresponding number task to be done: ")
    if (classesChoice == '1'): # When user inputs '1' the following will be executed to add values on the class table. When the task is done the program reruns the function
        try:
            classesName = input("Enter class name: ")
            mycursor.execute("INSERT INTO classes (className) VALUES (%s)", (classesName,))
            mydb.commit()
            print("\n Adding values done")
            classesFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            classesFunction()
    elif (classesChoice == '2'): # When user inputs '2' the following will be executed to delete values on the class table. When the task is done the program reruns the function
        try:
            print("Class Table (ID (PK), ClassName)")
            classID = int(input("Enter Class ID of the class you want deleted: "))
            deletecSQL = "DELETE FROM classes WHERE ID = '%d'" % (classID)
            mycursor.execute(deletecSQL)
            mydb.commit()
            print("Deleting values done")
            classesFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            classesFunction()
    elif (classesChoice == '3'): # When user inputs '3' the following will be executed to display table. When the task is done the program reruns the function
        try:
            print("Contents of the table: \n")
            mycursor.execute("SELECT * from classes")
            classData = mycursor.fetchall()
            print("Class Table (ID (PK), ClassName)")
            for row in classData:
                print(row)
            mydb.commit()
            classesFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            classesFunction()
    elif (classesChoice == '4'): # When user inputs '4' the following will be executed to make their own query. When the task is done the program reruns the function
        try:
            print("SELECT (a) FROM classes WHERE (b)")
            print("Enter proper sql query for python mysqldb")
            classQueryA = str(input("Enter query phrase for (a): "))
            classQueryB = str(input("Enter query phrase for (b): "))
            fullcSQL = "SELECT %s FROM classes WHERE %s" % (classQueryA,classQueryB)
            mycursor.execute(fullcSQL)
            classQData = mycursor.fetchall()
            print("Data Requested: ")
            for row in classQData:
                print(row)
            mydb.commit()
            classesFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            classesFunction()
    elif (classesChoice == '5'): # When user inputs '5' the following will be executed to import the csv file. When the task is done the program reruns the function
        try:    
            classCSVfile = str(input("Enter file directory of csv file for classes table: "))
            empdata = pd.read_csv(classCSVfile, index_col=False, delimiter = ',')
            empdata.head()
            for i,row in empdata.iterrows():
                sql = "INSERT INTO classes (className) VALUES (%s)"
                mycursor.execute(sql, tuple(row))
                print("Record inserted")
                mydb.commit()
            classesFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            classesFunction()
    elif (classesChoice == '6'):  # When use inputs '6' the following will be executed to go to the main menu
        mainFunc()
    else: # if the if condition is not met the following will print and rerun the function
        print("Invalid Input. Try again!")
        classesFunction()
    

def AAGFunction():
    print("\n AttendanceAndGrades Table: \n 1. Add Values \n 2. Delete Values \n 3. Display Table \n 4. Make your own Select Query for attendanceandgrades table \n 5. Read CSV File to populate attendanceandgrades table \n 6. Back to Main Menu")
    aagChoice = input("Enter corresponding number task to be done: ")
    if (aagChoice == '1'): # When user inputs '1' the following will be executed to add values on the AttendanceAndGrade table. When the task is done the program reruns the function
        try:
            studentsID = str(input("Enter student ID: "))
            classesID = str(input("Enter class ID where student is attending: "))
            attendanceRating = str(input("Enter student's attendance rate for the class (in percent, don't add percent sign): "))
            studentGrade = str(input("Enter student's grade for the class (in percent, don't add percent sign): "))
            mycursor.execute("INSERT INTO attendanceandgrades (studentID, classID, classAttendanceRate, classGrade) VALUES (%s, %s, %s, %s)", (studentsID, classesID, attendanceRating, studentGrade))
            mydb.commit()
            print("\n Adding values done")
            AAGFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            AAGFunction()
    elif (aagChoice == '2'):  # When user inputs '2' the following will be executed to delete values on the AttendanceAndGrade. When the task is done the program reruns the function
        try:
            print("AttendanceAndGrades Table (studentID (PK FK), classID (PK FK), classAttendanceRate, classGrade)")
            studentdID = int(input("Enter Student ID of the student you want deleted: "))
            classdID = int(input("Enter Class ID of the class that the student was attending that you want deleted: "))
            deleteSQL = "DELETE FROM attendanceandgrades WHERE studentID = '%d' AND classID = '%d'" % (studentdID,classdID)
            mycursor.execute(deleteSQL)
            mydb.commit()
            print("Deleting values done")
            AAGFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            AAGFunction()
    elif (aagChoice == '3'): # When user inputs '3' the following will be executed to AttendanceAndGrade. When the task is done the program reruns the function
        try:
            print("Contents of the table: \n")
            mycursor.execute("SELECT * from attendanceandgrades")
            aagData = mycursor.fetchall()
            print("AttendanceAndGrades Table (studentID (PK FK), classID (PK FK), classAttendanceRate, classGrade)")
            for row in aagData:
                print(row)
            mydb.commit()
            AAGFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            AAGFunction()
    elif (aagChoice == '4'):   # When user inputs '4' the following will be executed to make their own query. When the task is done the program reruns the function
        try:
            print("SELECT (a) FROM attendanceandgrades WHERE (b)")
            print("Enter proper sql query for python mysqldb")
            aagQueryA = str(input("Enter query phrase for (a): "))
            aagQueryB = str(input("Enter query phrase for (b): "))
            fullSQL = "SELECT %s FROM attendanceandgrades WHERE %s" % (aagQueryA,aagQueryB)
            mycursor.execute(fullSQL)
            studentAData = mycursor.fetchall()
            print("Data Requested: ")
            for row in studentAData:
                print(row)
            mydb.commit()
            AAGFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            AAGFunction()
    elif (aagChoice == '5'): # When user inputs '5' the following will be executed to import the csv file. When the task is done the program reruns the function
        try:
            aagCSVfile = str(input("Enter file directory of csv file for attendanceandgrades table: "))
            empdata = pd.read_csv(aagCSVfile, index_col=False, delimiter = ',')
            empdata.head()
            for i,row in empdata.iterrows():
                sql = "INSERT INTO attendanceandgrades (studentID, classID, classAttendanceRate, classGrade) VALUES (%s, %s, %s, %s)"
                mycursor.execute(sql, tuple(row))
                print("Record inserted")
                mydb.commit()
            AAGFunction()
        except:
            print("Error Occured! Please check if your input is correct")
            AAGFunction()
    elif (aagChoice == '6'): # When use inputs '6' the following will be executed to go to the main menu
        mainFunc()
    else: # if the if condition is not met the following will print and rerun the function
        print("Invalid Input. Try again!")
        AAGFunction()
        
def mainFunc(): # main function
    print("\n Welcome to the Student Database: \n 1. student Table \n 2. classes Table \n 3. attendanceAndGrades Table \n 4. Quit Program")
    firstMenuChoice = input("Enter corresponding number task to be done: ")
    if (firstMenuChoice == '1') : # For the student table
        studentFunction()
    elif (firstMenuChoice == '2') : # For the classes table
        classesFunction()
    elif (firstMenuChoice == '3') : # For attendanceAndGrades table
        AAGFunction()
    elif (firstMenuChoice == '4') : # to quit program
        os._exit(1)
    else: # if the conditions are the met, then the msg will print and rerun the main function
        print("Invalid Input. Try again!")
        mainFunc()

mainFunc()





