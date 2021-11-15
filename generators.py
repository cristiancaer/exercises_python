def fib_generator(max_output:int)->int:
    n1=0
    n2=1
    while True:
        yield n1
        n1,n2=n2,n1+n2
        if n1>max_output:
            break

if __name__=='__main__':
    numbers_fibo=fib_generator(20)
    for number in numbers_fibo:
        print(number)