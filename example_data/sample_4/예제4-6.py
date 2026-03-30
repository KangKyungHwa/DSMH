import numpy as np
 
list1 = [[1,2], [3,4]]
list2 = [[5,6], [7,8]]

a = np.array(list1)
b = np.array(list2)

c=np.add(a, b)
print(c)
 
c = np.dot(a, b)
print(c)
