class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return f"{self.name} teachs {self.subject}"

student = Student("Harry", "Gryffindor")
professor = Professor("Dumble", "Attack")
print(student, professor)