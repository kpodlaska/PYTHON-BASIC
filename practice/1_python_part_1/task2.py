""""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    x = dict_to_update.items()
    print(x)
    y = dict_to_update.keys()
    print(y)
    z = dict_to_update.values()
    print(z)
    for x in items_to_set:

        if dict_to_update[x] < items_to_set[x] and len(dict_to_update) > 0:
            print("zmienna ", x, "do podmiany przyjmuje wartosc", dict_to_update[x])
            print("zmienna ", x, "zostaje podmieniona na", items_to_set[x])
            print("dlugosc slownika wynosi", len(dict_to_update))
            dict_to_update[x] = items_to_set[x]
        elif len(dict_to_update) == 0:
            dict_to_update = type(items_to_set.split("="))
            print(dict_to_update)

    print(dict_to_update)
    print("*****koniec testu******")


print("testy")
set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4, c=7)
set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
set_to_dict({'a': 5})
set_to_dict({}, a=0)