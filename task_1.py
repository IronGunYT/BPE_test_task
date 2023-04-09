def swap_bytes(n: int) -> int:
    # n to binary
    s = bin(n)[2:]
    if len(s) > 8:
        raise Exception('Bad input')
    s = '0'*(8-len(s)) + s  # if n has less than 8 bits
    s = s[4:]+s[:4]  # swap bytes
    return int(s, 2)


if __name__ == '__main__':
    n = int(input('Enter positive 2-byte integer: '))
    print('Result:', swap_bytes(n))
