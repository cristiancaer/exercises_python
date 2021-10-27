import random
class KeyGenerator:
    abc_lowercase=tuple(letter for letter in "abcdefghijklmnopqrstuvwxyz")
    abc_uppercase=tuple(letter.capitalize() for letter in abc_lowercase)
    numbers=tuple(str(i) for i in range(0,10))
    symbols=tuple(symbol for symbol in "@/_-*+$&%#")
    available_charecters=abc_lowercase+abc_uppercase+numbers+symbols
    
    def maker(self,length_key):
        key=''
        for i in range(length_key):
            key+=random.choice(self.available_charecters)
        return key

    def __str__(self) -> str:
        return f'available characters: \n {self.available_charecters}'

def run():
    key_gen=KeyGenerator()
    print(key_gen)
    key=key_gen.maker(5)
    print('new key: ')
    print(key)

if __name__=='__main__':
    run()