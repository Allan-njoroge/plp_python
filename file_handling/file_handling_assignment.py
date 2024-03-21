with open ("my_file.txt", "w") as file:
    file.write("1. My name is Allan Njoroge\n")
    file.write("2. I'm 19 years old\n")
    file.write("3. I love programming\n")

# Displaying the information
try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line)

except FileNotFoundError:
    print("File cannot be found")

except PermissionError:
    print("You do not have access to this file")

# Appending three additional lines to the file
try:   
    with open ("my_file.txt", "a") as file:
        file.write("4. I am also a student\n")
        file.write("5. I go to school at KCA University\n")
        file.write("6. The best team is Manchester United\n")

except FileNotFoundError:
    print("File cannot be found")

except PermissionError:
    print("You do not have access to this file")