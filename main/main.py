from abc import ABC, abstractmethod


class PrintInterface(ABC):
    @abstractmethod
    def create(self, name, age):
        pass

    @abstractmethod
    def method_print(self):
        pass


class Student(PrintInterface):
    def create(self, name, age, groupNumber):
        self.Name = name
        self.Age = age
        self.GroupNumber = groupNumber

    def method_print(self):
        print("########################")
        print(self.Name)
        print(self.Age)
        print(self.GroupNumber)
        print("########################")


class Teacher(PrintInterface):
    def create(self, name, age, subject):
        self.Name = name
        self.Age = age
        self.Subject = subject

    def method_print(self):
        print("////////////////////////")
        print(self.Name)
        print(self.Age)
        print(self.Subject)
        print("////////////////////////")


class User:
    def __init__(self, person: PrintInterface):
        self.Realization = person


class Car:
    pass


if __name__ == "__main__":
    print("main start")
    student = Student()
    user = User(person=student)
    user.Realization.create("Ivan", 20, "Б20-782-1")
    user.Realization.method_print()

    teacher = Teacher()
    user = User(person=teacher)
    user.Realization.create("Vasia", 40, "Algebra")
    user.Realization.method_print()




class Ma:
    pass