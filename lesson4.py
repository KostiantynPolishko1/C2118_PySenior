# print('Lesson 3: Work with several classes\n')


class StudySubject:
    name: str
    hours: int
    level: str

    def __init__(self, name: str, hours: int, level: str):
        self.name = name
        self.hours = hours
        self.level = level

    def __str__(self):
        return f'{self.name} {self.level}, кількість годин {self.hours}'


class Student:
    first_name: str
    second_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject

    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject, is_offline=True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_offline = is_offline
        self.study_subject = study_subject

    def __str__(self):

        study_type: str
        if self.is_offline:
            study_type = 'offline'
        else:
            study_type = 'online'

        student_info = f'{self.second_name} {self.first_name}, вік {self.age}, навчається {study_type}'

        return f'{student_info}\n{self.study_subject}'


py_senior = StudySubject('Python', 18, 'Senior')
DushlyukMakar = Student('Дишлюк', "Макар", 13, py_senior)

# (DushlyukMakar)

