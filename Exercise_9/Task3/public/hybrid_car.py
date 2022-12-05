#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

class HybridCar(ElectricCar, CombustionCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if type(gas_capacity) != float != type(battery_size) != type(battery_range_km) != type(battery_size) or gas_capacity < 0 or battery_size < 0 or battery_range_km < 0:
            raise Warning("Invalid input type")
        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__c_e = battery_size
        self.__c_c = gas_capacity
        self.__drive_electric = True

    def switch_to_combustion(self):
        self.__drive_electric = False

    def switch_to_electric(self):
        self.__drive_electric = True

    def get_remaining_range(self):
        return self.__c_e/self.__battery_size*self.__battery_range_km + self.__c_c/self.__gas_per_100km*100

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input type")
        if dist > self.get_remaining_range():
            self.__c_e = 0
            self.__c_c = 0
            raise Warning("Both tanks are empty")

        if self.__drive_electric and self.__c_e > 0:
            self.__c_e -= dist/self.__battery_range_km*self.__battery_size
            if self.__c_e < 0:
                dist = abs(self.__c_e)/self.__battery_size*self.__battery_range_km
                self.__c_e = 0
                self.__drive_electric = False
                self.drive(dist)
        else:
            self.__c_c -= self.__gas_per_100km/100*dist
            if self.__c_c < 0:
                dist = abs(self.__c_c / self.__gas_per_100km * 100)
                self.__c_c = 0
                self.__drive_electric = True
                self.drive(dist)
    

    def get_gas_tank_status(self):
        status = self.__c_c
        capacity = self.__gas_capacity
        return status, capacity

    def get_battery_status(self):
        current_battery = self.__c_e
        max_battery = self.__battery_size
        return current_battery, max_battery

    def charge(self, kwh):
        if type(kwh) != float or kwh < 0:
            raise Warning("Invalid input type")
        self.__c_e += kwh
        if self.__c_e > self.__battery_size:
            self.__c_e = 0
            raise Warning("Battery overcharged")

    def fuel(self, f):
        if type(f) != float or f < 0:
            raise Warning("Invalid input Type")
        self.__c_c += f
        if self.__c_c > self.__gas_capacity:
            self.__c_c = 0
            raise Warning("Gas Tank overfilled")