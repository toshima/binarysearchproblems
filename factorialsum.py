

def solve(n):
    k = 1
    while n:
        if n % k <= 1:
            n //= k
        else:
            return False
        k += 1
    return True


if __name__ == '__main__':
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 32, 29]:
        print(n, solve(n))

