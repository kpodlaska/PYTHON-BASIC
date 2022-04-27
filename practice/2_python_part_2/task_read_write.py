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
import os
result=[]
listdir = '/Users/kpodlaska/PycharmProjects/pythonProject/PYTHON-BASIC/practice/2_python_part_2/'
for f_name in os.listdir('/Users/kpodlaska/PycharmProjects/pythonProject/PYTHON-BASIC/practice/2_python_part_2/'):
    if f_name.endswith('.txt'):
         with open(f_name) as content:
              line=content.readline()
              result.append(line)

         with open("result.txt","w") as output_file:
               for line in result:
                    output_file.write(f"{line}, ")
"""edytowalam program tak by zapisywal zawartosc wszystkich plikow z danego folderu.
 plik wynikowy nie jest "dopieszczony" glownie dlatego ze w folderze znajduja sie pliki wynikowe innego cwiczenia
 i ich uklad nie jest jednorodny 
 w wolnej chwili to przemyslenia jak zapisac to ladniej - do zabawy z result"""