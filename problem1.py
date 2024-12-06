#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")


try:
    a=float(input('a:'))
    b=float(input('b:'))
    c=float(input("c:"))
    z=b**2-4*a*c
    if z>0:
       x=(-b+math.sqrt(z))/(2*a)
       x=round(x,2) 
       y=(-b-math.sqrt(z))/(2*a)
       y=round(y,2)
       print (f"The roots are {x} and {y}")
    if z ==0:
        root=-b/(2*a)
        root=round(root,2)
        print(f"The root is {root} and {root}")
    if z <0:
        print('There are no real roots to the equation')

except Exception as e:
    print('Those are not valid values for a, b or c')
