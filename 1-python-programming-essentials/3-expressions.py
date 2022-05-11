"""
1 - simple expressions
plus, minus - positive + / negative -
addition, subtraction, multiplication - if int and int then int; if int and float then convert to float
division / - if int and int then float; if int and float then float
integer division // - throwing away the fractional part, and follow with int or float 
exponentiation **

2 - compound expressions
compound expressions - operator precedence
exponentiation > multiplication/division > addition/subtraction > positive/negative
in the same level use left to right
use parentheses to change evaluation order - do this first

"""

"""
Demonstration of simple arithmetic expressions in Python
"""

# Unary + and -
print("Unary operators")
print(+3)
print(-5)
print(+7.86)
print(-3348.63)

print("")

# Simple arithmetic
print("Addition and Subtraction")
print(1 + 2)
print(48 - 89)
print(3.45 + 2.7)
print(87.3384 - 12.35)
print(3 + 6.7)
print(9.8 - 4)

print("")

print("Multiplication")
print(3 * 2)
print(7.8 * 27.54)
print(7 * 8.2)

print("")

print("Division")
print(8 / 2)
print(3 / 2)
print(7.538 / 14.3)
print(8 // 2)
print(3 // 2)
print(7.538 // 14.3)

print("")

print("Exponentiation")
print(3 ** 2)
print(5 ** 4)
print(32.6 ** 7)
print(9 ** 0.5)

"""
Demonstration of compound arithmetic expressions in Python
"""

# Expressions can include multiple operations
print("Compound expressions")
print(3 + 5 + 7 + 27)
print(18 - 6 + 4)

print("")

# Operator precedence defines how expressions are evaluated
print("Operator precedence")
print(7 + 3 * 5)
print(5.5 * 6 // 2 + 8)
print(-3 ** 2)

print("")

# Use parentheses to change evaluation order
print("Grouping with parentheses")
print((7 + 3) * 5)
print(5.5 * ((6 // 2) + 8))
print((-3) ** 2)
