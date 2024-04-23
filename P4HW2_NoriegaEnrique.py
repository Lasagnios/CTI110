##Enrique Noriega
##4/23/2024
##P4HW2
##Calculates multiple employees overtime and gross pay
totOvertime=0
totRegPay=0
totGrossPay=0
count=0
employee = input("Enter employee's name or 'Done' to terminate: ")
while employee != "Done":
    hrs = float(input("How many hours did " + employee + " work? "))
    rate = float(input("What is " +employee+ "'s pay rate? " ))
    print('-'*37)
    print("Employee name: " +employee)
    print('Hours Worked   Pay Rate       OverTime       OverTime Pay   RegHour Pay    Gross Pay')
    print('-'*90)
    if hrs >40:
        reg_pay= rate *40
        ovt_hrs= hrs-40
        ovt_rate= 1.5*rate
        ovt_pay= ovt_hrs*ovt_rate
        gross_pay= reg_pay + ovt_pay
    else:
        ovt_hrs=0
        ovt_pay=0
        reg_pay= rate *hrs
        gross_pay= reg_pay + ovt_pay
        totOvertime= totOvertime + ovt_pay
        totRegPay = totRegPay + reg_pay
        totGrossPay= totGrossPay + gross_pay
        count = count + 1
    print(f'{hrs:<15.2f}{rate:<15.2f}{ovt_hrs:<15.2f}{ovt_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')
    employee= input("Enter employees's name or 'Done' to terminate: ")
print()
print("Total number of employees entered: " + str(count))
print("Total amount paid for overtime: $" + str(format(totOvertime,'.2f')))
print("Total amount paid for regular hours: $" + str(format(totRegPay,'.2f')))
print("Total amound paid in gross: $" + str(format(totGrossPay,'.2f')))
