import student_manager


file_path = r"C:\Users\koroz\90-days-coding\day-05\day05miniproject\students.json"

students = student_manager.load_students(file_path)

options = {
        1: "View Students",
        2: "View Students Averages",
        3: "View Top Student",
        4: "View Students Above Average",
        5: "Add Student",
        6: "Add Score",
        7: "Exit"
    }
while True:
    for key,value in options.items():
        print(f"{key}. {value}")
    option = input("Choose an option: ")
    if option == "1":
        for student in students:
            print(student['name'])
    elif option == "2":
        for student, average in student_manager.student_averages(students).items():
            print(f"{student}: {average}")
    elif option == "3":
        print(student_manager.top_student(students))
    elif option == "4":
        for student in student_manager.students_above_average(students):
            print(student)
    elif option == "5":
            while True:
                student_name = input("Type the name of a student to add: ")
                if student_name.strip():
                    break
                else:
                    print("Enter a student!")
            while True:
                student_score = input("Type the scores of the student: ")
                if student_score.strip():
                    try:
                        list_ = student_score.split()
                        scores = [int(score) for score in list_]
                        break
                    except ValueError:
                        print("Type numbers for the scores!")
                else: 
                    print("Enter a score!")
            student_manager.add_student(students, student_name, scores)
            student_manager.save_students(students, file_path)
    elif option == "6":
        while True:
            students_name = input("Type the students name: ")
            if students_name.strip():
                break
        while True:
            try:
                score = int(input("Type score to add: "))
                break
            except ValueError:
                print("Type an integer!")
        add = student_manager.add_score(students, students_name, score)
        if add:
            student_manager.save_students(students, file_path)
            print("Score was added!")
        else:
            print("Student was not found!")
    elif option == "7":
        break
    else:
        print("Invalid option")
                

            

