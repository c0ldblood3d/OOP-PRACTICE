from Bicycle import Bicycle, Vehicle

Vehicles = []
Vehicles.append(Vehicle("Toyota", "Camry", 2020, "Седан"))
Vehicles.append(Vehicle("Honda", "CR-V", 2021, "Внедорожник"))
Vehicles.append(Bicycle("Trek", "Marlin 5", 2022, "Горный велосипед", "19"))
Vehicles.append(Bicycle("Giant", "Escape 3", 2023, "Городской велосипед", "M"))
Vehicles.append(Vehicle("Ford", "Focus", 2019, "Хэтчбек"))

for i in Vehicles:
    print(i.Describe())
