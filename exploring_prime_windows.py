import matplotlib.pyplot as plt


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
    return [num for num in range(low_val, high_val) if is_prime(num) == True]


def get_distances(primes_list):
    rev = primes_list[::-1]
    offset = rev[1:]

    return [num - offset[idx] for idx, num in enumerate(rev[:len(rev)-1])][::-1]


def build_primes_dist_distr(primes_dist_window, include_zeros=True):
    d = dict()

    if include_zeros == True:
        for i in range(max(primes_dist_window)+1):
            d[i] = primes_dist_window.count(i)

    else:
        for dist in primes_dist_window:
            if dist not in d:
                d[dist] = primes_dist_window.count(dist)

    return d


def plot_primes_window(distances_distribution, window_low, window_high, primes_count, overlay=False):
    print(f'plotting window {window_low} to {window_high}')

    distances, counts = [], []

    for dist, count in sorted(distances_distribution.items()):
        distances.append(dist)
        counts.append(count)

    plt.scatter(distances, counts, marker="_")
    plt.plot(distances, counts)


    plt.suptitle(f'Prime Window between {window_low} and {window_high}')
    plt.title(f'Total Primes: {primes_count}, Max Distance: {max(distances)}')
    plt.xlabel('Distance')
    plt.ylabel('Occurrence of Distance in Window')

    plt.show()







if __name__ == '__main__':
    # print(get_distances(get_primes_in_window(low_val=0, high_val=10000)))

    window_low = 10000
    # window_high = 10000
    window_size = 10000

    primes_list = get_primes_in_window(low_val=0, high_val=10000)
    num_primes = len(primes_list)

    d =  build_primes_dist_distr(get_distances(primes_list), include_zeros=True)
    
    
    plot_primes_window(d, window_low, window_low + window_size, len(primes_list), overlay=False)
