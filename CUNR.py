from functools import reduce

n = 920

result = reduce(lambda a, b : a*b % 10**6, range(2* n - 5,1,-2))

print(result)