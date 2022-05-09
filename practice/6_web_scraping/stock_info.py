"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

from bs4 import BeautifulSoup
from requests import get
URL = 'https://finance.yahoo.com/most-active'
page = get(URL)
bs=BeautifulSoup(page.content,'html.parser')

title_=" 5 stocks with most youngest CEOs "
n="Name"
c="Code"
cntry="County"
empl="Employees"
ceo="CEO NAME"
ceo_yb="CEO Year Born"
header=(f'|{n:40}|{c:8}|{cntry:20}|{empl:16}|{ceo:30}|{ceo_yb:16}|')
how_many_stars=int(len(header)-len(title_)-2)/2

print("=" * int(how_many_stars), title_ , "=" * int(how_many_stars))
print(header)
print("-"*len(header))
for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
    company_code=company.get_text()
    company_name=company.get("title")
    company_link_profile='https://finance.yahoo.com'+"/quote/"+company_code+"/profile?p="+company_code
    """stąd pobierzemy nazwe CEO, liczbe pracownikow, kraj i kraj urodzenia"""
    company_link_key_statistics='https://finance.yahoo.com'+"/quote/"+company_code+"/key-statistics?p="+company_code
    #print(company_link_profile)
    #print(company_link_key_statistics)


    #bs_=BeautifulSoup(company_page_profile.content)
    #print(bs_)
    #for offer in bs_.find_all('p'):
    #    print(offer)

    print(f"|{company_name:40}| {company_code:8}|{company_code:20}|{company_code:16}|{company_code:30}|{company_code:16}|")