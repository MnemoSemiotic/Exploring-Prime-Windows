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


    sorted_counts, sorted_distances = zip(*sorted(zip(counts, distances), reverse=True))


    plt.scatter(distances, counts, marker="_")
    plt.plot(distances, counts)


    if overlay == False:
        for dist, count in zip(distances, counts):
            label = '{}'.format(dist)

            plt.annotate(label, (dist, count), textcoords="offset points", xytext=(0,0), ha='center', color='black', bbox=dict(boxstyle='circle, pad=0.05', fc='yellow', alpha=0.3))


    col_labels = ['distance', 'count']
    table_vals = []
    for i in range(15):
        table_vals.append([sorted_distances[i], sorted_counts[i]])

    plt.table(cellText=table_vals, colWidths = [.1]*3, colLabels=col_labels, loc='center right')


    plt.suptitle(f'Prime Window between {window_low} and {window_high}')
    plt.title(f'Total Primes: {primes_count}, Max Distance: {max(distances)}')
    plt.xlabel('Distance')
    plt.ylabel('Occurrence of Distance in Window')

    plt.ylim(ymax=200, ymin=0)
    plt.xlim(xmax=115, xmin=0)


    # plt.show()

    plt.savefig(f'images/prime_window_{str(window_low).zfill(10)}_{str(window_high).zfill(10)}')

    if overlay == False:
        plt.clf()

    
    







if __name__ == '__main__':

    window_size = 10000
    windows_start = 0
    windows_stop = 100000
    overlay = True
    zeros = False

    for i in range(windows_start, windows_stop, window_size):

        window_low = i
        window_high = i + window_size

        primes_window = get_primes_in_window(window_low, window_high)

        num_primes = len(primes_window)

        primes_window_distances = get_distances(primes_window)

        max_prime_dist = max(primes_window_distances)

        distances_distribution = build_primes_dist_distr(primes_window_distances, include_zeros=zeros)


        plot_primes_window(distances_distribution, window_low, window_high, num_primes, overlay=overlay)
