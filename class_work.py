from threading import Thread
from time import sleep
class ClassWork:
    def __init__(self) -> None:
        self.list_works=[self.work1,self.work2]
    def work1(self):
        while True:
            print('work 1')
            sleep(1)
    def work2(self):
        while True:
            print('work 2')
            sleep(2)
    def set_works(self):
        for target_function in self.list_works:
            work=Thread(target=target_function,daemon=True)
            work.start()
if __name__=='__main__':
     works=ClassWork()
     works.set_works()
     sleep(10)