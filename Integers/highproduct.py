import numpy as np

alist = [10,10,1,3,2]

def get_high_product(alist):
    if len(alist)<3:
        raise IndexError("need at least three")
    alist.sort(reverse=True)
    if all(numbers > 0 for numbers in alist):
        print ("we have all positives ints")
        top_3_values = alist[:3]
        highest_values = np.prod(np.array(top_3_values))
        print (highest_values)
    else:
        print ("we have at least a negative")
        #at this point we should count to see if we can leverage two negative numbers to produce a positive:
        #todo we still need to take into consideration just one negative number in the list
        negative_count = 0
        for numbers in alist:
            if numbers <0:
                negative_count += 1
        if negative_count >= 2:
            alist_abs = [abs(number) for number in alist]
            alist_abs.sort(reverse=True)
            top_3_abs_values = alist_abs[:3]
            highest_values = np.prod(np.array(top_3_abs_values))
            print (highest_values)


def main():
    get_high_product(alist)

if __name__ == "__main__":
    main()