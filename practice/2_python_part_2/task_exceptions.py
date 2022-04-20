"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing


def division(x: int, y: int) -> typing.Union[None, int]: #użyć dekoratora?!

    try:
        result = float(x / y)
        print("Deletion finished")
        print(result)
        if y == 1:
            raise ValueError("Deletion on 1 get the same result")
    except  TypeError:
            print("Deletion finished")
            print("Podano nieprawidłową wartość")
    except ZeroDivisionError:
            print("Deletion finished")
            print("Division by 0")
    except ValueError as blad:
            print(blad)





division(1, 0)
print("*"*20) #ozdobniki wylacznie dla funu
division(1, 1)
print("-"*20)
division(2, "bulka")
print("."*20)
division(1,4)
division(10,1)
print("#"*20)
division("zero",7)
print("!"*20)
division(121,11)
def division(x: int, y: int) -> typing.Union[None, int]:
    ...
