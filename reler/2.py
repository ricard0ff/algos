def fibo(index_to_start,number_up_to):
    #create two entries to start the sequence
    fibonacci_list = [1, 2]
    result = 0

    for index in range(2, number_up_to):
        if index == 1000000:
            print "bazinga"
        number = fibonacci_list[index-1] + fibonacci_list[index-2]
        fibonacci_list.append(number)
        if number % 2 == 0:
            result += number
    print "the result is :"+str(result)
    print fibonacci_list

    return result


def main():
    print(fibo((0,1),10))



if __name__ == "__main__":
    main()
