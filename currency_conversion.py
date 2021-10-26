from os import system
import requests
from bs4 import BeautifulSoup
import sys
class Currency_converser:
    def __init__(self) -> None:
        
        self.url="https://wise.com/es/currency-converter/usd-to-cop-rate"
        self.rate_dollar2cop=self.get_rate_dollar_cop()
        self.list_name_conversions=['Dollar to COP',
                                'COP to Dollar'
                                ]
        self.list_conversions=[self.dollar2cop,
                                    self.cop2dollar
                                    ]
    
    def dollar2cop(self,value):
        return value*self.rate_dollar2cop
    def cop2dollar(self,value):
        return value*(1/self.rate_dollar2cop)
    def get_rate_dollar_cop(self):
        response=requests.get(url=self.url)
     
        soup=BeautifulSoup(response.text,"html.parser")
        rate=soup.findAll('span',class_='text-success')[0]
        rate=rate.text.split(",")[0]
        rate=float(rate)
        return rate
    def menu(self):
        print('press q to exit')
        print('press a number:')
        for i,option in enumerate(self.list_name_conversions):
            print(f'{i}) ',option,)
        menu=input()
        if menu=='q':
            sys.exit()
        else:
            Value=float(input('sent value to exchange: '))
            change=self.list_conversions[menu](Value)
            print(change)
        
def main():
    converser=Currency_converser()
    
    while True:
        converser.menu()

if __name__=='__main__':
    main()