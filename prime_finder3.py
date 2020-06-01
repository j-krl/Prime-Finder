#Version 3 of prime number finder up to specified value "max_value"
#iterates through every value up to square root of "max_value"
#Author: Jesse Kearl

#The difference between versions 1 and 3 is that if the variable n gets within
#1 of the square root of the max_value, i is automatically appended to the
#primes list. This is because if a number has no factors before its square root
#it must be prime.

import time
import math

while True:
    max_value = input("Find all primes up to what value? ")
    start_time = time.time()
    if max_value == 'exit' or max_value == 'quit':
        raise SystemExit
    else:
        try:
            max_value = int(max_value)
            if max_value < 3:
                print("Input a number three or greater")
            else:
                primes = [2]
                i = 3.0; n = 2
                while (n < i) and (i < max_value):
                    if (i/n).is_integer() is False and (i-n) > 1 and \
                    (math.sqrt(float(max_value))-n) > 1:
                    #Only code varied between versions 1 and 3.
                        n += 1
                    elif (i/n).is_integer() is True:
                        n = 2
                        i += 1
                    else:
                        primes.append(int(i))
                        n = 2
                        i += 1
                end_time = time.time()
                print('All primes up to',max_value,': ', primes)
                print('Number of primes:', len(primes))
                print('Elapsed computing time:', end_time - start_time)
        except ValueError:
            print("Input does not compute")
