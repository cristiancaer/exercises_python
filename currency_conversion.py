from os import system
import requests
from bs4 import BeautifulSoup
import sys
class Currency_converser:
    def __init__(self) -> None:
        self.rate_cop2dollar=0
        self.rate_cop2euro=0
        self.conversion=0
        self.list_name_conversions=['COP',
                                    'Dollar',
                                    'euro'
                                ]
        self.list_rate_cop_to=[ 1,
                                self.get_rate_cop2dollar(),
                                self.get_rate_cop2euro()
                                ]
    def get_rate_cop2another_from_url(self,url):
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        rate=soup.findAll('span',class_='text-success')[0]
        rate=rate.text.replace(',','.')
        rate=float(rate)
        return rate
    def get_rate_cop2dollar(self):
        if not self.rate_cop2dollar:
            url="https://wise.com/es/currency-converter/cop-to-usd-rate"
            self.rate_cop2dollar=self.get_rate_cop2another_from_url(url)
        return self.rate_cop2dollar
    def get_rate_cop2euro(self):
        if not self.rate_cop2euro:
            url="https://wise.com/gb/currency-converter/cop-to-eur-rate"
            self.rate_cop2euro=self.get_rate_cop2another_from_url(url)
        return self.rate_cop2euro

    def print_options(self):
        print('press a number:')
        for i,option in enumerate(self.list_name_conversions):
            print(f'{i+1}) ',option,)
    
    def menu(self):
        system('clear')
        if self.conversion:
            print(f'result: {self.value} {self.list_name_conversions[self.from_currency]} are {self.conversion} {self.list_name_conversions[self.to_currency]}')
            print('''
            
            ''')
        print('press q to exit')
        print('currency converser')
        print('origen corrency')
        self.print_options()
        self.from_currency=input()
        if self.from_currency=='q':
            sys.exit()
        else:
            self.from_currency=int(self.from_currency)-1
            print("to corrency")
            self.print_options()
            self.to_currency=int(input())-1
            print('insert value to exchange: ')
            self.value=float(input())
            self.conversion=(1/self.list_rate_cop_to[self.from_currency])*self.list_rate_cop_to[self.to_currency]*self.value
            self.conversion=round(self.conversion,2)


def run():
    converser=Currency_converser()
    while True:
        converser.menu()

if __name__=='__main__':
    run()