sumGrossPay = 0
employeeCount = 0
print("Do you want to continue?")
response = input()
while response == "yes":
    print("Enter employee last name")
    lastName = input()
    print("Enter hours worked")
    hoursWorked = float(input())
    print("Enter rate of pay")
    rateOfPay = float(input())
    if hoursWorked > 40:
        grossPay = 40 * rateOfPay + hoursWorked - 40 * rateOfPay * 1.5
    else:
        grossPay = hoursWorked * rateOfPay
    print(lastName)
    print(grossPay)
    sumGrossPay = sumGrossPay + grossPay
    employeeCount = employeeCount + 1
    print("Would you like to add another employee?")
    response = input()
averagePay = sumGrossPay / employeeCount
print("Total gross pay:")
print(sumGrossPay)
print("Number of employees:")
print(employeeCount)
print("Average Pay:")
print(averagePay)
