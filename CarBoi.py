import requests
from bs4 import BeautifulSoup

while True:
    print("====================")
    reg = str(input("Enter registration number: "))
    url = 'https://www.mycarcheck.com/check?reg_no='+reg.replace(' ', '+')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    if soup.title.text == "Page not found - My Car Check":
        print("Registration number not found")
        continue
        
    for label, attr in zip(['Make', 'Body', 'Colr', 'Fuel', 'Year'],
                           [{'class': 'top-title'},
                            {'data-role': 'vehicle-identity-body-type'},
                            {'data-role': 'vehicle-identity-colour'},
                            {'data-role': 'vehicle-identity-fuel'},
                            {'data-role': 'vehicle-identity-year'}]):
        print("{}: {}".format(label, soup.find(attrs=attr).text))
