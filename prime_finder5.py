#Version 5 of prime number finder iterating up to square root of "i", and\
#iterating through only primes up to that point.

#Author: Jesse Kearl

import time
import math

while True:
    max_value = input("Find all primes up to what value? ")
    start_time = time.time()
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
                #i will now only divide by primes less than its square root
                    if (i/n).is_integer() is False and\
                    (math.sqrt(float(i))-n) >= 1:
                        continue
                    elif (i/n).is_integer() is True:
                        break
                    else:
                        primes.append(int(i))
                        break
                i += 1
            end_time = time.time()
            print('All primes up to',max_value,': ', primes)
            print('Number of primes:', len(primes))
            print('Elapsed computing time:', end_time - start_time)
    except ValueError:
        print("Input does not compute")
