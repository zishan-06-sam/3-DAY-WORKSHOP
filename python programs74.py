def sin_series(x, terms=10):
    total = 0
    sign = 1
    power = x
    fact = 1
    for n in range(1, terms + 1):
        total += sign * power / fact
        
        power *= x * x
        fact *= (2 * n) * (2 * n + 1)
        sign *= -1
    return total

import math
x = math.pi / 6  # 30 degrees
print(sin_series(x))       
print(math.sin(x))         