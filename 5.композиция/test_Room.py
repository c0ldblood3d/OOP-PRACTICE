from Room import Room
from Room import WallAC

room1 = Room(5, 4, 2)
print(f"Площадь под оклейку: {room1.get_area_to_cover()}")
print(f"Рулонов обоев: {room1.get_wallpaper_rolls(0.53, 10)}")
print()
    
room2 = Room(6, 4, 2)
ac1 = WallAC(0.8, 0.6)
room2.add_ac(ac1)
print(f"Площадь под оклейку: {room2.get_area_to_cover()}")
print(f"Рулонов обоев: {room2.get_wallpaper_rolls(0.53, 10)}")
print()
    
room3 = Room(8, 5, 3)
ac2 = WallAC(1.0, 0.7)
ac3 = WallAC(0.9, 0.5)
room3.add_ac(ac2)
room3.add_ac(ac3)
print(f"Площадь под оклейку: {room3.get_area_to_cover()}")
print(f"Рулонов обоев: {room3.get_wallpaper_rolls(1.06, 10)}")
print()

