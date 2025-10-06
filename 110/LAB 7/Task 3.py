import numpy as np
def reverseArray(arr):
  arr=arr[::-1]
  return arr

arr1 = np.array([10, 12, 20, 5, 7])
arr1 = reverseArray(arr1)
print(arr1)