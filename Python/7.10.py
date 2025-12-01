languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

element = input("Enter a language: ")

if element in languages[0]:
    print(f"{element} is a backend language ?")
elif element in languages[1]:
    print(f"{element} is a frontend language ?")
else:
    print("Language not found in the lists.")