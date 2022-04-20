"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    wynik = []
    pomocnicza = line.split(" ")
    print("lista wejsciowa :", pomocnicza)
    for x in pomocnicza:
        if x not in wynik:
            wynik.append(x)
    print("wynik w postaci listy:", wynik)
    wynik = [' '.join([str(i) for i in wynik])]
    print("wynik w postaci jednoelemtowej listy", wynik)
    print("wynik jako string", wynik[0])
    print("*********")  # dla czytelnosci


remove_duplicated_words('cat dog 3')
remove_duplicated_words('cat cat dog 1 dog 2')
remove_duplicated_words('1 2 3')
remove_duplicated_words('1 2 3 4 5 12 13 2 2 2 3 silly word')
remove_duplicated_words('1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1')
remove_duplicated_words('cat dog cat cat cat monkey dog dog dog dog dog dog cat cat cat cat cat cat')
