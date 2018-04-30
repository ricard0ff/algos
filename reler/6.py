import math
import itertools


def squared(number):
  return number ** 2

def main():
  sum_of_squares = 0
  squared_total_sum = 0
  for i in xrange(1,101):
    sum_of_squares += squared(i)
    squared_total_sum += i
  result = squared(squared_total_sum) - sum_of_squares
  print result

        



if __name__ == "__main__":
  main()
