from threading import Timer
import time
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def dummyfn(msg="foo"):
    print(msg)

class TimerHandler:
    def __init__(self,interval,target_function,) -> None:
        self.timer=None
        self.interval=interval
        self.target_function=target_function
    def start(self):
        self.timer=RepeatTimer(self.interval,self.target_function)
        self.timer.setDaemon(True)
        self.timer.start()
    def change_interval(self,interval):
        self.interval=interval
        self.timer.cancel()
        self.start()
    def cancel(self):
        self.timer.cancel()

if __name__=='__main__':
    periode=1
    timer=TimerHandler(periode,dummyfn)
    timer.start()
    time.sleep(3)
    timer.change_interval(2)
    time.sleep(6)
