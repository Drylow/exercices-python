students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
alphabetical_students = sorted(students)
print("Students in alphabetical order :", alphabetical_students)

nameStartingWithM = []
for student in students:
    if student.startswith("M"):
        nameStartingWithM.append(student)

print("Students whose names start with M :", nameStartingWithM)

