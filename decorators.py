from os import system
def boxing(func:object)->object:
    def wrapper(text: str)->None:
        print(" "+"_"*(1+len(text)))
        print('/'+"_"*(len(text))+"/|")
        print('|'+" "*(len(text))+"||")
        func("|"+text+"||")
        print('|'+"_"*(len(text))+'|/')
    return wrapper

@boxing
def text_render(text:str)->None:
    print(text)
def multi_by(multiplier: int)->object:
    def wrapper(multiplicand:str)->None:
        if multiplicand.isnumeric():
            multiplicand=int(multiplicand)
        else:
            multiplicand=0
        result=multiplier*multiplicand
        if result:
            text='{} is result of sum {} for {} times '.format(result,multiplicand,multiplier)
        else:
            text='input was not a number'
        return text
    return wrapper
 
multi_by3=multi_by(3)

if __name__=='__main__':
    system('clear')
    while True:
        text=input('multiplication by 3, sent a number  \n')
        system('clear')
        if text=='q':
            break
        text=multi_by3(text)
        text_render(text)
        print('press q to close')
