class Employee:
    staff = {}

    def __new__(cls, name, department):
        if not name.startswith('emp_'):
            raise ValueError("Сотрудник должен иметь префикс 'emp_'")
        emp_id = name[4:]
        instance = super().__new__(cls)
        cls.staff[emp_id] = instance
        setattr(instance, f"e{emp_id}", department)
        return instance
    
    def __init__(self, name, department):
        pass
    

    
