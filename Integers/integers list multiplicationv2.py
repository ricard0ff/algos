import numpy as np
import time
import random

alist = [1, 7, 3, 1]

def get_product_all(alist):
    if len(alist) < 2:
        raise IndexError("to multiply we require at least 2")
    start = time.time()
    alist.sort(reverse=True)
    value = np.prod(np.array(alist[:3]))
    stop = time.time()
    timevalue=stop-start
    print("Sum is %d required %10.7f seconds "% (value, timevalue))

def main():
    i=10
    while i<1000000000:
        randomlist = random.sample(xrange(1000000000),i)
        get_product_all(randomlist)
        print "size"
        print len(randomlist)
        i*=10






if __name__ == "__main__":
    main()
