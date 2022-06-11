import mysql.connector
con = mysql.connector.connect(
    host="localhost", user="root", password="", database="Salary_Management_System1")
def menu():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                  Salary Management System")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. Administer/Hr.")
    print("        2. General Worker.")
    print("        3. Payroll.")
    print("        4. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    if ch == 1:
        AdministerHr_menu()
    elif ch == 2:
        General_Work_menu()
    elif ch == 3:
        displaypayrooll()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice.")
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
        menu()


def AdministerHr_menu():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("              Welcome To Administer/Hr Department")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. Add Employee.")
    print("        2. Remove Employee .")
    print("        3. Update Employee's Information.")
    print("        4. Update Employee's Tax.")
    print("        5. Update Employee’s Insurance.")
    print("        6. Display.")
    print("        7. Back.")
    print("        8. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    code=1
    if ch == 1:
        Add_Employ(code)
    elif ch == 2:
        Remove_Employ(code)
    elif ch == 3:
        Update_Employee_Information(code)
    elif ch == 4:
        Employee_Tax(code)
    elif ch == 5:
        Employees_Insurance(code)
    elif ch == 6:
        Display_menu_Administer_Hr()
    elif ch == 7:
        menu()
    elif ch == 8:
        exit(0)
    else:
        print("Invalid Choice")
        AdministerHr_menu()


def General_Work_menu():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("              Welcome To General Worker Department")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. Full Time Worker Sector.")
    print("        2. Part Time Worker Sector.")
    print("        3. Back.")
    print("        4. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    if ch == 1:
        Full_Time()
    elif ch == 2:
        Part_Time()
    elif ch == 3:
        menu()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice.")
        General_Work_menu()

def Full_Time():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                 Full Time Worker Sector")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. Add Employee.")
    print("        2. Remove Employee .")
    print("        3. Update Employee's Information.")
    print("        4. Update Employee's Tax.")
    print("        5. Update Employee’s Insurance.")
    print("        6. Display.")
    print("        7. Back.")
    print("        8. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    code = 2
    if ch == 1:
        Add_Employ(code)
    elif ch == 2:
        Remove_Employ(code)
    elif ch == 3:
        Update_Employee_Information(code)
    elif ch == 4:
        Employee_Tax(code)
    elif ch == 5:
        Employees_Insurance(code)
    elif ch == 6:
        Display_menu_Fulltime()
    elif ch == 7:
        General_Work_menu()
    elif ch == 8:
        exit(0)
    else:
        print("Invalid Choice")
        Full_Time()

def Part_Time():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                 Part Time Worker Sector")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. Add Employee.")
    print("        2. Remove Employee.")
    print("        3. Update Employee's Information.")
    print("        4. Update Employee's Tax.")
    print("        5. Display.")
    print("        6. Back.")
    print("        7. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    code = 3
    if ch == 1:
        Add_Employ(code)
    elif ch == 2:
        Remove_Employ(code)
    elif ch == 3:
        Update_Employee_Information(code)
    elif ch == 4:
        Employee_Tax(code)
    elif ch == 5:
        Display_menu_Parttime()
    elif ch == 6:
        General_Work_menu()
    elif ch == 7:
        exit(0)
    else:
        print("Invalid Choice")
        Part_Time()


def Display_menu_Administer_Hr():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Display")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. All Employee's Information.")
    print("        2. Search employee.")
    print("        3. Back.")
    print("        4. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    if ch == 1:
        AdministerHr_DisplayAll()
    elif ch == 2:
        AdministerHr_Displaysearch()
    elif ch == 3:
        AdministerHr_menu()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice")
        Display_menu_Administer_Hr()

def AdministerHr_DisplayAll():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                  All Employee's Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    sql = 'select *from  administerhr_employee a,Tax t, Insurance i where a.AId=t.EId and t.EId=i.EId'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("        Employee salary after Insurance is included: ", i[12])
        print("        Employee salary percentage of Insurance: ", i[13])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Administer_Hr()

def AdministerHr_Displaysearch():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Search")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id=input("Enter Employee's Id: ")
    sql = 'select *from  administerhr_employee a,Tax t, Insurance i where a.AId=t.EId and t.EId=i.EId and a.AId=%s'
    database = (Id,)
    c = con.cursor()
    c.execute(sql,database)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("        Employee salary after Insurance is included: ", i[12])
        print("        Employee salary percentage of Insurance: ", i[13])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Administer_Hr()

def displaypayrooll():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                         Payroll Segment")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    sql = 'select sum(ASalary) from administerhr_employee;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        a=i[0]

    sql = 'select sum(FSalary) from fulltime;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        b = i[0]

    sql = 'select sum(PSalary) from parttime;'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        c = i[0]

    total=a+b+c

    print('        Total monthly payroll',total)

    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Administer_Hr()


def Display_menu_Fulltime():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Display")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. All Employee's Information.")
    print("        2. Search employee.")
    print("        3. Back.")
    print("        4. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    if ch == 1:
        Fulltime_DisplayAll()
    elif ch == 2:
        Fulltime_Displaysearch()
    elif ch == 3:
        Full_Time()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice")
        Display_menu_Fulltime()

def Fulltime_DisplayAll():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                  All Employee's Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    sql = 'select *from  fulltime f,Tax t, Insurance i where f.FId=t.EId and t.EId=i.EId'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("        Employee salary after Insurance is included: ", i[12])
        print("        Employee salary percentage of Insurance: ", i[13])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Fulltime()

def Fulltime_Displaysearch():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Search")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id=input("Enter Employee's Id: ")
    sql = 'select *from  fulltime f,Tax t, Insurance i where f.FId=t.EId and t.EId=i.EId and f.FId=%s'
    database = (Id,)
    c = con.cursor()
    c.execute(sql,database)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("        Employee salary after Insurance is included: ", i[12])
        print("        Employee salary percentage of Insurance: ", i[13])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Fulltime()

def Display_menu_Parttime():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Display")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    print("        1. All Employee's Information.")
    print("        2. Search employee.")
    print("        3. Back.")
    print("        4. Exit.")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    ch = int(input("      Enter your option: "))
    print("****-----****    ****-----****    ****-----****    ****-----****\n")
    if ch == 1:
        Parttime_DisplayAll()
    elif ch == 2:
        Parttime_Displaysearch()
    elif ch == 3:
        Part_Time()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice")
        Display_menu_Fulltime()

def Parttime_DisplayAll():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                  All Employee's Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    sql =  'select *from  parttime p,Tax t where p.PId=t.EId'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Parttime()

def Parttime_Displaysearch():
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                          Search")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id=input("Enter Employee's Id: ")
    sql = 'select *from  parttime p,Tax t where p.PId=t.EId and p.PId=%s'
    database = (Id,)
    c = con.cursor()
    c.execute(sql,database)
    r = c.fetchall()
    for i in r:
        print("        Employee id number: ", i[0])
        print("        Employee name: ", i[1])
        print("        Employee age: ", i[2])
        print("        Employee address: ", i[3])
        print("        Employee designation: ", i[4])
        print("        Employee monthly salary: ", i[5])
        print("        Employee monthly salary after tax is included: ", i[7])
        print("        Employee monthly percentage of tax: ", i[8])
        print("        Employee yearly salary after tax is included: ", i[9])
        print("        Employee yearly percentage of tax: ", i[10])
        print("****-----****    ****-----****    ****-----****    ****-----****\n")
    Display_menu_Parttime()


def Add_Employ(code):
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                       Add New Employee")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id = input("Enter Employee Id: ")
    if code==1:
        if (administerhr_check_employee(Id) == True and  administerhr_check_employee_Ta(Id) == True and administerhr_check_employee_In(Id) == True ):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("      Sorry Sir,Employee aready exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")

        else:
            AName = input("Enter Employee Name : ")
            AAge = input("Enter Employee Age: ")
            AAddress = input("Enter Employee Address: ")
            ADesignation = input("Enter Employee Designation: ")
            ASalary = input("Enter Employee monthly salary: ")
            database = (Id, AName, AAge, AAddress, ADesignation, ASalary)
            sql = 'insert into administerhr_employee values(%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, database)
            con.commit()
            tax_Add(Id,ASalary)

            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                      Employee Added Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        AdministerHr_menu()

    elif code==2:
        if (General_FullTime_check_employee(Id) == True and administerhr_check_employee_Ta(Id) == True and administerhr_check_employee_In(Id) == True):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("      Sorry Sir,Employee aready exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")

        else:
            FName = input("Enter Employee Name : ")
            FAge = input("Enter Employee Age: ")
            FAddress = input("Enter Employee Address: ")
            FDesignation = input("Enter Employee Designation: ")
            FSalary = input("Enter Employee monthly salary: ")
            database = (Id, FName, FAge, FAddress, FDesignation, FSalary)
            sql = 'insert into fulltime values(%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, database)
            con.commit()
            tax_Add(Id,FSalary)

            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                      Employee Added Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Full_Time()
    elif code == 3:
        if (General_PartTime_check_employee(Id) == True and administerhr_check_employee_Ta(Id) == True and administerhr_check_employee_In(Id) == True):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("      Sorry Sir,Employee aready exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")

        else:
            PName = input("Enter Employee Name : ")
            PAge = input("Enter Employee Age: ")
            PAddress = input("Enter Employee Address: ")
            PDesignation = input("Enter Employee Designation: ")
            PSalary = input("Enter Employee monthly salary: ")
            database = (Id, PName, PAge, PAddress, PDesignation, PSalary)
            sql = 'insert into Parttime values(%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, database)
            con.commit()
            tax_AddP(Id,PSalary)

            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                      Employee Added Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Part_Time()

def Remove_Employ(code):
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                       Remove Employee")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id = input("Enter Employee Id: ")
    if code==1:
        if (administerhr_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            sql = 'delete from administerhr_employee where AId=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            remove_taxe_info(Id)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                    Employee Removed Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        AdministerHr_menu()
    elif code==2:
        if (General_FullTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            sql = 'delete from fulltime where FId=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            remove_taxe_info(Id)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                    Employee Removed Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Full_Time()
    elif code==3:
        if (General_PartTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            sql = 'delete from parttime where PId=%s'
            data = (Id,)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            remove_taxe_info(Id)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                    Employee Removed Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Part_Time()

def Update_Employee_Information(code):
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                     Update Employee's Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id = input("Enter Employee Id: ")
    if code == 1:
        if (administerhr_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            AName = input("Enter Employee Name : ")
            AAge = input("Enter Employee Age: ")
            AAddress = input("Enter Employee Address: ")
            ADesignation = input("Enter Employee Designation: ")
            ASalary = input("Enter Employee monthly salary: ")

            sql = 'update administerhr_employee set AName=%s where AId=%s'
            d = (AName, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update administerhr_employee set AAge=%s where AId=%s'
            d = (AAge, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update administerhr_employee set AAddress=%s where AId=%s'
            d = (AAddress, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update administerhr_employee set ADesignation=%s where AId=%s'
            d = (ADesignation, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update administerhr_employee set ASalary=%s where AId=%s'
            d = (ASalary, Id)
            c.execute(sql, d)
            con.commit()
            tax_Add(Id, ASalary)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                   Updated Employee's Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        AdministerHr_menu()
    elif code==2:
        if (General_FullTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            FName = input("Enter Employee Name : ")
            FAge = input("Enter Employee Age: ")
            FAddress = input("Enter Employee Address: ")
            FDesignation = input("Enter Employee Designation: ")
            FSalary = input("Enter Employee monthly salary: ")

            sql = 'update fulltime set AName=%s where FId=%s'
            d = (FName, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update fulltime set AAge=%s where FId=%s'
            d = (FAge, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update fulltime set AAddress=%s where FId=%s'
            d = (FAddress, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update fulltime set ADesignation=%s where FId=%s'
            d = (FDesignation, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update fulltime set ASalary=%s where FId=%s'
            d = (FSalary, Id)
            c.execute(sql, d)
            con.commit()
            tax_Add(Id, FSalary)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("                   Updated Employee's Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Full_Time()
    elif code ==3:
        if (General_PartTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            PName = input("Enter Employee Name : ")
            PAge = input("Enter Employee Age: ")
            PAddress = input("Enter Employee Address: ")
            PDesignation = input("Enter Employee Designation: ")
            PSalary = input("Enter Employee monthly salary: ")

            sql = 'update parttime set PName=%s where PId=%s'
            d = (PName, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update parttime set PAge=%s where PId=%s'
            d = (PAge, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update parttime set PAddress=%s where PId=%s'
            d = (PAddress, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update parttime set PDesignation=%s where PId=%s'
            d = (PDesignation, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update parttime set PSalary=%s where PId=%s'
            d = (PSalary, Id)
            c.execute(sql, d)
            con.commit()
            tax_AddP(Id,PSalary)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("           Updated Employee's Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Part_Time()

def Employee_Tax(code):
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                     Update Employee's Tax Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id = input("Enter Employee Id: ")
    if code == 1:
        if (administerhr_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and  administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            percentage = int(input("Enter the percentage of tax: "))
            sql = 'select ASalary from administerhr_employee where AId=%s'
            database = (Id,)
            c = con.cursor()
            c.execute(sql, database)
            r = c.fetchone()
            t = int(r[0]) * (percentage/100)
            tax_Salary = int(r[0]) - t

            Year_tax_Salary = tax_Salary * 12
            Yearly_tax_percentage = percentage * 12
            Monlhly_tax_Salary = str(tax_Salary)
            Yearly_tax_Salary = str(Year_tax_Salary)
            Monlhly_tax_Salary_percentage = str(percentage) + '%'
            Yearly_tax_Salary_percentage = str(Yearly_tax_percentage) + '%'


            sql = 'update tax set Monlhly_tax_Salary=%s where EId=%s'
            d = (Monlhly_tax_Salary, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Monlhly_tax_Salary_percentage=%s where EId=%s'
            d = (Monlhly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary=%s where EId=%s'
            d = (Yearly_tax_Salary, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary_percentage=%s where EId=%s'
            d = (Yearly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()
            insurance_Add(Id, Monlhly_tax_Salary)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("       Updated Employee's Tax Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        AdministerHr_menu()

    elif code==2:
        if (General_FullTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            percentage = int(input("Enter the percentage of tax: "))
            sql = 'select FSalary from fulltime where FId=%s'
            database = (Id,)
            c = con.cursor()
            c.execute(sql, database)
            r = c.fetchone()
            t = int(r[0]) * (percentage/100)
            tax_Salary = int(r[0]) - t

            Year_tax_Salary = tax_Salary * 12
            Yearly_tax_percentage = percentage * 12
            Monlhly_tax_Salary = str(tax_Salary)
            Yearly_tax_Salary = str(Year_tax_Salary)
            Monlhly_tax_Salary_percentage = str(percentage) + '%'
            Yearly_tax_Salary_percentage = str(Yearly_tax_percentage) + '%'


            sql = 'update tax set Monlhly_tax_Salary=%s where EId=%s'
            d = (Monlhly_tax_Salary, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Monlhly_tax_Salary_percentage=%s where EId=%s'
            d = (Monlhly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary=%s where EId=%s'
            d = (Yearly_tax_Salary, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary_percentage=%s where EId=%s'
            d = (Yearly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()
            insurance_Add(Id, Monlhly_tax_Salary)
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("         Updated Employee's Tax Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Full_Time()

    elif code == 3 :
        if (General_PartTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            percentage = int(input("Enter the percentage of tax: "))
            sql = 'select PSalary from parttime where PId=%s'
            database = (Id,)
            c = con.cursor()
            c.execute(sql, database)
            r = c.fetchone()
            t = int(r[0]) * (percentage/100)
            tax_Salary = int(r[0]) - t

            Year_tax_Salary = tax_Salary * 12
            Yearly_tax_percentage = percentage * 12
            Monlhly_tax_Salary = str(tax_Salary)
            Yearly_tax_Salary = str(Year_tax_Salary)
            Monlhly_tax_Salary_percentage = str(percentage) + '%'
            Yearly_tax_Salary_percentage = str(Yearly_tax_percentage) + '%'


            sql = 'update tax set Monlhly_tax_Salary=%s where EId=%s'
            d = (Monlhly_tax_Salary, Id)
            c = con.cursor()
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Monlhly_tax_Salary_percentage=%s where EId=%s'
            d = (Monlhly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary=%s where EId=%s'
            d = (Yearly_tax_Salary, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update tax set Yearly_tax_Salary_percentage=%s where EId=%s'
            d = (Yearly_tax_Salary_percentage, Id)
            c.execute(sql, d)
            con.commit()

            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("            Updated Employee's Tax Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Part_Time()

def Employees_Insurance(code):
    print("\n\n****-----****    ****-----****    ****-----****    ****-----****")
    print("                     Update Employee's Insurance Information")
    print("****-----****    ****-----****    ****-----****    ****-----****")
    Id = input("Enter Employee Id: ")
    if code == 1:
        if (administerhr_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            percentage = int(input("Enter the percentage of tax: "))
            sql = 'select  Monlhly_tax_Salary from tax where EId=%s'
            database = (Id,)
            c = con.cursor()
            c.execute(sql, database)
            r = c.fetchone()
            t = r[0]
            t1 = float(t)
            t2 = t1 * (percentage / 100)

            k = t1 - t2
            Insurance_Amount_monthely = str(k)
            Insurance_Monethely_percentage = str(percentage) + '%'

            sql = 'update insurance set Insurance_Amount_monthely=%s where EId=%s'
            d = (Insurance_Amount_monthely, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update insurance set Insurance_Monethely_percentage=%s where EId=%s'
            d = (Insurance_Monethely_percentage, Id)
            c.execute(sql, d)
            con.commit()
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Updated Employee's Insurance Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        AdministerHr_menu()
    elif code==2:
        if (General_FullTime_check_employee(Id) == False and administerhr_check_employee_Ta(Id) == False and administerhr_check_employee_In(Id) == False):
            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("     Sorry Sir,Employee does not exists.Please try again.")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        else:
            percentage = int(input("Enter the percentage of tax: "))
            sql = 'select  Monlhly_tax_Salary from tax where EId=%s'
            database = (Id,)
            c = con.cursor()
            c.execute(sql, database)
            r = c.fetchone()
            t =r[0]
            t1=float(t)
            t2=t1*(percentage / 100)

            k = t1 - t2
            Insurance_Amount_monthely = str(k)
            Insurance_Monethely_percentage = str(percentage) + '%'

            sql = 'update insurance set Insurance_Amount_monthely=%s where EId=%s'
            d = (Insurance_Amount_monthely, Id)
            c.execute(sql, d)
            con.commit()

            sql = 'update insurance set Insurance_Monethely_percentage=%s where EId=%s'
            d = (Insurance_Monethely_percentage, Id)
            c.execute(sql, d)
            con.commit()

            print("\n****-----****    ****-----****    ****-----****    ****-----****")
            print("           Updated Employee's Insurance Information Successfully")
            print("****-----****    ****-----****    ****-----****    ****-----****\n\n")
        Full_Time()

def administerhr_check_employee(id):
    sql = 'select * from administerhr_employee where AId=%s'
    c = con.cursor(buffered=True)
    data = (id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def administerhr_check_employee_Ta(id):
    sql = 'select * from tax where EId=%s'
    c = con.cursor(buffered=True)
    data = (id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def administerhr_check_employee_In(id):
    sql = 'select * from insurance where EId=%s'
    c = con.cursor(buffered=True)
    data = (id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def remove_taxe_info(Id):
    sql = 'delete from tax where EId=%s'
    data = (Id,)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    remove_insurance_info(Id)

def remove_insurance_info(Id):
    sql = 'delete from insurance where EId=%s'
    data = (Id,)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()

def tax_Add(EId,SSalary):
    Salary=int(SSalary)
    tax_Salary=Salary-(Salary*(15/100))
    Monlhly_tax_Salary_percentage='15%'
    Year_tax_Salary=tax_Salary*12
    Yearly_tax_Salary_percentage='180%'
    Monlhly_tax_Salary=str(tax_Salary)
    Yearly_tax_Salary=str(Year_tax_Salary)
    database = (EId, Monlhly_tax_Salary,  Monlhly_tax_Salary_percentage,  Yearly_tax_Salary, Yearly_tax_Salary_percentage)
    sql = 'insert tax values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, database)
    con.commit()
    insurance_Add(EId, tax_Salary)

def tax_AddP(EId,SSalary):
    Salary=int(SSalary)
    tax_Salary=Salary-(Salary*(15/100))
    Monlhly_tax_Salary_percentage='15%'

    Year_tax_Salary=tax_Salary*12
    Yearly_tax_Salary_percentage='180%'
    Monlhly_tax_Salary=str(tax_Salary)
    Yearly_tax_Salary=str(Year_tax_Salary)
    database = (EId, Monlhly_tax_Salary,  Monlhly_tax_Salary_percentage,  Yearly_tax_Salary, Yearly_tax_Salary_percentage)
    sql = 'insert tax values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, database)
    con.commit()

def insurance_Add(EId,SSalary):
    Salary=float(SSalary)
    Insurance_Salary=Salary-(Salary*(5/100))
    Insurance_Monethely_percentage='5%'
    Insurance_Amount_monthely=str(Insurance_Salary)
    database = (EId, Insurance_Amount_monthely,Insurance_Monethely_percentage)
    sql = 'insert insurance values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, database)
    con.commit()

def General_FullTime_check_employee(id):
    sql = 'select * from fulltime where FId=%s'
    c = con.cursor(buffered=True)
    data = (id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def General_PartTime_check_employee(id):
    sql = 'select * from parttime where PId=%s'
    c = con.cursor(buffered=True)
    data = (id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
menu()



