"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import requests



def make_request(url: str) -> Tuple[int, str]:
    resp=requests.get(url)
    response=resp.text[:1000]
    status_code = resp.status_code
    result:Tuple[int,str]=(status_code,response)
    print(result)
    return response


make_request('https://www.google.com')





"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
