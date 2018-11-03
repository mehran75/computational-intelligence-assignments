import numpy as np
# import time

n = int(input())

# 1: [n 0 n 0 n 0 n 0 ...n]
#  ****************this is faster*******
# t1 = time.time()
# a = [n if (i % 2 == 0) else 0 for i in range(n)]
# print('time in for loop: %d',(time.time() - t1))
# print(a)

# t1 = time.time()
a = np.array([n, 0] * (int(n/2)+1) )[:n]
# print('time with numpy: %d', (time.time() - t1))
print(a)
print('\n')

# 2: create n by n matrix started from n to n*n+n
b = np.arange(n, n * n + n).reshape(n, n)
print(b)
print('\n')

# 3: Lower triangle of matrix 'b'
c = np.tril(b)
print(c)
print('\n')

# 4: add a constant padding to zero matrix and store into d
d = np.pad(np.zeros((n - 2, n - 2), dtype=int), 1, mode='constant', constant_values=n)
print(d)
print('\n')

# 5: multiplication of matrix c and d and store it in e
e = np.matmul(c, d)
print(e)
print('\n')

# 6: if 'e' elements are grater than n power 3 -> inverse the element
n3 = n ** 3
f = np.where(e > n3, e * (-1), e)
print(f)
print('\n')

# 7: sum of min and max of matrix 'f'
print(np.min(f) + np.max(f))
