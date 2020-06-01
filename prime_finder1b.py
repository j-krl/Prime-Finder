#Version 1 of prime number finder up to specified value "max_value"
#iterates through every value up to "max_value"
#Author: Jesse Kearl

import time

while True:
    max_value = input("Find all primes up to what value? ")
    start_time = time.time()
    if max_value == 'exit' or max_value == 'quit' or max_value == 'q':
        raise SystemExit
    try:
        max_value = int(max_value)
        index = 2
        divisions = 0
        cum_divisions = 0
        if max_value < 3:
            print("Input a number three or greater")
        else:
            primes = [2]
            i = 3.0; n = 2
            while (i <= max_value):
                divisions = 0
                while True:
                    if (i/n).is_integer() is False and (i-n) > 1:
                        n += 1
                        cum_divisions += 1
                        divisions += 1
                    elif (i/n).is_integer() is True and (i-n) > 1:
                        n = 2
                        i += 1
                        cum_divisions += 1
                        divisions += 1
                        break
                    else:
                        primes.append(int(i))
                        n = 2
                        i += 1
                        cum_divisions += 1
                        divisions += 1
                        break
            end_time = time.time()
            print('All primes up to',max_value,': ', primes)
            print('Number of primes:', len(primes))
            print('Elapsed computing time:', end_time - start_time)
            print('Cumulative division operations:',cum_divisions)
            print('Divisions for max value:',divisions)
    except ValueError:
        print("Input does not compute")
