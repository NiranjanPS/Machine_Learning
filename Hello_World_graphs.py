# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:37:34 2019

@author: niranjans4
"""

print("Hello WOrld")

import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,10,0,-5,6,11,55,36] 
# corresponding y axis values 
y = [1,5,3,25,56,0,-11,23,-65,75] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 


left = [0, 3, 6, 4, 5] 
  
# heights of bars 
height = [10, 24, 36, 40, 5] 
  
# labels for bars 
tick_label = ['one', 'nir', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 

  
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = False, explode = (0.05, 0, 0, 0), 
        radius = 1, autopct = '%1.1f%%') 
  
# plotting legend 
#plt.legend() 
  
# showing the plot 
#plt.show() 