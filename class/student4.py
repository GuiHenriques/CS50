class Student:
    def __init__(self, name, house):      
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", ]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name


def main():
    try:
        student = get_student()
        student.house = "Geneve"
        print(student)
    except Exception as e:
        print(e)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()
