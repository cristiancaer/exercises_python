from os import system
import requests
from bs4 import BeautifulSoup
import sys
class Currency_converser:
    def __init__(self) -> None:
        self.rate_cop2dollar=0
        self.rate_cop2euro=0
        self.list_name_conversions=['COP',
                                    'Dollar',
                                    'euro'
                                ]
        self.list_rate_cop_to=[ 1,
                                self.get_rate_cop2dollar(),
                                self.get_rate_cop2euro()
                                ]
    
    def get_rate_cop2dollar(self):
        if not self.rate_cop2dollar:
            url="https://wise.com/es/currency-converter/usd-to-cop-rate"
            response=requests.get(url)
            soup=BeautifulSoup(response.text,"html.parser")
            rate=soup.findAll('span',class_='text-success')[0]
            rate=rate.text.split(",")[0]
            rate=float(rate)
            self.rate_cop2dollar=1/rate
        return self.rate_cop2dollar
    def get_rate_cop2euro(self):
        if not self.rate_cop2euro:
            url="https://wise.com/gb/currency-converter/cop-to-eur-rate"
            response=requests.get(url)
            soup=BeautifulSoup(response.text,"html.parser")
            rate=soup.findAll('span',class_='text-success')[0]
            rate=float(rate.text)
            self.rate_cop2euro=rate
        return self.rate_cop2euro

    def print_options(self):
        print('press a number:')
        for i,option in enumerate(self.list_name_conversions):
            print(f'{i}) ',option,)
    
    def menu(self):
        print('press q to exit')
        print('origen corrency')
        self.print_options()
        from_currency=input()
        if from_currency=='q':
            sys.exit()
       
        else:
            self.print_options()
            from_currency=int(from_currency)
            to_currency=int(input())
            print('insert value to exchange: ')
            value=float(input())
            conversion=(1/self.list_rate_cop_to[from_currency])*self.list_rate_cop_to[to_currency]*value
            print(f'result: {value} {self.list_name_conversions[from_currency]} are {conversion} {self.list_name_conversions[to_currency]}')
        
        
def main():
    converser=Currency_converser()
    
    while True:
        converser.menu()

if __name__=='__main__':
    main()