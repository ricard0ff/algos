import time

def sum_n(values):
    value_sum = 0
    for i in range(1,values+1):
        value_sum = value_sum + i
    return value_sum

def sum_n2(values):
    start = time.time()
    tsum = 0
    for i in range(1, values+1):
        tsum = tsum + i
    end = time.time()
    return tsum,end-start

def sum_n3(values):
    start = time.time()
    final = (values*(values+1))/2
    end = time.time()
    return final,end-start

alist = [10,5,6,1,8,20]
def compare_values(alist):
    min = alist[1]
    for values in alist:
        if values < min:
            min = values
    print (min)


print(compare_values(alist))
print (sum_n(10))
for i in range(5):
    print("Sum of n2 %d required %10.7f seconds "%sum_n2(1000000))
    
for i in range(5):
    print("Sum of n3 %d required %10.7f seconds "%sum_n3(1000000))