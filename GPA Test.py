#Xavier Randolph,GPA Tester, this program will take a students info and calculate if the theyve made the honor roll or deans list
while True:
    last_name = input("Enter your last name: (Enter ZZZ to quit) ")
    if last_name == "ZZZ":
        break

    first_name = input("Enter your first name: ")
    student_GPA = float(input("Enter your GPA: "))
    
    if student_GPA > 3.5:
        print(first_name + " " + last_name + " has made the Dean's List")
    elif student_GPA > 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll")
    elif student_GPA<3.25:
        print(first_name + " " + last_name + " has not made the list for either")