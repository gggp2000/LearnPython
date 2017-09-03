from multiprocessing import Process, Queue
import os, time, random

# code for writing process data
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...'% value)
        q.put(value)
        time.sleep(random.random())

#code for reading process data
def read(q):
    print('Process to read %s'% os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.'% value)

if __name__ == '__main__':
    # create Queue in Father Process, then send to each Child Process
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #start Child pw, Write
    pw.start()
    #start Child pr, Read
    pr.start()
    #waiting for end of pw
    pw.join()
    #end process manually
    pr.terminate()
