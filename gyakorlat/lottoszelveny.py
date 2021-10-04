# HF: hányféleképpen tudom kitölteni
# az ötös lottó szelvényt

import math

n = 90
k = 5

result, i = 1, 1
while i <= k:
    result = result * (n - k + i) / i
    i += 1

print(result)
