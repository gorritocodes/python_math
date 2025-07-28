import sympy
import math
from sympy import symbols

x = symbols('x')
equation = input('Enter the equation: ')

solution = sympy.solve(equation, x)

print(f'The solution is: {solution}')