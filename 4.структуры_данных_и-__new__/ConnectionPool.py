class ConnectionPools:
    _connections = []
    pool_size = 8

    def __new__(cls, *args, **kwargs):
        if len(cls._connections) >= cls.pool_size:
            raise RuntimeError("Пул соединений полон!")
        else:
            instance = super().__new__(cls)
            cls._connections.append(instance)
            return instance
        
    def __init__(self, connection_id):
        self.id = connection_id
        self._active = True

    def __del__(self):
        self.release()
    
    def release(self):
        if self._active and self in self._connections:
            self._connections.remove(self)
            self._active = False



        