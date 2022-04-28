"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math


def math_calculate(function: str, *args):

    if function=="log":
        result=len(list(args)) #sprawdza ilosc argumentow
        math_result=math.log(args[0],args[1])
        print(result)
        print(math_result)
    elif function=="ceil":
        result=len(list(args))
        math_result=math.ceil(args[0])
        print(result)
        print(math_result)
    else:
         print("nie ma takiej funkcji")
math_calculate("log", 1024 , 2)
math_calculate('ceil', 10.7)





"""
Write tests for math_calculate function
"""
