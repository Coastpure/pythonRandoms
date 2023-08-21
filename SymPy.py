# Math using sympy library
import sympy
import math
from sympy import symbols, factor, expand, diff, integrate, limit, oo

x = symbols("x")
y = symbols("y")

formula = x ** 2

print(diff(sympy.exp(x)))
print(diff(sympy.sin(x) + sympy.cos(x) ))

print(integrate(2 ** x, (x, 0, 10)))

print(integrate(sympy.sin(x), (x, -oo, oo)))            # from negative infinity to infinity
print(integrate(sympy.sin(x**2), (x, -oo, oo)))
print(integrate(1 / (x ** 4 + 1), (x, 0, oo)))

# expression = 2 * (x + y)
# print(integrate(2 ** x + 2 ** y, x))
#
# print(factor(expression))
# # print(expression - x)
#
# expression2 = x ** 2 + x * y
# print(factor(expression2))
#
# expression3 = x * (x + y)
# print(expand(expression3))