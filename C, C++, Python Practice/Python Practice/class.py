class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.__age})"
if __name__ == "__main__":
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)

    print(student1)
    print(student2)
    print(student1.name)
    print(student2._Student__age)
    student1.__age = 21
    print(student1)
    student2.name = "Charlie"
    print(student2)
     
""" class Student:
    name="Krish"
s1=Student()
print(s1.name)
s2=Student()
print(s2.name) """