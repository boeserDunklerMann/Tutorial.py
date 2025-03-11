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
# Die erste Anweisung des Funktionskörpers kann auch ein Zeichenkettenliteral sein, ein so genannter Dokumentationsstring der Funktion, auch Docstring genannt.
# mehr zu Docstrings: https://py-tutorial-de.readthedocs.io/de/python-3.3/controlflow.html#tut-docstrings
def fib(n):
    """Print the fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b=b, a+b
    print()

# Funktion aufrufen:
fib(2000)

def fib2(n):    # gibt die Fibonacci-Folge bis n zurück
    """Returns a list containing the fibonacci series up to n."""
    result = list()
    a, b = 0, 1
    while a<n:
        result.append(a)
        a, b=b, a+b
    return result

f100 = fib2(100)
print(f100)

# Funktionssparameter erzeugt Dictionary
def cheese_shop(kind, *arguments, **keywords):
    print("-- Haben Sie", kind, "?")
    print("-- Sorry, ", kind, "ist gerade aus.")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())  # Reihenfolge wäre ssonst undefiniert
    for kw in keys:
        print (kw, ":", keywords[kw])

cheese_shop("Limburger", "Der ist sehr flüssig, mein Herr",
            "Der ist wirklich SEHR flüssig",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")

#Benutzung von Listen als Queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])  # die drei sind schon da
queue.append("André")       # André kommt hinzu
queue.append("Chrysoula")   # Chrissy auch
queue.popleft() # der Erste geht
queue.popleft() # noch einer geht
print (queue)

# Tupel bestehen aus mehreren Komma-getrennten Werten
t = 1234, 54321, "qwertz"
print(t[0])
print(t)
# sie können verschachtelt werden:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tupel sind immutable
# t[0]=8888 # macht Bumm!
a, b, c = t # tupel auspacken
print(c)

# Mengen (sets) ist eine ungeordnete Sammlung ohne doppelte Elemente
basket = { "Apfel", "Orange", "Apfel", "Birne", "Orange", "Banane"}
print(basket)   # Duplikate sind weg
print('Orange' in basket)   # Schnelles testen auf Contains
print("Zwiebel" in basket)
a = set("abacadabra")
b = set("alacazam")
print(a)        # {'d', 'a', 'b', 'c', 'r'}
print(a - b)    # {'d', 'r', 'b'}
print(a | b)    # in a oder b
print(a & b)    # sowohl in a, als auch in b
print(a ^ b)    # entweder in a oder b

# Dictionaries (Key-Value-Pairs)
tel = {'jack': 1234, 'ich': 800123400}
tel['guido'] = 4711
print(tel)
del tel['ich']
tel['bro']=4711
print(tel)
list(tel.keys())
sorted(tel.keys())
'guido' in tel
'ich' in tel
for k, v in tel.items():
    print(k, v)
for index, value in enumerate(['tic', 'tac', 'toe']):
    print(index, value)
basket2 = { "Apfel", "Orange", "Apfel", "Birne", "Orange", "Banane"}
for fruit in sorted(basket2):
    print(fruit)
