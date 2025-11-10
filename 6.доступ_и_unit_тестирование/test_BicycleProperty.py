from BicycleProperty import BicycleProperty

mybike1 = BicycleProperty(max_speed=25, capacity=1, luggage_spaces=2)
mybike2 = BicycleProperty(max_speed=35, capacity=2, luggage_spaces=4) 
mybike3 = BicycleProperty(max_speed=20, capacity=1, luggage_spaces=1)
    
mybike1.speed = 15
mybike1.distance = 100
mybike1.passengers = ["Alice"]
mybike1.luggage = ["backpack"]
    
mybike2.speed = 25
mybike2.distance = 200
mybike2.passengers = ["Bob", "Charlie"]
mybike2.luggage = ["bag1", "bag2", "tent"]
    

mybike3.speed = 10
mybike3.distance = 50
mybike3.passengers = ["David"]
mybike3.luggage = ["small_bag"]
    

print("mybike1:")
print(f"  Скорость: {mybike1.speed}")
print(f"  Пассажиры: {mybike1.passengers}")
print(f"  Багаж: {mybike1.luggage}")
    
print("\nmybike2:")
print(f"  Скорость: {mybike2.speed}")
print(f"  Пассажиры: {mybike2.passengers}")
print(f"  Багаж: {mybike2.luggage}")
    
print("\nmybike3:")
print(f"  Скорость: {mybike3.speed}")
print(f"  Пассажиры: {mybike3.passengers}")
print(f"  Багаж: {mybike3.luggage}")