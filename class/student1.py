class Student:
    ...

def main():
    student = get_student()
    print(name, "is from", house)

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()