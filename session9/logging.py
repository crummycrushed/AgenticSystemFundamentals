name = input("Enter name: ")

with open("output.log", "a") as file:
    file.write(f"User: {name}\n")
