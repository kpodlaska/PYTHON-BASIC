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

def cooking_soup_1():
    URL = 'https://finance.yahoo.com/most-active'
    page = get(URL)
    bs=BeautifulSoup(page.content,'html.parser')
    return bs

def get_company_code():
    for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
        company_code = company.get_text()
    #dokonczyc - trzeba stworzyc slownik gdzies wyzej

def count_stars_of_title(header,title_):
    how_many_stars = int(len(header) - len(title_) - 2) / 2
    return how_many_stars

def print_title_of_table():
    title_ = " 5 stocks with most youngest CEOs "
    return title_

def print_header():
    how_many_stars=count_stars_of_title(lets_build_header(),print_title_of_table())
    title=print_title_of_table()
    print("=" * int(how_many_stars), title, "=" * int(how_many_stars))

def lets_build_header():
    n="Name"
    c="Code"
    cntry="County"
    empl="Employees"
    ceo="CEO NAME"
    ceo_yb="CEO Year Born"
    header=(f'|{n:40}|{c:8}|{cntry:20}|{empl:16}|{ceo:30}|{ceo_yb:16}|')

    return header



for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
    company_code=company.get_text()
    company_name=company.get("title")
    company_link_profile='https://finance.yahoo.com'+"/quote/"+company_code+"/profile?p="+company_code
    """stąd pobierzemy nazwe CEO, liczbe pracownikow, kraj i kraj urodzenia"""
    company_link_key_statistics='https://finance.yahoo.com'+"/quote/"+company_code+"/key-statistics?p="+company_code
    company_page_profile=get(company_link_profile, headers={'User-Agent': 'PostmanRuntime/7.29.0'})
    #print(company_link_profile)
    #print(company_link_key_statistics)
    soup=BeautifulSoup(company_page_profile.content, "html.parser")
    footer=soup.find('div', class_="Mb(25px)")
    country=footer.find('p', class_="D(ib) W(47.727%) Pend(40px)").get_text("_").split("_")[-3]
    #print(footer)
    more_details=footer.find_all("span",class_="Fw(600)")
    employes=more_details[-1].get_text()


def main():
    print_header()
    h=lets_build_header()
    print(h)
    print("-"*len(h))


if __name__ == "__main__":
    main()



#print(f"|{company_name:40}| {company_code:8}|{country:20}|{company_code:16}|{company_code:30}|{company_code:16}|")