school_class = {}

menu = """
1 - Add New Student
2 - Add Point
3 - Calculate Average Score
-1 - Exit
"""

operation = 0
while operation != -1:
    try:
        operation = int(input(menu))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if operation == 1:
        name = input("Name: ").strip()
        if name not in school_class:
            school_class[name] = []
            print("Student successfully created!")
        else:
            print("Already exists!")

    elif operation == 2:
        name = input("Enter student name: ").strip()
        if name in school_class:
            try:
                grade = int(input("Grade (1-10): "))
                if 1 <= grade <= 10:
                    school_class[name].append(grade)
                    print("Grade added!")
                else:
                    print("Grade must be between 1 and 10!")
            except ValueError:
                print("Invalid grade! Please enter a number.")
        else:
            print("Student doesn't exist!")

    elif operation == 3:
        if not school_class:
            print("There are no students yet!")
        else:
            for name, grades in school_class.items():
                if grades:
                    avg = sum(grades) / len(grades)
                    print(f"{name}: {grades} | avg: {avg:.2f}")
                else:
                    print(f"{name} has no grades yet!")

    elif operation != -1:
        print("Invalid option! Please choose a correct number.")
