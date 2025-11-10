from Instrument import Instrument, Guitar, Piano

instrument1 = Instrument("Базовый инструмент", "Generic", 500, 4, 10)
guitar1 = Guitar("Акустическая гитара", "Yamaha", 15000)
piano1 = Piano("Рояль", "Steinway", 250000)
    
print("\n1. Базовый инструмент:")
instrument1.describe()
instrument1.play_style()
instrument1.material()
print(f"Рассчитанная громкость: {instrument1.calculate()}")
    
print("\n2. Гитара:")
guitar1.describe()
guitar1.play_style()
guitar1.material()
print(f"Цена за струну: {guitar1.calculate()} руб.")
    
print("\n3. Пианино:")
piano1.describe()
piano1.play_style()
piano1.material()
print(f"Количество октав: {piano1.calculate()}")
    
instruments = [
        Instrument("Универсальный", "BrandX", 1000, 8, 12),
        Guitar("Электрогитара", "Fender", 45000),
        Piano("Пианино", "Kawai", 120000),
        Guitar("Бас-гитара", "Ibanez", 28000),
        Piano("Синтезатор", "Roland", 80000)
    ]
    
for i, instrument in enumerate(instruments, 1):
    print(f"\nИнструмент {i}")
    instrument.describe()
    print("Способ игры:", end=" ")
    instrument.play_style()
    print("Материал:", end=" ")
    instrument.material()
    result = instrument.calculate()
    print(f"Результат calculate(): {result}")
    print(f"Тип объекта: {type(instrument).__name__}")