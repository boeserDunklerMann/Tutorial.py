# Fibonacci-Zahlen-Modul
def fib(n):
    """Print the fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b=b, a+b
    print()


def fib2(n):    # gibt die Fibonacci-Folge bis n zurück
    """Returns a list containing the fibonacci series up to n."""
    result = list()
    a, b = 0, 1
    while a<n:
        result.append(a)
        a, b=b, a+b
    return result

