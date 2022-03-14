# CODE FOR PROJECT
'''
1. adding employee
2. Deleting employee
3. retrieving
4. modifying
5. generate pay slip
6. exit

EMPLOYEE Record->
Employee id
NAME
GENDER
DEPARTMENT
SALARY
LOCATION
ACCOUNT NO(7digit)

PROPERITES ->
EMPLOYEE ID: int
NAME: varchar
DEPARTMENT: FINANCE/HR/ACCOUNTS/ADMIN/SECURITY/OPERATIONS
SALARY: int
GENDER: M/F

'''

from dataclasses import FrozenInstanceError
from mysql.connector import MySQLConnection, Error
import mysql.connector as connector
import time

# CHECKING CONNECTION
try:
    db = connector.connect(host='localhost', user='root', passwd='ROOT', database='employee_management')
except:
    db = connector.connect(host="localhost", user="root", passwd="ROOT")
    cursor = db.cursor()

    createDatabaseQuery = "create database employee_management"
    createTableQuery = "create table employee(emp_id int(5) NOT NULL PRIMARY KEY, emp_name varchar(30) NOT NULL , gender char(1) NOT NULL, department varchar(11) NOT NULL, salary int NOT NULL, location varchar(20) NOT NULL, Accountno int(7) NOT NULL)"

    cursor.execute(createDatabaseQuery)
    db = connector.connect(host="localhost", user="root", passwd="ROOT", database='employee_management')

    cursor = db.cursor()
    cursor.execute(createTableQuery)
    db.commit()
    db.close()

mydb = connector.connect(host='localhost', user='root', passwd='ROOT', database='employee_management')
mycursor = mydb.cursor()

def mainLoop():
    print("\t\t\t", time.ctime())
    print("EMPLOYEES MANAGEMENT SYSTEM")
    response = "y"

    while response.lower() == 'y':
        print("operations...")
        print("1.employee registeration")
        print("2.employee details")
        print("3.update salary")
        print("4.employees list")
        print("5.remove employee")
        print("6.generate pay slip")
        print("7.know your salary")
        print("8.Exiting")

        operation = int(input('Enter the operation to perform(number): '))

        if operation == 1:
            registerEmployee()
        elif operation == 2:
            getDetails()
        elif operation == 3:
            pass
            # update_salary()
        elif operation == 4:
            pass
            # retrieve_list()
        elif operation == 5:
            pass
            # delete_employee()
        elif operation == 6:
            pass
            # generate_payslip()
        elif operation == 7:
            pass
            # get_salary()
        elif operation == 7:
            # print('Exiting...')
            break
        else:
            print("Sorry Couldn't find that one ...")

        response = input('Do you want to continue:(Y/N)')

        if response.lower() != 'y':
            break
    else:
        cursor.close()
        mydb.close()
        print('Thanks! Have a nice day.')


def registerEmployee():
    print('Departments list')
    print("1.Finance")
    print("2.HR")
    print("3.Accounts")
    print("4.Admin")
    print("5.security")
    print("6.operations")

    emp_id = input('Enter employee id(5 digit): ')
    name = input('Enter name of the employee: ')
    gender = input("Enter gender:(M/F) ")
    department = input("Enter department number: ")
    salary = input("Enter salary of employee: ")
    city = input("Enter city: ")
    account_number = input("Enter account number of employee: ")

    if department == 1:
        department = 'Finance'
    elif department == 2:
        department = 'HR'
    elif department == 3:
        department = 'Accounts'
    elif department == 4:
        department = 'Admin'
    elif department == 5:
        department = 'security'
    else:
        department = 'operations'

    try:
        query = "insert into employee values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (emp_id, name, gender.upper(), department, salary, city, account_number)
        mycursor.execute(query)
        mydb.commit()

        print('/n')
        print('Employee Added Successfully!')
    except Error as error:
        print('Something went wrong there!')
        print('Please try again...')
        mydb.rollback()

def getDetails():
    employeeId = input('Enter employee id: ')

    try:
        query = "select * from employee where emp_id='%s'" % employeeId
        mycursor.execute(query)
    except Error as error:
        print('Something went wrong there!')
        print('Please try again...')
    employeeTuple = mycursor.fetchall() # LIST(<TUPLE>)
    
    print(employeeTuple)

mainLoop()