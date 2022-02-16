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
DEPARTMENT
SALARY
GENDER(M/F)
LOCATION
AGE

PROPERITES ->
EMPLOYEE ID: int
NAME: varchar
DEPARTMENT: FINANCE/HR/ACCOUNTS/ADMIN/SECURITY/OPERATIONS
SALARY: int
GENDER: M/F

'''

from mysql.connector import MySQLConnection, Error
import mysql.connector as connector
import time


# mydb = connector.connect(host="localhost", user="root",
#                          passwd="ROOT", database="employee_management", )
# mycursor = mydb.cursor()

def main_loop():
    print("\t\t\t", time.ctime())
    print("EMPLOYEES MANAGEMENT SYSTEM")
    print("operations...")
    print("1.employee registeration")
    print("2.employee details")
    print("3.update salary")
    print("4.employees list")
    print("5.remove employee")
    print("6.generate pay slip")
    print("7.know your salary")
    print("8.Exiting")
    response = "y"

    while response.lower() == 'y':

        operation = int(input('Enter the number of operation to perform: '))

        if operation == 1:
            register_employee()
        elif operation == 2:
            pass
            # retrieve_details()
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
        print('Thanks! Have a nice day.')


def register_employee():
    print('Departments list')
    print("1.Finance")
    print("2.HR")
    print("3.Accounts")
    print("4.Admin")
    print("5.security")
    print("6.operation")

    emp_id = input('Enter the employee id(4 digit): ')
    name = input('Enter name of the employee: ')
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    gender = input("Enter gender:(M/F) ")
    PFno = input("Enter pf number: ")
    account_number = input("Enter account number of employee: ")

    query = "insert into employee values (%s, %s, %s, %s, %s, %s, %s)" % (emp_id, name, department, salary, gender, PFno, account_number)


main_loop()