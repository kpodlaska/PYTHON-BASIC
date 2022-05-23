import os
from random import randint
import threading


OUTPUT_DIR: str = '/Users/kpodlaska/Desktop/python/output'
RESULT_FILE = 'Users/kpodlaska/Desktop/python/output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1
"""generate list of fibonacci numbers"""

def fib_list(n):
    fib_list=[]
    for i in range(0,n):
        x=fib(i)
        fib_list.append(x)
    return fib_list

#def func1(array: list):
def func1(n):
    fibs=fib_list(n)
    print(fibs)
    for index,fib in enumerate(fibs):
        file_name = str(index) + ".txt"
        file_txt = os.path.join(OUTPUT_DIR, file_name)

        print(file_name,file_txt)
        with open(file_txt,"w") as file:
            file.write(str(fib))
        print(index,fib)

        lista=os.listdir(OUTPUT_DIR)
    print(lista)


    print("end")


#def func2(result_file: str):
#    print("wywołałem funckję 2")

#for _ in range(10):
#    threading.Thread(target=func1).start()

func1(10_000)

"""

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    func1(array=[randint(1_000, 100_000) for _ in range(1_000)])
    func2(result_file=RESULT_FILE)
"""