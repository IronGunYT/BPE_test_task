def find_backet(n: int, w: int, d: int, p: int) -> int:
    if d == 0:
        raise Exception('Bad input')
    # count weight without fake coin
    true_weight = w * (n*(n-1) // 2)
    delta_weight = true_weight - p
    if delta_weight == 0:
        return n
    else:
        return delta_weight // d


if __name__ == '__main__':
    n = int(input('Enter n: '))
    w = int(input('Enter w: '))
    d = int(input('Enter d: '))
    p = int(input('Enter p: '))
    print('Number: ', find_backet(n, w, d, p))
