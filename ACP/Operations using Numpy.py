import numpy as np
num = [0, 1, 2, 3,4 ,5 ,6 ,7 ,8 ,9]
arr = np.array(num)
for i in num:
    if i % 2 != 0:
        print(i, "is an odd number")
        new_arr = [-1 for i in arr if i%2 != 0] + [i for i in arr if i%2 == 0]
print(new_arr)