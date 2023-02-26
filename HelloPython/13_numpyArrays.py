# Lesson 13:
# Numpy Arrays (https://www.learnpython.org/en/Numpy_Arrays)
# based on lessons available at www.learnpython.org

# Note: You may need to install numpy via pip
# Python 2.x:
# pip install numpy
# Python 3.x:
# pip3 install numpy

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

# numpy arrays report a 'numpy.ndarray' type
print(type(np_height))

# Now we can perform element-wise calculations on height and weight.
# For example, you could take all 6 of the height and weight observations above,
# and calculate the BMI for each observation with a single equation.
#
# These operations are very fast and computationally efficient.
# They are particularly helpful when you have 1000s of observations in your data.
# bmi = weight (kg) / (height (m))²
bmi = np_weight / np_height ** 2
print(bmi)
print()
# Subsetting can also be done via numpy arrays

# returns a list with True if the element is greater than 23, False if not
print(bmi > 24)

# prints a list with entries where the boolean expression is True
print(bmi[bmi > 24])

print()
print("Exercise")

# Exercise

# First, convert the list of weights from a list to a Numpy array.
# Then, convert all of the weights from kilograms to pounds.
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
# Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print(np_weight_lbs)
