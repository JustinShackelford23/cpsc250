class Person():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Hi, my name is {self.name}.')

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self):
        print(f'Hi, my name really is {self.name} and I am {self.student_id}.')

if __name__ == '__main__':
    s = Student("Alice","C001")
    s.introduce()