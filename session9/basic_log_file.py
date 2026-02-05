# write todays date to log.txt
# append "Program started"


with open("log.txt", "a") as file:
    file.write("2026-02-05\n")
    file.write("Program started\n")