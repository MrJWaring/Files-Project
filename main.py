with open("students.txt", "r") as file:
    for line in file:
        for char in line:
            if char.isdigit():
                print(char)
                break