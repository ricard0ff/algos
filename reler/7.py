import math
import itertools
from itertools import count, ifilter


def sieve():
    seq = count(2)
    while True:
        p = seq.next()
        seq = ifilter(p.__rmod__, seq)
        yield p


def main():
  count = 0
  for i in sieve():
    if count == 10001:
      break
    a=i
    count += 1
  print a



if __name__ == "__main__":
  main()
