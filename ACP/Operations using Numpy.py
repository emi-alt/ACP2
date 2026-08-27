import numpy as np
num = [0, 1, 2, 3,4 ,5 ,6 ,7 ,8 ,9]
arr = np.array(num)
print("Original Array: ", arr)

modify = np.where(arr%2 != 0, -1, arr)
print("Modified Array: ", modify)

twoDarr = np.reshape(arr, (2, -1))
print("2D Array: ", twoDarr)

even_sum = 0
for i in arr:
    if i % 2 == 0:
        even_sum += i
print("Sum of Even Numbers: ", even_sum)