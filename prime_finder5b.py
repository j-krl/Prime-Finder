#Version 5 of prime number finder iterating up to square root of "i", and iterating through only\
#primes up to that point.

#'a' versions of prime_finder include tickers for data analysis as well as plot creation.
#Plot

#Author: Jesse Kearl

import time
import math
def primeFinder():
    while True:
        max_value = input("Find all primes up to what value? ")
        index = 2
        divisions = 0
        cum_divisions = 0
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
                    divisions = 0
                    for n in primes:
                    #i will now only divide by primes less than its square root
                        divisions += 1
                        cum_divisions += 1
                        if (i/n).is_integer() is False and (math.sqrt(float(i))-n) >= 1:
                            continue
                        elif (i/n).is_integer() is True:
                            break
                        else:
                            primes.append(int(i))
                            break
                    index += 1
                    i += 1
                end_time = time.time()
                expected_primes = (float(max_value)/math.log(float(max_value))) #Based on Prime Number Theorem
                print('All primes up to', max_value,': ', primes)
                print('Number of primes:', len(primes))
                print('Approximate expected number of primes based on Prime Number Theorem (x/ln(x)):',\
                int((max_value)//(math.log(float(max_value)))))
                print('Ratio of measured number to theoretical approximation:',\
                (float(len(primes)))/(float(max_value)/math.log(float(max_value))))
                print('Elapsed computing time:', end_time - start_time)
                print('Cumulative division operations:', cum_divisions)
                print('Divisions for max value:', divisions)
        except ValueError:
            print("Input does not compute")

primeFinder()
