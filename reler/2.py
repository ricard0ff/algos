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
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a + b


def main():
#    print(fibo((1, 2), 4000000))
#    print(sum(i for i in even_fibo(10) if i % 2 == 0))
     result_even_sum = 0
     for i in fibo_generator(4000000):
         if i % 2 == 0:
             result_even_sum += i
     print "TOTAL"
     print result_even_sum


if __name__ == "__main__":
    main()
