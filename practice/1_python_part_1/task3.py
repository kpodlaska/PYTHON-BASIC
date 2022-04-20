"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    x = enumerate(lines)
    y = (list(x))
    wynik = ""
    if word_number < 0:
        print("niepoprawna wartość word_number")
    elif word_number >= len(y):
        print("")
        print("word number poza zakresem")
    else:
        # print("nasza lista elementów: ",len(y))
        for i in range(len(y)):
            z = y[i][1]
            w = z.split(" ")
            w.sort()
            usuniete_duplikaty = list(set(w))
            wynik = wynik + " " + usuniete_duplikaty[word_number]

    print(wynik)


print("*******testy*****")

build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
build_from_unique_words('1 2', '1 2 3', word_number=10)
build_from_unique_words(word_number=10)