import course_manager

file_path = r"C:\Users\koroz\90-days-coding\day-09\day09_miniproject\courses.json"

courses = course_manager.load_courses(file_path)

while True:
    options = {
        1: "View Course",
        2: "View Course Statistics",
        3: "Find Courses",
        4: "View Top Students",
        5: "Rank Courses",
        6: "Add Student",
        7: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Choose an option: ")
    if option == "1":
        print(courses)
    elif option == "2":
        print(course_manager.course_statistics(courses))
    elif option == "3":
        category = input("Category: ")
        if not category.strip():
            category = None
        while True:
            has_students = input("Has students? (yes/no/any): ")
            if has_students.lower() == "yes":
                has_students = True
                break
            elif has_students.lower() == "no":
                has_students = False
                break
            elif has_students.lower() == "any":
                has_students = None
                break
            else:
                print("Please type (yes/no/any)!")
        find = course_manager.find_courses(courses, category, has_students)
        if find:
            print(find)
        else:
            print("Courses were not found!")
    elif option == "4":
        for student in course_manager.top_students(courses):
            print(student)
    elif option == "5":
        for index, course in enumerate(course_manager.rank_courses(courses), start=1):
            print(f"{index}. {course['name']}")
    elif option == "6":
        while True:
            course_name = input("Course name: ")
            if course_name.strip():
                break
            else:
                print("Type course name!")
        while True:
            student_name = input("Student name: ")
            if student_name.strip():
                break
            else:
                print("Type a name!")
        while True:
            try:
                score = int(input("Score: "))
                break
            except ValueError:
                print("Type an integer!")
        while True:
            completed = input("completed? (yes/no): ")
            if completed.lower() == "yes":
                completed = True
                break
            elif completed.lower() == "no":
                completed = False
                break
            else:
                print("Please Type (yes/no)!")
        student = {
            "name": student_name,
            "score": score,
            "completed": completed
        }
        add = course_manager.add_student(courses, course_name, student)
        if add:
            course_manager.save_courses(courses, file_path)
            print("Student was added!")
        else:
            print("Student was not added!")
    elif option == "7":
        break
    else:
        print("Invalid option!")


            
            

