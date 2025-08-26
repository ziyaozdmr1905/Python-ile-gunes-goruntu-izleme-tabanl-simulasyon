
"""
import numpy as np


np_array = np.array([1,2,3,4,5,6,7,8,9])

multi = [[1,2,3] , [4,5,6], [7,8,9]]
np_multi = np_array.reshape(3,3)


"""

#res = np.arange(1,10)


import pandas as pd


numbers = [20,30,40,50]
letters = ['a','b','c','d']

#pandas_seri = pd.Series(numbers)

#pandas_seri = pd.Series(letters)
pandas_seri = pd.Series(numbers, letters)


print(pandas_seri)
print("zıya")
