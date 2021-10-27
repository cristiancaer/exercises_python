from threading import Thread, ThreadError
from time import sleep
from datetime import datetime
def work(check_running,id):
    while check_running():
        print('from worker ', id)
        print(datetime.now())
        sleep(1)
    print("end work", id)
def run():
    is_running=True
    # remember that in the assignment the place where the variable is located is given and not the value of the variable as such.
    check_running=lambda :is_running
    thr=Thread(target=work,kwargs={'check_running':check_running,'id':1})
    thr.start()
    # set daemon=True to kill/stop thread at end of application
    thr2=Thread(target=work,kwargs={'check_running':lambda:True,'id':2},daemon=True)
    thr2.start()


    sleep(10)
    is_running=False
    sleep(2)

if __name__=='__main__':
    run()
    