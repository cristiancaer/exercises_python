from threading import Thread
import sys
from os import system
def is_palindrome(word:str)->bool:
    word=word.strip().lower()
    return word==word[::-1]

def run()->None:
    is_running=True
    system('clear')
    while is_running:
        word=input('Put a word to now if it is Palindrome: \n')
        system('clear')
        print('The word is ',end=' ')
        if word=='q':
            is_running=False
        if is_palindrome(word):
            print('Palindrome')
        else:
            print('Not a Palindrome')
        print('press q exit')
if __name__=='__main__':
    work=Thread(target=run)
    work.start()
    work.join()
