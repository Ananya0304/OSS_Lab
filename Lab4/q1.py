import numpy as np
from collections import Counter
print("Numpy Version",np.__version__)
inp=(input("Enter input for list "))

f=inp.split()
frequency=Counter(f)
print("Frequency of each elment")
for element,count in frequency.items():
    print(f"{element}:{count}")