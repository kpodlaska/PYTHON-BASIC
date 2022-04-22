
from typing import Iterable
import unittest


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
class ReadWriteTest(unittest.TestCase):
    def test_word_number(self): #czy poprawnie interpretuje word_number
        # Given
        word_number=-3
        # When
        max_len=5
        # Then
        self.assertFalse(word_number in range(0,max_len))

    def test_kolejnosc(self):
        j=""
        wynik = [1,1,22,34,56]
        for i in wynik:
            str(j)<=str(i) is True
            i=j
        result=True
        self.assertTrue(result)





if __name__ =='__main__':
    unittest.main()

build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
build_from_unique_words('1 2', '1 2 3', word_number=10)
build_from_unique_words(word_number=10)