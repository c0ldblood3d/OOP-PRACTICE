from Rocket import RocketTrain

rt = RocketTrain()
rt.shuffle()

selected_rockets = set()
total_rockets = rt.get_count()

while len(selected_rockets) < total_rockets:
    try:
        user_input = input('Введите целое число от 0 до 55 или q для выхода: ')
        
        if user_input == 'q':
            print('Завершение программы')
            break

        rocket_number = int(user_input)
        if rocket_number < 0 and rocket_number > 55:
            print('Номер должен быть в диапазоне от 0 до 55')
            continue

        if rocket_number in selected_rockets:
            print(f"Ракета №{rocket_number} уже была выбрана ранее!")
            continue
        
        rocket = rt.get(rocket_number)
        rocket_name, rocket_payload = rocket.get_info()
        print(f"Выбрана: {rocket_name} с нагрузкой: {rocket_payload}")
        selected_rockets.add(rocket_number)

    except ValueError:
        print("Ошибка: введите целое число или 'q' для выхода")
    except IndexError as e:
        print(f"Ошибка: {e}")
        