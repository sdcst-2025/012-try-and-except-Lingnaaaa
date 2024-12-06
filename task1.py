#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

x=input('Please enter in an integer number:')
try:
    x=int(x)
    print(x)
except Exception as e:
    print('This was an error, try again')
