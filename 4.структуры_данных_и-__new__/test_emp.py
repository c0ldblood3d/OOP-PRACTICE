from Employee import Employee

e1 = Employee('emp_001', 'IT')
e2 = Employee('emp_002', 'HR')
try: 
    e3 = Employee('worker_003', 'IT')
except ValueError as e:
    print(f"Ошибка: {e}")

print(e1.e001)
print(e2.e002)

print(Employee.staff)