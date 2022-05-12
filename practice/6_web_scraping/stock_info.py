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
    companies=list()
    bs=cooking_soup_1()
    for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
        company_code = company.get_text()
        companies.append(company_code)
        #print(company_code)
    print(companies)


def get_company_name():
    companies_names=list()
    bs=cooking_soup_1()
    for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
        company_name = company.get("title")
        companies_names.append(company_name)
    print(companies_names)
    return companies_names

def get_page_to_get_country_and_CEO_details():
    comp_link_profiles=list()
    bs=cooking_soup_1()
    for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
        company_code = company.get_text()
        company_link_profile = 'https://finance.yahoo.com' + "/quote/" + company_code + "/profile?p=" + company_code
        comp_link_profiles.append(company_link_profile)
    return comp_link_profiles

def get_page_to_get_W52_details():
    comp_key_statistics=list()
    bs=cooking_soup_1()
    for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
        company_code = company.get_text()
        company_link_ks ='https://finance.yahoo.com' + "/quote/" + company_code + "/key-statistics?p=" + company_code
        comp_key_statistics.append(company_link_ks)
    return comp_key_statistics

def get_country():
    countries=list()
    urls = get_page_to_get_country_and_CEO_details()
    for i in urls:
        page=get(i,headers={'User-Agent': 'PostmanRuntime/7.29.0'})
        soup = BeautifulSoup(page.content, "html.parser")
        company=soup.find('div', class_="Mb(25px)")
        country = company.find('p', class_="D(ib) W(47.727%) Pend(40px)").get_text("_").split("_")[-3].split(",")[0]
        #print(footer)
        #print(country)
        countries.append(country)
    return countries

def get_empl_number():
    employ_numbers=list()
    urls = get_page_to_get_country_and_CEO_details()
    for i in urls:
        page=get(i,headers={'User-Agent': 'PostmanRuntime/7.29.0'})
        soup = BeautifulSoup(page.content, "html.parser")
        empl=soup.find('div', class_="Mb(25px)")
        country = empl.find('p', class_="D(ib) Va(t)")
        #print(footer)
        print(country)
        #employ_numbers.append(number_of_employees)






def count_stars_of_title(header,title_):
    how_many_stars = int(len(header) - len(title_) - 2) / 2
    return how_many_stars

def print_title_of_table():
    title_ = " 5 stocks with most youngest CEOs "
    return title_

def print_header():
    head=lets_build_header()
    title=print_title_of_table()
    x=count_stars_of_title(head,title)+1
    deco_header="=" * int(x) +title+ "=" * int(x)
    return deco_header

def lets_build_header():
    n="Name"
    c="Code"
    cntry="County"
    empl="Employees"
    ceo="CEO NAME"
    ceo_yb="CEO Year Born"
    header=(f'|{n:40}|{c:8}|{cntry:20}|{empl:16}|{ceo:30}|{ceo_yb:16}|')

    return header

def create_table():
    print(print_header())
    print(lets_build_header())
    print("-"*len(lets_build_header()))
    return None



"""for company in bs.find_all('a', class_="Fw(600) C($linkColor)"):
    company_code=company.get_text()
    company_name=company.get("title")
    company_link_profile='https://finance.yahoo.com'+"/quote/"+company_code+"/profile?p="+company_code"""
"""stąd pobierzemy nazwe CEO, liczbe pracownikow, kraj i kraj urodzenia
    company_link_key_statistics='https://finance.yahoo.com'+"/quote/"+company_code+"/key-statistics?p="+company_code
    company_page_profile=get(company_link_profile, headers={'User-Agent': 'PostmanRuntime/7.29.0'})
    #print(company_link_profile)
    #print(company_link_key_statistics)
    soup=BeautifulSoup(company_page_profile.content, "html.parser")
    footer=soup.find('div', class_="Mb(25px)")
    country=footer.find('p', class_="D(ib) W(47.727%) Pend(40px)").get_text("_").split("_")[-3]
    #print(footer)
    more_details=footer.find_all("span",class_="Fw(600)")
    employes=more_details[-1].get_text()"""


def main():
    create_table()
    get_company_code()
    get_company_name()
    print(get_page_to_get_country_and_CEO_details())
    print(get_page_to_get_W52_details())
    print(get_country())
    get_empl_number()


if __name__ == "__main__":
    main()



#print(f"|{company_name:40}| {company_code:8}|{country:20}|{company_code:16}|{company_code:30}|{company_code:16}|")