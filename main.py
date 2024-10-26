print('Lesson2. Python OOP')


class Marker:
    color: str
    thikness: int
    isAvailable: bool

    def __init__(self, color, thikness, isAvailabe = True):
        self.color = color
        self.thikness = thikness
        self.isAvailable = isAvailabe

    def get_info(self):
        print('general info:')
        if self.isAvailable:
            print(f'\tcolor-{self.color} | thk - {self.thikness}')
        else:
            print('\tthis marker is absent in storage')


markerRed = Marker('red', 2)
markerRed.get_info()
markerRed.color = 'black'
markerRed.get_info()
