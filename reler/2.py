def fibo(index_to_start, number_up_to):
    #create two entries to start the sequence
    fibonacci_list = [index_to_start[0], index_to_start[1]]
    result = 0
    for index in range(2, number_up_to):
        number = fibonacci_list[index-1] + fibonacci_list[index-2]
        fibonacci_list.append(number)
        fibonacci_list[3:]
        if number % 2 == 0:
            result += number
    return result


def fibo_generator(limit):
    #make sure there are >=2 numbers in the initial index
    index0, index1 = 1, 2
    while index0 < limit:
        yield index0
        index0, index1 = index1, index0 + index1


def main():
     result_even_sum = 0
     for i in fibo_generator(4000000):
         if i % 2 == 0:
             result_even_sum += i
     print "TOTAL"
     print result_even_sum


if __name__ == "__main__":
    main()
