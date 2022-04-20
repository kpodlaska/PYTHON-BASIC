"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.
Example:
    Input:
    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")
    Output:
    result.txt(content: "23, 78, 3")
"""

result=[]
readable_file=''
while readable_file!="koniec":
    readable_file=input('podaj nazwe pliku w formacie text.txt, jesli chcesz zakonczyc napisz [koniec] ')
    with open(readable_file) as content:
        line = content.readline()
        result.append(line)
        print(result)
    with open("result.txt", 'w') as output_file:
        for line in result:
            output_file.write(f"{line}\n")