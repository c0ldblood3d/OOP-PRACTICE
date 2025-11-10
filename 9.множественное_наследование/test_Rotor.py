from Rotor import Rotorcraft

if __name__ == '__main__':
    print("Создание летательного аппарата Rotorcraft...")
    aircraft = Rotorcraft(
        flight_time=45,
        camera_resolution=20,
        rotor_diameter=10.5,
        fuel_capacity=350,
        max_altitude=4000,
        engine_power=120,
        rotor_type="Полуавтоматический",
        takeoff_distance=75,
        empty_weight=280
    )
    
    print("Тестирование методов полета...")
    aircraft.fly_vertical()
    
    print("Изменение характеристик...")
    aircraft.flight_time = 60
    aircraft.camera_resolution = 25
    aircraft.engine_power = 150
    
    print(f"Обновленное время полета: {aircraft.flight_time} мин")
    print(f"Обновленное разрешение камеры: {aircraft.camera_resolution} Мп")
    print(f"Обновленная мощность: {aircraft.engine_power} л.с.")