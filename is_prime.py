def is_prime(num):
    '''
    Native method of checking for primes
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else:
        print(num, 'is prime')