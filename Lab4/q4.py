import numpy as np
org=np.ones((3,3))
print("Original array:")
print(org)
org=np.pad(org,pad_width=1,mode='constant',constant_values=0)
print(org)