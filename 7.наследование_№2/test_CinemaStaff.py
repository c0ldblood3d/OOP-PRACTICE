from CinemaStaff import CinemaStaff, Projectionist, Usher, CleanRobot

cleany = CleanRobot("Cleany-3000")
print(cleany.work())
print(cleany.giveRaise(5000))
print(f"Текущая зарплата: {cleany.salary}")
print(f"Представление объекта: {repr(cleany)}")
    
staff_members = [
    CinemaStaff("Иван Петров", 35000),
    Projectionist("Алексей Сидоров"),
    Usher("Мария Иванова"),
    CleanRobot("Робоклинер-2000")
    ]
    
for employee in staff_members:
    print(employee.work())

    
