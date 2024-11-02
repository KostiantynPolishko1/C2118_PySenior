print('Lesson 4: Class Inharitance\n')


class Person:
    second_name: str
    first_name: str
    stat = 'male'
    age = 22

    def __init__(self, second_name: str, first_name: str):
        self.first_name = first_name
        self.second_name = second_name

    def __str__(self):
        person_info = f'{self.second_name} {self.first_name}, вік {self.age}, стать {self.stat}'
        return f'{person_info}\n'


class SchoolChild(Person):
    activity: str

    def __init__(self, second_name, first_name):
        self.activity = 'studying'
        self.second_name = second_name
        self.first_name = first_name

    def __str__(self):
        person_info = Person.__str__(self)
        return f'{person_info}main activity {self.activity}'


KnyshTimur = SchoolChild('Книш', 'Тімур')
print(KnyshTimur)


class Teacher:
    pass


class HeadManger(Person):
    activity: str

    def __init__(self, second_name, first_name):
        self.activity = 'management'
        self.second_name = second_name
        self.first_name = first_name

    def __str__(self):
        person_info = Person.__str__(self)
        return f'{person_info}main activity {self.activity}'


