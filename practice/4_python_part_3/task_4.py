"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider - ma same
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from faker import Faker
fake = Faker()
"""generate some names"""
for _ in range(number_of_fakes):
    print(fake.name(),fake.address())

"""def print_name_address(args: argparse.Namespace) -> None:
    #creating fake address
    #random number + space + field from dict - download readable file with US zip codes or something ;)
    #then prepare recipe for building fake address
    person=[some_name]
    fake_address=random.randrange(1,999)+' '+random.choice(fake_street_names)+" "+random.choice(fake_cities_names)
    print(fake_address)
    person.append(fake_address)
    print(person)

if __name__=="__main__":
    print(print_name_address)




"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
