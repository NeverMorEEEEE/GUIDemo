import time
import threading
def hold1(limit):
    i=0
    while i<limit:
        i += 1
        print(t1.name,"is runing " + str(i))
        time.sleep(1)
    print(t1.name,"is over")
def hold2(limit):
    i=0
    while i<limit:
        i+=1
        print(t2.name,"is runing " + str(i))
        time.sleep(1)
    print(t2.name,"is over")

start_time=time.time()
t1=threading.Thread(target=hold1,args=(3,))
t2=threading.Thread(target=hold2,args=(6,))

t1.start()
t2.start()

print(threading.current_thread().name,"耗时",time.time()-start_time)