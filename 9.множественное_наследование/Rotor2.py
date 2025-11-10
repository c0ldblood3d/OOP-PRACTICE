class Drone:

    def __init__(self, flight_time, camera_resolution, **kwargs):
        self.__flight_time = flight_time
        self.__camera_resolution = camera_resolution
        super().__init__(**kwargs)

    @property
    def flight_time(self):
        return self.__flight_time
    
    @flight_time.setter
    def flight_time(self, new_flight_time):
        self.__flight_time = new_flight_time

    @property
    def camera_resolution(self):
        return self.__camera_resolution
    
    @camera_resolution.setter
    def camera_resolution(self, new_camera_resolution):
        self.__camera_resolution = new_camera_resolution

    def take_off(self):
        print('take off')
    
    def hover(self):
        print('hover')
    
class Helicopter:

    def __init__(self, rotor_diameter, fuel_capacity, max_altitude, **kwargs):
        self.__rotor_diameter = rotor_diameter
        self.__fuel_capacity = fuel_capacity
        self.__max_altitude = max_altitude
        super().__init__(**kwargs)

    @property
    def rotor_diameter(self):
        return self.__rotor_diameter
    
    @rotor_diameter.setter
    def rotor_diameter(self, value):
        self.__rotor_diameter = value
    
    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self.__fuel_capacity = value
    
    @property
    def max_altitude(self):
        return self.__max_altitude
    
    @max_altitude.setter
    def max_altitude(self, value):
        self.__max_altitude = value

    def start_rotors(self):
        print('start rotor')
    
    def hover(self):
        print('hover')
    
    def land(self):
        print('land')

class Gyrocopter:
    def __init__(self, engine_power, rotor_type, takeoff_distance, empty_weight, **kwargs):
        self._engine_power = engine_power
        self._rotor_type = rotor_type
        self._takeoff_distance = takeoff_distance
        self._empty_weight = empty_weight
        super().__init__(**kwargs)
    
    @property
    def engine_power(self):
        return self._engine_power
    
    @engine_power.setter
    def engine_power(self, value):
        self._engine_power = value
    
    @property
    def rotor_type(self):
        return self._rotor_type
    
    @rotor_type.setter
    def rotor_type(self, value):
        self._rotor_type = value
    
    @property
    def takeoff_distance(self):
        return self._takeoff_distance
    
    @takeoff_distance.setter
    def takeoff_distance(self, value):
        self._takeoff_distance = value
    
    @property
    def empty_weight(self):
        return self._empty_weight
    
    @empty_weight.setter
    def empty_weight(self, value):
        self._empty_weight = value
    
    def spin_rotor(self):
        print('spin_rotor')

class Rotorcraft(Drone, Helicopter, Gyrocopter):
    def __init__(self, flight_time, camera_resolution, rotor_diameter, fuel_capacity, max_altitude, engine_power, rotor_type, takeoff_distance, empty_weight):
        super().__init__(
            flight_time=flight_time,
            camera_resolution=camera_resolution,
            rotor_diameter=rotor_diameter,
            fuel_capacity=fuel_capacity,
            max_altitude=max_altitude,
            engine_power=engine_power,
            rotor_type=rotor_type,
            takeoff_distance=takeoff_distance,
            empty_weight=empty_weight
        )

    def fly_vertical(self):
        self.take_off()
        self.start_rotors()
        self.spin_rotor()

        self.hover()
        self.hover()

        self.land()



