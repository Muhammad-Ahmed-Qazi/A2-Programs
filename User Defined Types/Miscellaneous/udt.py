class student:
    
    def __init__(self):
        self.name = ""
        self.id = 0
        self.house = ""
        self.year = 0

while True:
    s = student()

    print("Enter student information: "	)
    s.name = input("Name: ")
    s.id = int(input("ID: "))
    s.house = input("House: ")
    s.year = int(input("Year: "))
    
    print("Student information confirmation: ")
    print("Name: " + s.name)
    print("ID: " + str(s.id))
    print("House: " + s.house)
    print("Year: " + str(s.year))
    print()