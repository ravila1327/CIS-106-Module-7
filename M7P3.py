studentCount = 0
print("Do you want to continue? Yes or No")
studentCount = 0
response = input()
while response == "yes":
    print("Enter last name:")
    lastName = input()
    print("Enter Exam 1 score.")
    exam1 = float(input())
    print("Enter Exam 2 score.")
    exam2 = float(input())
    average = exam1 + exam2 / 2
    print(lastName)
    print(average)
    studentCount = studentCount + 1
    print("Enter another student?")
    response = input()
print("Number of Students:")
print(studentCount)
