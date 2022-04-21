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

generate_files()