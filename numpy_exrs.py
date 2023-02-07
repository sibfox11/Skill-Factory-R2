import numpy as np
"""
print(2**16)
print(np.iinfo(np.int64))
print(-9223372036854775808*2)
print(np.sctypeDict)
print(len(np.sctypeDict))
"""
#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

#print(np.uint8(-456))

arr = np.array([1,5,2,9,10])
print(arr.dtype)