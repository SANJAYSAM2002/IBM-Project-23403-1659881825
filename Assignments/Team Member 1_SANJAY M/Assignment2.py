# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uc_VbO9N0q7102uXR4ONeFuH0Pt2upPC
""

import random

t = random.randint(0,100)
h = random.randint(0,100)

print("Temperature is = ",t)
print("Humidity is = ",h)

if t >60 and h > 60:
    print("alarm ON : It's seems to be risky")
elif t > 60 and h < 60:
    print("alarm ON : It's seems to be high temperature")
else:
    print("alarm OFF")
