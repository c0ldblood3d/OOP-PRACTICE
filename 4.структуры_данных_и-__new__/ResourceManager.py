class ResourceManager:
    _manager = None
    
    def __new__(cls, *args, **kwargs):
        if cls._manager is None:
            cls._manager = super().__new__(cls)
        return cls._manager

    def __init__(self, resource_type=None, capacity=None, priority=None):
        if not hasattr(self, '_initialized'):
            self.resource_type = resource_type
            self.capacity = capacity
            self.priority = priority
            self._initialized = True
        
    def allocate(self):
         print(f'Выделено {self.capacity} ресурсов типа {self.resource_type} (приоритет: {self.priority})')
    
    def __del__(self):
        print("Освобождение ресурсов")
    
    def status(self):
        return "Ресурсы доступны"
    
    def release(self):
        print("Ресурсы освобождены")
    
    


    
