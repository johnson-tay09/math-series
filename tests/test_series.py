from math_series.series import fibonacci, lucas


# from math_series.series import sum_series


def test_import():
    assert fibonacci


def test_import1():
    assert lucas


def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fib_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fib_16():
    actual = fibonacci(16)
    expected = 987
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected
