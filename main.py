def collatz_length(n):
    collatz_list = list()

    while (n != 1):
        collatz_list.append(n)

        if (n % 2 == 0):
            n = n // 2
        else:

            n = (3 * n) + 1
    collatz_list.append(1)
    M = len(collatz_list)

    return (M - 1)
