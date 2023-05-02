def generate_prime(n: int):
    if n <= 1:
        raise ValueError

    for number in range(2, n + 1):
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number


# primes = generate_prime(100)
# for prime_number in range(10):
#     print(next(primes))


def lines_with_word(filename: str, word: str):
    with open(filename, "r") as file:
        for line in file:
            if word in line:
                yield line


lines = lines_with_word("mbox-short.txt", "From")
for line in lines:
    print(next(lines))


def all_possible_combos(string_list):
    count = len(string_list)
    for string in string_list:
        yield string

    """
    Generates all possible combinations of strings in the given list.
    """
    n = len(strings)
    for i in range(1, 2**n):
        subset = [strings[j] for j in range(n) if (i & (1 << j))]
        yield "".join(subset)
