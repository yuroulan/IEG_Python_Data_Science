# create a list

qtt = [10, 20, 30, 40, 50]
newQtt = [5, 15, 25, 35, 45]
totQtt = zip(qtt, newQtt) # <<-- did not implemented __str__ method of zip class but obj class
print(totQtt)

print(list(totQtt)) # <<-- tuple

totQtt = [x + y for x, y in zip(qtt, newQtt)]
print(totQtt)

# need huge num

import time
import numpy as np

size = 1000000
lista = range(0, size)
listb = range(0, size)
numpya = np.arange(0, size)
numpyb = np.arange(0, size)

starttime = time.time()
c = [x + y for x, y in zip(lista, listb)]
print(time.time() - starttime)

starttime = time.time()
d = numpya + numpyb
print(time.time() - starttime)

print(c[0:10])
print(d[0:10])

