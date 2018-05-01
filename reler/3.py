import math
import itertools

def prime_generator(primatize_number):
 #   if primatize_number 
  return 0

def sieve_generator(number_up_to):
  #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  #https://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
  if number_up_to <= 2: return
  yield 2
  F = [True] * number_up_to
  seq1 = xrange(3, int(math.sqrt(number_up_to)) + 1, 2)
  seq2 = xrange(seq1[-1] + 2, number_up_to, 2)
  for p in itertools.ifilter(F.__getitem__, seq1):
    yield p
    for q in xrange(p * p, number_up_to, 2 * p):
      F[q] = False
  for p in itertools.ifilter(F.__getitem__, seq2):
    yield p 


def main():
  for i in sieve_generator(14):
    print i


if __name__ == "__main__":
  main()
