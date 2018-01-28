import numpy as np
alist = [1, 7, 3, 1]

def get_product_all(alist):
    if len(alist)<2:
        raise IndexError("to multiply we require at least 2")
    final_list = []
    for list_values in alist:
        list_index = alist.index(list_values)
        alist.pop(list_index)
        final_list.insert(list_index,np.prod(np.array(alist)))
        alist.insert(list_index,list_values)
    print (final_list)

def main():
    get_product_all(alist)

if __name__ == "__main__":
    main()