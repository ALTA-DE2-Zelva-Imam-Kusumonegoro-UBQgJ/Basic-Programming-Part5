import math

def prime_number(number):
    if number <= 1:
        return False
    
    log = int(math.log2(number))

    for x in range(2, log+1):
        if number % x == 0:
            return False
    return True



if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
