from mpmath import *
from math import log


def dividebcd(numerator, denominator):
    if denominator == 0:
        raise ValueError("divide by 0")
    elif denominator == 0:
        return numerator
    else:
        count = 0
        while numerator >= denominator:
            numerator = numerator - denominator
            count = count + 1
        return count


def newdiv(numerator, denominator):
    sizeremainder = numerator - denominator
    r = (1 << (2*1)) // (numerator >> (denominator - 1))
    last_prec = 1
    for precision in range(1, sizeremainder):
        a = lshift(r, precision - last_prec + 1)
        b = rshift(r**2 * rshift(denominator,
                                 numerator - precision), 2 * last_prec)
        r = a - b
        last_prec = precision
    return ((numerator >> denominator) * r) >> sizeremainder


def main():
    print(dividebcd(10, 2))
    print(dividebcd(100, 8))
    print(dividebcd(2, 1))
    print(dividebcd(1, 1))
#    print(dividebcd(2, 0))
    print "NEWDIV"
    print(newdiv(10, 2))
    print(newdiv(100, 8))
    print(newdiv(2, 1))
    print(newdiv(1, 2))


if __name__ == "__main__":
    main()
