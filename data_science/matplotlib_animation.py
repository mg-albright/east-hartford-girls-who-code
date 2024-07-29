import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation#, writers
# import numpy as np

# Set up figure:
# It is good practice to start with plt.figure and set a figure size. 
# Here, the size is 7 inches by 5 inches
fig = plt.figure(figsize = (7,5))
# Set up axes:
# Here, when it says to add the subplot, the numbers given to it (1, 1, 1) are three integers: (number of rows, number of columns, index)
axes = fig.add_subplot(1,1,1)
# Set your y-axis to be from 0 to 300
axes.set_ylim(0, 300)
# choose colors for the bar plots
palette = ['blue', 'red', 'green', 
           'darkorange', 'maroon', 'black']

# Assign empty lists to each county we want to show 
# This is so we can add values to these lists later
india = []
china = []
germany = []
usa = []
canada = []
uk = []

# Define function 
def animation_function(i):
    india = i
    china = 5 * i
    germany = 3 * i
    usa = 2 * i
    canada = 6 * i
    uk = 3 * i

    plt.xlabel("Country")
    plt.ylabel("GDP of Country")

    plt.bar(["India", "China", "Germany", 
             "USA", "Canada", "UK"],
            [india, china, germany, usa, canada, uk],
            color = palette)

plt.title("Bar Chart Animation")

# Use the animation function! Documentation is here: https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
animation = FuncAnimation(fig, animation_function, 
                          interval = 50)
plt.show()
