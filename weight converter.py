#!/usr/bin/env python
# coding: utf-8

# In[ ]:


weight = int(input("Please enter your weight: "))
unit = input("weight entered in (L)bs or (k)g ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f" you are {converted} pounds")

