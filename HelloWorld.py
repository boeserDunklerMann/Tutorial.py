# https://py-tutorial-de.readthedocs.io/de/python-3.3/introduction.html
the_earth_is_flat = True
if the_earth_is_flat:
    print("Dont fall off!")
# Fibonacci-Folge
a, b = 0, 1
while b < 1000:
    print(b, end=" ")
    a, b=b, a+b
print("\n")

# im C# ist das folgende eine foreach
a = ["André", "Chrysoula"]
for word in a:
    print(word, len(word))

# Funktion range() erzeugt arithmetische Folgen (wofür auch immer)
for i in range(0, 10, 2):
    print(i)

# auch Schleifen können ein else-Zweig haben, der wird durchlaufen, wenn die Schleife NICHT durch ein break vorzeitig beendet wurde
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print (n, "equals", x, "*", n//x)
            break
    else:
        print (n, "is a prime number")

# continue gibt's auch im C#
for num in range(2, 10):
    if num % 2 == 0:
        print("Found even number", num)
        continue
    print ("Found odd number", num)

# pass macht nichts
#while True:
#   pass    # Warten auf Strg+C

# Funktionen definieren

def fib(n):
    """Print the fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b=b, a+b
    print()

# Funktion aufrufen:
fib(2000)
