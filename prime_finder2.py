#Version 2 of prime number finder up to specified value "max_value"
#iterates through only primes up to "max_value", yet is still less efficient than version 1?
#Author: Jesse Kearl

import time

while True:
    max_value = input("Find all primes up to what value? ")
    start = time.time()
    if max_value == 'exit' or max_value == 'quit' or max_value == 'q':
        raise SystemExit
    try:
        max_value = int(max_value)
        if max_value < 3:
            print("Input a number three or greater")
        else:
            primes = [2]
            i = 3.0
            while i <= max_value:
                for n in primes:
                    if (i/n).is_integer() is False and \
                    primes.index(n)+1 != len(primes):
                        continue
                    elif (i/n).is_integer() is False and \
                    primes.index(n)+1 == len(primes):
                        primes.append(int(i))
                        break
                    else:
                        break
                i += 1
            end = time.time()
            print('All primes up to',max_value,': ', primes)
            print('Number of primes:', len(primes))
            print('Elapsed computing time:', end - start)
    except ValueError:
        print("Input does not compute")
