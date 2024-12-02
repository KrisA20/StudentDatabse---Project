# Define student class
# Steps1: Create a list dictionary to store students
# Steps2: Store the students inputted into the dictionary alongside their coressponding information
# Steps3: Create a fuction where Upon entering a name for the student their releveant information is pulled up
# Steps4: Create a functuon where students course can be updated aswell a their address
# Steps5: Create the menu for the Teacher/User that will display all different options to access dictionary


Studentlist = []
Student_database = {}


class Student:
    def __init__(self, name, address, date_of_birth, course):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.course = course

    def printName (self):
        print("Name          :", self.name)
        print("Address       :", self.address)
        print("Date Of Birth :", self.date_of_birth)
        print("Course       :", self.course)
        print(25 * "-")

    def updateCourse (self):
        self.course = input("Pleas enter the updated course")


    def createStudent ():
        name = input("Please enter the students FULL name       :")
        address = input("Please enter the address               :")
        date_of_birth = input("Please enter the DOB             :")
        course = input("Please enter the course                 :")
        return Student(name, address, date_of_birth, course,)
    
def menu ():
    print ("To look up a student in the database please press:" "[1]")
    print ("To update a students course please press:"          "[2]")
    print ("To update a students address please press:"         "[3]")
    print ("To add a new student please press:"                 "[4]")
    print ("To exit please press:"                              "[9]")

menu()
option = int(input("Please select your option: "))

while option != 9:

    if option == 1:
        lookup_name = input("Please enter the student's  name to lookup: " )
        if lookup_name in Student_database:
            Student_database[lookup_name].printName()
            menu()
        else:
            print ("There are no students matching that information")
            menu()


    elif option == 2:
        update_name = input("Please enter the students name you wish to update: ")
        if update_name in Student_database:
            Student_database[update_name].updateCourse()
            print ("Course succesfully updated")

            menu()
        else:
            print ("No student found with that name")

    elif option == 3:
        update_name = input("Enter the name of the student to update the address:")
        if update_name in Student_database:
            new_address = input("Enter the new adress: ")
            Student_database[update_name].address = new_address
            print ("Adress succesfully updated")
            student.printName()

        menu()

    elif option == 4:
        StudentCount = int(input("How many students are you going to add? "))

        for x in range(StudentCount):
            new_student = Student.createStudent()
            Student_database[new_student.name] = new_student
            print("\nStudent Information Database:")
            for student in Student_database.values():
                student.printName()

        menu()
        option = int(input("Please select your option"))


    else:
        print("Invalid option")
        menu()

print ("Goodbye")
        

    


