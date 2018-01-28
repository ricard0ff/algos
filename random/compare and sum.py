alist1 = [1,4,5,6]
alist2 = [1,10,3,4,5,6]


def get_sum(alist,number_sum):
    item = set()
    alist.sort()
    for index, valueouter in enumerate(alist):
        try:
            item.add(valueouter)
            if (number_sum - valueouter) in item:
                #then we have an item that will get us to the sum
                print ("we have found the number")
                print ("the number is %d that can be used with %d" %(valueouter,(number_sum - valueouter)))
        except IndexError:
            print ("oops out of the range")


        

def main():
    get_sum(alist2, 6)

if __name__ == "__main__":
    main()