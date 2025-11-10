import math

class WallAC:

    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

class Room:

    def __init__(self, width: int, length: int, height: int) -> None:
        self._width = width
        self._length = length
        self._height = height
        self._ac_list = []

    def add_ac(self, ac: WallAC) -> None:
        self._ac_list.append(ac)

    def get_area_to_cover(self) -> float:
        self._room_area = 2 * self._height * (self._width + self._length)
        self._ac_area = 0
        for i in range(len(self._ac_list)):
            self._ac_area += self._ac_list[i].get_area()
        return self._room_area - self._ac_area
    
    def get_wallpaper_rolls(self, roll_width: float, roll_length: float) -> int:
        self._roll_area = roll_length * roll_width
        return math.ceil((self._room_area - self._ac_area) / self._roll_area)
    



