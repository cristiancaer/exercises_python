def is_odd(value):return value%2==0

def run():
    while True:
        try:

            value=input('what number do you wan to check if it is odd: ')
            # assert value.isnumeric(),'must be an integer number'
            value=int(value)
            assert value>0," value must be positive number"
            print(is_odd(value))

        except (ValueError, TypeError):
            print('value must be a integer number')

        SyntaxError
        ValueError

        
if __name__=='__main__':
    run()