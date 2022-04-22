"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.
Example:
    Input: ['abc', 'def', 'xyz']
    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import unittest

def generate_files():
    words=[]
    with open("input_file.txt") as input_file:
        for line in input_file:
            content=line.strip()
            words.append(content)

    print(words)

    verso=(words[::-1])
    print(verso)

    with open("test_file_1.txt", "w", encoding="utf8") as output_file:
        for word in words:
                output_file.write(f"{word}\n")

    #odwrócona kolejność
    with open("test_file_2.txt","w",encoding="cp1252") as output_2:
        for word in verso:
            output_2.write(f"{word}, ")
class ReadWriteTest(unittest.TestCase):
    def test_czytanie(self): #czy program czyta plik wejsciowy
        # Given
        with open("input_file.txt") as otwarty:
            testowy=otwarty.readline()
        # When
        powinno_byc="cztery\n"
        # Then
        self.assertEqual(powinno_byc,testowy)


    def test_zapisywanie(self): #czy program czyta plik wyjsciowy_1
        #Given
        with open("test_file_1.txt") as otwarty2:
            testowy2=otwarty2.readline()
        # When
        powinno_byc="cztery\n"
        # Then
        self.assertEqual(powinno_byc, testowy2)



if __name__ =='__main__':
    unittest.main()