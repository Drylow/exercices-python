def final_grade(exam_grade, completed_projects):
    if exam_grade > 90 or completed_projects > 10:
        return 100
    elif exam_grade > 75 and completed_projects >= 5:
        return 90
    elif exam_grade > 50 and completed_projects >= 2:
        return 75
    else:
        return 0

exam = int(input("Enter the exam grade (0-100) : "))
projects = int(input("Enter the number of completed projects : "))
print("Final grade :", final_grade(exam, projects))