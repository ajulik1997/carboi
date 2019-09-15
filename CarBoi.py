import requests
from bs4 import BeautifulSoup

print('This is just a test and convenience script so only use the XXXX XXX format, anything else will just crash it.')

while True:
    print('====================')
    reg = input('Enter car reg : ')
    url = 'https://www.mycarcheck.com/check/?reg_no='+reg[0:4]+'+'+reg[-3:]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    make = soup.find('h3', attrs={'class': 'make-model'}).text.strip()
    body = soup.findAll('td', attrs={'class': 'col-xs-9'})[0].text.strip()
    colour = soup.findAll('td', attrs={'class': 'col-xs-9'})[1].text.strip()

    print('Make:', make)
    print('Body:', body)
    print('Colour:', colour)
