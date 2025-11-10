import random
from typing import Tuple

class Rocket:
    _num_list: list[str] = [f'Ракета_{i}' for i in range(1,15)]
    _mas_list: list[str] = ['Спутник', 'Грузовой модуль', 'Экипаж', 'Научное оборудование']

    def __init__(self) -> None:
        self._name = random.choice(self._num_list)
        self._payload = random.choice(self._mas_list)

    def get_info(self) -> Tuple[str, str]:
        return (self._name, self._payload)

class RocketTrain:

    def __init__(self) -> None:
        self._train: list[Rocket] = [Rocket() for i in range(56)]

    def shuffle(self) -> None:
        random.shuffle(self._train)

    def get(self, i: int) -> Rocket:
        return self._train[i]
    
    def get_count(self) -> int:
        return len(self._train)
    
    
    


    