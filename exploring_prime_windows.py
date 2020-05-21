
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for n in range(3, int(num**(1/2)+1), 2):
        if num % n == 0:
            return False

    return True

for num in range(100):
    if is_prime(num):
        print(num)