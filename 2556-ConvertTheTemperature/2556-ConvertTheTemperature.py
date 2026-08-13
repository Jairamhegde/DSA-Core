# Last updated: 8/13/2026, 8:19:38 PM
class Solution(object):
    def convertTemperature(self, celsius):
        
        fahranheit = celsius * 1.80 + 32.00
        Kelvin = celsius + 273.15
        return [Kelvin,fahranheit]


        