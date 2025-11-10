class CinemaStaff:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def giveRaise(self, amount=1000):
        self.salary += amount

    def work(self):
        return 'Работает'
    
    def __repr__(self):
        return f'name: {self.name}, salary: {self.salary}'
    
class Projectionist(CinemaStaff):

    def __init__(self, name):
        super().__init__(name, salary=40000)

    def work(self):
        return 'Фильм запущен!'
    
class Usher(CinemaStaff):

    def __init__(self, name):
        super().__init__(name, salary=30000)

    def work(self):
        return 'Раздача попкорна'
    
class CleanRobot(Usher):

    def __init__(self, name):
        super().__init__(name)
        self.salary = 20000

    def work(self):
        return 'Уборка зала'
    
