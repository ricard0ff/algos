def multiple(number_up_to):
    result = 0
    for i in range(1, number_up_to):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print ("the result is :" + str(result))
    return result



def main():
    multiple(1000)


if __name__ == "__main__":
    main()
