alist= [10, 7, 5, 8, 11, 9]

def get_profit(alist):
    if len(alist) < 2:
        raise IndexError("we need at least 2 to compare")
    min_value = min(alist)
    #since its a "time series" we only care about the first ocurrence
    min_value_index = alist.index(min_value)
    profit = 0

    for values in alist[min_value_index:]:
        temp_profit = values - min_value
        if profit < temp_profit:
            profit = temp_profit
        else:
            print ("not good enough profit")

    print ("The biggest profit you can make is %s" % (profit))
    return 0


def main():
    get_profit(alist)

if __name__ == "__main__":
    main()