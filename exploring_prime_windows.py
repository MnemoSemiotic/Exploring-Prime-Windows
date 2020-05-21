
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for n in range(3, int(num**(1/2)+1), 2):
        if num % n == 0:
            return False

    return True


def find_next_prime(n):
    count = n+1
    continue_looking = True

    while continue_looking:
        if is_prime(count):
            continue_looking = False
            break
        count += 1
    
    return count


def get_primes_in_window(low_val, high_val):
    primes = []

    for num in range(low_val, high_val):
        if is_prime(num):
            primes.append(num)

    return primes

for num in get_primes_in_window(low_val=0, high_val=10000):
    print(num)