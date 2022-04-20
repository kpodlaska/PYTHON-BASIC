"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)
Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
plik=open("dużo_liczb.txt","w")
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:

    file=open(filename,"r")
    lines=file.readlines()
    file.close()

    for i in lines:
        print(f'lines:{i}')
    print(lines)
    pomocnicza_tablica=[]
    for i in lines:
        tymczasowe=i.strip()
        print(tymczasowe)
        pomocnicza_tablica.append(tymczasowe)


    print(pomocnicza_tablica)

    print("a teraz zapis w formacie jaki chce zadanie:")
    wynik=[]
    min_arg=min(pomocnicza_tablica)
    wynik.append(min_arg)
    max_arg=max(pomocnicza_tablica)
    wynik.append(max_arg)
    wynik2=(min(pomocnicza_tablica),max(pomocnicza_tablica))
    #print(wynik) #wynik uzyskany dla porównania
    print(wynik2)
get_min_max("tekst1.txt")
get_min_max("tekst2.txt")
get_min_max("same_parzyste.txt")
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    ...

