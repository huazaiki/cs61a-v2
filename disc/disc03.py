def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        all_but_last, last = n // 10, n % 10
        print(last)
        swipe(all_but_last)
        print(last)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)


def is_prime_iter(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def f(i):
        """
        i: 用来判断是否有其他因数的辅助参数
        """
        if n % i == 0:
            return n == i
        elif i + 1 == n:
            return True
        else:
            return f(i + 1)
    return f(2)


def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return hailstone(n // 2) + 1

def odd(n):
    if n == 1:
        return 1
    else:
        return hailstone(n * 3 + 1) + 1


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        """
        direction:
            0: 逆时针
            1: 顺时针
        """
        if i == n:
            return who
        elif has_seven(i) or i % 7 == 0:
            if direction == 1:
                who = who - 1
                if who == 0:
                    who = k
                return f(i + 1, who, 0)
            else:
                who = who + 1
                if who == k + 1:
                    who = 1
                return f(i + 1, who, 1)
        else:
            if direction == 1:
                who = who + 1
                if who == k + 1:
                    who = 1
                return f(i + 1, who, 1)
            else:
                who = who - 1
                if who == 0:
                    who = k
                return f(i + 1, who, 0)

    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)