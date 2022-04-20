"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)] /1^2-(0^2-0)
"""
from typing import List

def calculate_power_with_difference(ints: List[int]) -> List[int]:
    x=enumerate(ints)
    y=(list(x))
    wynik=[]
    #print(y)
    for i in range(len(y)):
        if i == 0:
            z=y[i][1]
            #print("wartosc",i,"tego elementu wynosi",z)
            #print("dla pierwszego elementu nic nie odejmiemy")
            kwadrat=z**2
            wynik.append(kwadrat)
        else:
          z=y[i][1]
          #print("wartosc",i,"tego elementu wynosi",z)
          kwadrat = z**2-((z-1)**2-(z-1))
          wynik.append(kwadrat)
    print(wynik)
calculate_power_with_difference([1, 2, 3])
calculate_power_with_difference([4,6,9])
calculate_power_with_difference([-1,4,5,2,3,6,7])