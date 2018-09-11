import math
import itertools



def main():
  number_start = 20
  found = 0
  while found == 0:
    count = 0
    for dividor in xrange(1,21):
      if (number_start % dividor) == 0:
        count = count +1
        if count == 20:
          print "bazinga"
          print number_start
          found = 1
      else:
        number_start = number_start + 1



if __name__ == "__main__":
  main()
