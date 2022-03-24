from mysql.connector import MySQLConnection, Error
import mysql.connector as connector
import time

username = input('Enter username of mysql: ')
password = input('Enter password of mysql: ')

# CHECKING CONNECTION
try:
    db = connector.connect(host='localhost', user=username, passwd=password, database='employee_management')
    db.close()
except:
    db = connector.connect(host="localhost", user=username, passwd=password)
    cursor = db.cursor()

    createDatabaseQuery = "create database employee_management"
    createTableQuery = "create table employee(emp_id int(5) NOT NULL PRIMARY KEY, emp_name varchar(30) NOT NULL , gender char(1) NOT NULL, department varchar(11) NOT NULL, salary int NOT NULL, location varchar(20) NOT NULL, Accountno int(7) NOT NULL)"

    cursor.execute(createDatabaseQuery)
    db = connector.connect(host="localhost", user=username, passwd=password, database='employee_management')

    cursor = db.cursor()
    cursor.execute(createTableQuery)
    db.commit()
    cursor.close()
    db.close()

mydb = connector.connect(host='localhost', user=username, passwd=password, database='employee_management')
mycursor = mydb.cursor()

def mainLoop():
    print(f'\t\t\t {time.ctime()}')
    print("\t\t\t EMPLOYEES MANAGEMENT SYSTEM")
    response = "y"

    while response.lower() == 'y':
        print('\n')
        print("\t\t\t Operations")
        print("\t\t\t 1.employee registeration")
        print("\t\t\t 2.employee details")
        print("\t\t\t 3.update salary")
        print("\t\t\t 4.employees list")
        print("\t\t\t 5.remove employee")
        print("\t\t\t 6.generate pay slip")
        print("\t\t\t 7.Exiting")

        operation = int(input('Enter the operation to perform(number): '))

        if operation == 1:
            registerEmployee()
        elif operation == 2:
            getDetails()
        elif operation == 3:
            updateSalary()
        elif operation == 4:
            getEmployeeList()
        elif operation == 5:
            deleteEmployee()
        elif operation == 6:
            generatePayslip()
        elif operation == 7:
            mycursor.close()
            mydb.close()
            print('Thanks! Have a nice day.')
            break
        else:
            print("Sorry Couldn't find that one ...")

        response = input('Do you want to continue:(Y/N)')

        if response.lower() != 'y':
            mycursor.close()
            mydb.close()
            print('Thanks! Have a nice day.')
            break
        


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

        print('\n')
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
    except Error as _:
        print('Something went wrong there!')
        print('Please try again...')
    employeeTuple = mycursor.fetchall()[0] 
    print(f'Employee details {employeeTuple[1]}...')
    
    print('\n')

    print('%11s'%'employee id', '%17s'%'name', '%9s'%'gender', '%15s'%'department', '%9s'%'salary', '%13s'%'city', '%11s'%'account no')

    print('%11s'%str(employeeTuple[0]), '%17s'%employeeTuple[1], '%9s'%employeeTuple[2], '%15s'%employeeTuple[3], '%9s'%str(employeeTuple[4]), '%13s'%employeeTuple[5], '%11s'%str(employeeTuple[6]))

def updateSalary():
    employeeId = input('Enter the employee id: ')

    toIncrementOrDecrement = int(input('Enter operation (increment -> 1 decrement -> 2): '))

    if toIncrementOrDecrement == 1:
        increment = input('Enter the amount to increment: ')

        try:
            query = "UPDATE employee SET salary = salary + '%s' WHERE emp_id = '%s'" % (increment, employeeId)
            mycursor.execute(query)
            mydb.commit()
            print('Salary updated successfully!')
        except Error as _:
            print('Something went wrong there!')
            print('Please try again...')
            mydb.rollback()

    else:
        decrement = input('Enter the amount to decrement: ')

        try:
            query = "UPDATE employee SET salary = salary - '%s' WHERE emp_id = '%s'" % (decrement, employeeId)
            mycursor.execute(query)
            mydb.commit()
            print('Salary updated successfully!')
        except Error as _:
            print('Something went wrong there!')
            print('Please try again...')
            mydb.rollback()

def getEmployeeList():
    print('EMPLOYEE LIST...')
    print('\n')

    print('%11s'%'employee id', '%17s'%'name', '%9s'%'gender', '%15s'%'department', '%9s'%'salary', '%13s'%'city', '%11s'%'account no')
    try:
        query = "SELECT * FROM employee"
        mycursor.execute(query)
        employeeList = mycursor.fetchall()
        for row in employeeList:
            print('%11s'%str(row[0]), '%17s'%row[1], '%9s'%row[2], '%15s'%row[3], '%9s'%str(row[4]), '%13s'%row[5], '%11s'%str(row[6]))
    except Error as _:
        print('Something went wrong there!')
        print('Please try again...')

def deleteEmployee():
    employeeId = input('Enter the employee id: ')
    print('\n')
    try:
        query = "DELETE FROM employee WHERE emp_id='%s'" % employeeId
        mycursor.execute(query)
        mydb.commit()
        print('Employee removed successfully!')
    except Error as _:
        print('Something went wrong there!')
        print('Please try again...')
        mydb.rollback()

def generatePayslip():
    employeeId = input('Enter the employee id: ')
    print('\n')

    data = tuple()

    try:
        query = "SELECT * FROM employee WHERE emp_id='%s'" % employeeId
        mycursor.execute(query)
        listOfEmployees = mycursor.fetchall()

        for emp in listOfEmployees:
            if str(emp[0]) == employeeId:
                data = emp
  
        mydb.commit()
    except Error as _:
        print('Something went wrong there!')
        print('Please try again...')
        mydb.rollback()

    employeeName = data[1]
    employeeSalary = data[4]
    departmentName = data[3]
    city = data[5]
    accountNumber = data[6]

    medicalAllowance = 0.02 * employeeSalary
    dailyAllowance = 0.01 * employeeSalary
    houseRentAllowance = 0.05 * employeeSalary
    gross = employeeSalary + medicalAllowance + dailyAllowance + houseRentAllowance
    pf = 0.02 * employeeSalary
    it = 0.04 * employeeSalary
    deduction = pf + it

    net = gross - deduction

    print(f'\t\t\t ---------------SALARY SLIP OF {employeeName}----------------')

    print(f'\t\t\t Employee ID:', employeeId)
    print(f'\t\t\t Name of the employee:', employeeName)
    print(f'\t\t\t Department of employee:', departmentName)
    print(f'\t\t\t City of employee:', city)

    print(f'\t\t\t Account number:', accountNumber)

    print('\t\t\t Basic Salary:', employeeSalary)
    print('\n')

    print('\t\t\t Medical Allowance:\t\t', medicalAllowance)

    print('\t\t\t Daily Allowance:\t\t', dailyAllowance)

    print('\t\t\t House Rent Allowed:\t\t', houseRentAllowance)

    print('\t\t\t +')
    print('\t\t\t -----------------------------------------------')
    print('\t\t\t Gross Salary\t\t', gross)

    print('\n')
    print('\t\t\t Provident Fund\t\t', pf)

    print('\t\t\t Income Tax\t\t', it)

    print('\t\t\t +')
    print('\t\t\t -----------------------------------------------')

    print('\t\t\t Deductions:\t\t', deduction)

    print('\t\t\t Net Salary = Gross - Deductions\t\t₹', net)

mainLoop()