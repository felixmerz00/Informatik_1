#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if type(gas_capacity) != float or type(gas_per_100km) != float or gas_capacity < 0 or gas_per_100km < 0:
            raise Warning("Invalid input type")
        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__c = gas_capacity


    def fuel(self, f):
        if type(f) != float or f < 0:
            raise Warning("Invalid input type")
        self.__c += f
        if self.__c > self.__gas_capacity:
            self.__c = 0
            raise Warning("Gas tank overfilled")

    def get_gas_tank_status(self):
        status = self.__c
        capacity = self.__gas_capacity
        return status, capacity

    def get_remaining_range(self):
        return self.__c/self.__gas_per_100km*100

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input type")
        if self.get_remaining_range() < dist:
            self.__c = 0
            raise Warning("Fuel is depleted")
        else:
            self.__c -= dist/100*self.__gas_per_100km
