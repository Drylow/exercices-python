def sum_of_students(students_list: list) -> int:
    total_students = 0
    
    for group in students_list:
        total_students += len(group)
        
    return total_students

student_data = [
    ["Jean", "Alice", "Edwige", "Peter", "James"],
    ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]
]

result = sum_of_students(student_data)
print(f"The list of students contains {result} students.") 

student_data_2 = [
    ["Marc"],
    ["Sophie", "Lucas"],
    ["Paul", "Marie", "Léa"]
]
result_2 = sum_of_students(student_data_2)
print(f"The second list of students contains {result_2} students.")