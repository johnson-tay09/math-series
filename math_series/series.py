def fibonacci(n):
    #  error catching
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(i):
    #  error catching
    if i < 0:
        print("Incorrect input")
    elif i == 0:
        return 2
    # Second lucas number is 2
    elif i == 1:
        return 1
    # Second lucas number is 1
    elif i == 2:
        return 3
    elif i == 3:
        return 4
    else:
        return lucas(i - 1) + lucas(i - 2)


def sum_series(num, first=0, second=1):
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 2
    elif num == 1:
        return 1
    elif num == 2:
        return 3
    elif num == 3:
        return 4
    else:
        return sum_series(num - 1, first, second) + sum_series(num - 2, first, second)
