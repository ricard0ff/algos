import math
import itertools



def main():
  temp = 0
  for a in xrange(1000):
    for b in xrange(1000):
      result = a * b 
      if ((str(result) == str(result)[::-1]) and (result > temp)):
        temp = result
  print temp
        



if __name__ == "__main__":
    main()
