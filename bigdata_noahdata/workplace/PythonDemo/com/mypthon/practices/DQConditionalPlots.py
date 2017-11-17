'''
Created on 01-Nov-2017

@author: bigdata
'''

# Make a get request with the parameters.
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    # Add your code here.
    plt.show()
def draw_secant1(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    
    x_0 = x_values[0]
    x_1 = x_values[1]
    y_0 = -1*(x_0**2) + x_0*3 - 1
    y_1 = -1*(x_1**2) + x_1*3 - 1
    m = (y_1 - y_0) / (x_1 - x_0)
    b = y_1 - m*x_1
    
    y_secant = x*m + b
    plt.plot(x, y_secant, c='green')
    plt.show()
def job_opt():
    x=np.linspace(0,50,1000)
    print x 
    y1=1000+30*x
    y2=100+50*x
    plt.plot(x, y1, c='orange')
    plt.plot(x, y2, c='blue')
    plt.show()
job_opt()    
#draw_secant1([3,5])
#draw_secant1([3,10])
#draw_secant1([3,15])

