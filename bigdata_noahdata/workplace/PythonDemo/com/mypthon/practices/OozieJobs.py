'''
Created on 29-Aug-2017

@author: bigdata
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urwid.text_layout import line_width
women_degrees=pd.read_csv("/tmp/mozilla_bigdata0/percent-bachelors-degrees-women-usa.csv")
print women_degrees.columns
# plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
# plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
# plt.legend(loc='upper right')
# plt.title('Percentage of Biology Degrees Awarded By Gender')
# plt.show()
# fig, ax = plt.subplots()
# ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
# ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
# ax.spines["right"].set_visible(False)
# ax.tick_params(bottom="off", top="off", left="off", right="off")
# ax.set_title('Percentage of Biology Degrees Awarded By Gender')
# ax.legend(loc="upper right")
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(20, 20))
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women',linewidth=4)
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men',linewidth=4)
    for key,spine in ax.spines.items():
        spine.set_visible(True)
        
    ax.set_xlim(1968, 2011)
    ax.text(1970, 0, "starting point")
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="on", top="off", left="on", right="off") 
              
            
    plt.legend(loc='upper right')
    
    # Add your code here.

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.show()
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')

plt.legend(loc='upper right')
plt.show()
