def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n


if __name__ == "__main__":
    get_divisors(10)