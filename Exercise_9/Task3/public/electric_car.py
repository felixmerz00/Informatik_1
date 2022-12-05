#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if type(battery_size) != float or type(battery_range_km) != float or battery_size < 0 or battery_range_km < 0:
            raise Warning("Invalid input type")
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__c = battery_size


    def charge(self, kwh):
        if type(kwh) != float or kwh < 0:
            raise Warning("Invalid input type")
        self.__c += kwh
        if self.__c > self.__battery_size:
            self.__c = 0
            raise Warning("Battery overcharged")

    def get_battery_status(self):
        current_battery = self.__c
        max_battery = self.__battery_size
        return current_battery, max_battery

    def get_remaining_range(self):
        return self.__c/self.__battery_size*self.__battery_range_km

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input type")
        if self.get_remaining_range() < dist:
            self.__c = 0
            raise Warning("The battery empty")
        else:
            self.__c -= dist/self.__battery_range_km*self.__battery_size
