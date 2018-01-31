import numpy as np
alist = [1, 7, 3, 1]

def get_product_all(alist):
    if len(alist)<2:
        raise IndexError("to multiply we require at least 2")
    alist.sort(reverse=True)
    print(np.prod(np.array(alist[:3])))

def main():
    get_product_all(alist)

if __name__ == "__main__":
    main()
