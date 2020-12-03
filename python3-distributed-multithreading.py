
# python3 python3-distributed-multithreading.py
# time python3 python3-distributed-multithreading.py
# /usr/bin/time python3 python3-distributed-multithreading.py

# this program illustrates threading library in python and its
# difference when using it for intensive task and non-intensive tasks

import threading
import time
import timeit
import urllib.request

def fibonacci(n):
   # n:      0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11
   # fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
   if n < 2 :
      return n
   else:
      val = 1
      prev = 0
      for i in range(2,n+1):
         val , prev = val + prev , val
      return val

def print_fibonacci(n):
   print(n,fibonacci(n))
   

def compute_all_intensive(n,m):
   ntimes = 10
   time_sequential = timeit.timeit('compute_sequential_intensive(n,m)',number=ntimes,globals=globals())
   time_threaded = timeit.timeit('compute_threaded_intensive(n,m)',number=ntimes,globals=globals())
   print('intensive sequential time',time_sequential)
   print('intensive threaded time  ',time_threaded)

def compute_sequential_intensive(n,m):
   #print_fibonacci(n)
   #print_fibonacci(m)
   fibonacci(n)
   fibonacci(m)

def compute_threaded_intensive(n,m):
   if __name__ == "__main__": 
      # creating threads
      #t1 = threading.Thread(target=print_fibonacci, args=(n,))
      #t2 = threading.Thread(target=print_fibonacci, args=(m,))
      t1 = threading.Thread(target=fibonacci, args=(n,))
      t2 = threading.Thread(target=fibonacci, args=(m,))
      
      # starting threads
      t1.start()
      t2.start()
      
      # wait until threads are completely executed
      t1.join()
      t2.join()

def compute_all_nonintensive(pair1,pair2,pair3):
   ntimes = 10
   time_threaded = timeit.timeit('compute_threaded_nonintensive(pair1,pair2,pair3)',number=ntimes,globals=globals())
   time_sequential = timeit.timeit('compute_sequential_nonintensive(pair1,pair2,pair3)',number=ntimes,globals=globals())
   print('nonintensive sequential time',time_sequential)
   print('nonintensive threaded time  ',time_threaded)

def compute_sequential_nonintensive(pair1,pair2,pair3):
   nonintensivetask(pair1)
   nonintensivetask(pair2)
   nonintensivetask(pair3)

def compute_threaded_nonintensive(pair1,pair2,pair3):
   if __name__ == "__main__": 
      # creating threads
      t1 = threading.Thread(target=nonintensivetask, args=(pair1,))
      t2 = threading.Thread(target=nonintensivetask, args=(pair2,))
      t3 = threading.Thread(target=nonintensivetask, args=(pair3,))
      
      # it is not necessary to be defined as daemon
      #t1 = threading.Thread(target=nonintensivetask, args=(pair1,),daemon=True)
      #t2 = threading.Thread(target=nonintensivetask, args=(pair2,),daemon=True)
      
      # starting threads
      t1.start()
      t2.start()
      t3.start()
      
      # wait until threads are completely executed
      t1.join()
      t2.join()
      t3.join()

def nonintensivetask(pair):
   #time.sleep(1)
   baseurl = 'https://query1.finance.yahoo.com/v7/finance/download/{}=X'
   res = urllib.request.urlopen(baseurl.format(pair))
   #bodyb = res.read()
   #body = bodyb.decode('utf-8')
   #print('body: ',body)


# compute intensive tasks
# we choose big numbers hide overhead of creating threads
n = 10000
m = 20000
compute_all_intensive(n,m)

# compute non-intensive tasks
pair1 = 'EURUSD'
pair2 = 'GBPUSD'
pair3 = 'COPUSD'

#nonintensivetask('EURUSD')
compute_all_nonintensive(pair1,pair2,pair3)
