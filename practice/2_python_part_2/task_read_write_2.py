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


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)
    print(words)
    verso=(words[::-1])
    print(verso)

    with open("file1.txt", "w", encoding="utf8") as output_file:
        for word in words:
                output_file.write(f"{word}\n")

    #odwrócona kolejność
    with open("file2.txt","w",encoding="cp1252") as output_2:
        for word in verso:
            output_2.write(f"{word} ,")


generate_words(20)
