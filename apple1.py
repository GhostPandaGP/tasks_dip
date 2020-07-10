def is_shifted(a, b):

    if len(a) != len(b):
        return False

    for i in range(len(a)):

        if (a[i:] + a[:i]) == b:
            return True

    return False


if __name__ == '__main__':
    print(is_shifted('abcde', 'cdeab'))
    # True
