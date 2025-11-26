name = "Alan Turing"
age = "42"
person = [name, age, "mathematician"]
text = "Hello, my name is {}. I am {} years old and I am a {}.".format(person[0], person[1], person[2])
age_type = type(person[1])
print(text)
