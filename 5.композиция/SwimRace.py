from random import randint

class Swimmer:

    def __init__(self, name:str, health:int = 100) -> None:
        self._name = name
        self._health = health

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def swim_lap(self) -> int:
        return randint(10, 30)
    
    def __str__(self):
        return f'Пловец {self._name}, его здоровье: {self._health}'
    
class SwimRace:

    def __init__(self, swimmer1:Swimmer, swimmer2:Swimmer) -> None:
        self.swimmer1 = swimmer1
        self.swimmer2 = swimmer2

    def race(self) -> None:
        while self.swimmer1._health > 0 and self.swimmer2._health > 0:
            self.swimmer2._health -= self.swimmer1.swim_lap()

            if self.swimmer2._health <= 0:
                break

            self.swimmer1._health -= self.swimmer2.swim_lap()

            if self.swimmer1._health <= 0:
                break

    def announce_medal(self) -> str:
        if self.swimmer1._health <= 0:
            return 'Победил второй пловец!'
        elif self.swimmer2._health <= 0:
            return 'Победил первый пловец!'



    



