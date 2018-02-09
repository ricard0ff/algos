def fibo(number_up_to):
    #create two entries to start the sequence
    fibonacci_list = [0, 1]
    for i in range(2, number_up_to):
        fibonacci_list.insert(i, (fibonacci_list[i-1] + 
                                  fibonacci_list[i-2]))
    print "the result is :"+(fibonacci_list)
    return fibonacci_list


def compute_even_numbers(fibonacci_list):
    sum_fibonacci = 0
    for i in fibonacci_list:
        if i % 2 == 0:
            sum_fibonacci += i
    return sum_fibonacci



def main():
    print(compute_even_numbers(fibo(4000000)))


if __name__ == "__main__":
    main()
