'''
Created on 28-Aug-2017

@author: bigdata
'''
import math  
class Pizza(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
 
    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)
 
    @classmethod
    def compute_volume(cls, height, radius):
        return height * cls.compute_area(radius)
 
    def get_volume(self):
        return self.compute_volume(self.height, self.radius)
 
        
pi=Pizza(23,45) 
print pi.get_volume()
print Pizza.compute_volume(2, 3)
print Pizza.compute_area(2)    

months = { 1 : "January",
         2 : "February",
        3 : "March",
        4 : "April",
         5 : "May",
         6 : "June",
        7 : "July",
        8 : "August",
         9 : "September",
        10 : "October",
        11 : "November"}
months[12]="December"
print months   
