name = input("Enter name: ")

with open("output.log", "a") as file:
    file.write("Program started\n")
    file.write(f"User: {name}\n")
    file.write("Program ended!")