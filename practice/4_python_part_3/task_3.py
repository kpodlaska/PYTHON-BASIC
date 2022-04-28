"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    pattern_to_search=re.compile(r'http')
    matches=pattern_to_search.finditer(domain)
    result=[]
    for match in matches:
        result.append(match)

    if len(result)==0:
        print(f'False. domena {domain} NIE zawiera http')
    else:
        print(f'True. domenta {domain} zawiera http')


is_http_domain('griddynamics.com')
is_http_domain('https://ru.wikipedia.org/')


"""
write tests for is_http_domain function
"""