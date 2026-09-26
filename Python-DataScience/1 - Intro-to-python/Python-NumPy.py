# to understand the essence of numpy take an examplewe have a list with weight and height and we want to calculate the BMI 
# to we cant just do it directly ....it will me less efficeint ot go through each item in the list one by one ..that is where numpy - numeric python comes in 
# Numpy array is similar to the python lists but provides more spec - allowing calclutaions

# here is our typical example 

height = [1.2,1.3,1.4,1.5,1.6]
weight = [2.3,2.4,2.5,2.6,2.7]

# if we try getting the bmi
print(bmi = (weight / height ** 2))

# the above gies us an error 

# with numpy arrays this works like magic 

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height **2

# this is possible since np arrays can only contain items of the same type 
# if you try to mix types they all default to strings 
# they also come with its methods

# we can use the comparison of values result to make a selction criteria

# point to know - the arithmetic operators work different from python lists



# 2DNUmpyarrays
# we can create 2D arrays from reular python lists of lists
# we can get more info about 2dnparrays using attributes but they are not the same as mehtods  eg n2d.shape
 