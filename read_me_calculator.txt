TASK - Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.

SOLUTION - I chose Dynamic Parsing of inputs as arithemetic operations can be performed on integer, float and complex datatypes in python.
I have taken the input manually and then passed the input in another function for performing the operation as the input function takes the input in string only so i had to cast it in formatted type entered by the user.

The isinstance() function is used in modulus and floor divison functions as in Python it is used to check whether an object (or a variable) is an instance or subclass of a particular class or a tuple of classes.
syntax- isinstance(object, classinfo)
It returns:
True: If the object is an instance of the class or classes specified in classinfo.
False: If the object is not an instance of the class or classes specified.

In the get() function the j in if condition represents "complex" number.
in elif condition . represents "float".
and else contains "integer".

after checking the datatypes the operations are performed as chosen by the user and result is provided in a formatted manner.