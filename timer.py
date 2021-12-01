from threading import Timer
import time
class RepeatTimer(Timer):
    def run(self):
        print("outside while")
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
def dummyfn(msg="foo"):
    print(msg)

timer = RepeatTimer(0.1, dummyfn)
timer.cancel()
timer.start()
time.sleep(1)

timer = RepeatTimer(1, dummyfn,args=('foo2',))
timer.start()
time.sleep(2)
timer.cancel()