
from time  import sleep, time

class Fiboiter:
    def __init__(self,maxi) -> None:
        self.max=maxi

    def __iter__(self)->object:
        self.buffer=[0,0]
        return self

    def __next__(self)->int:
        counter=sum(self.buffer)
        self.buffer=[self.buffer[1],counter]
        # sow seed to start
        if counter==0:
            self.buffer[0]=1
        if counter>self.max:
            raise StopIteration
    
        return counter
if __name__=='__main__':
    numbers_fibo=Fiboiter(20)
    for number in numbers_fibo:
        print(number)
        sleep(1)

