# Beispiel zu Gültigkeitsbereichen (scopes) und Namensräumen (namespaces)
# ich frag mich wozu das nütze ist und wer das kapiert?
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "Global spam"
    
    spam = "test spam"
    do_local()
    print("lokale Zuweisung:", spam)
    do_nonlocal()
    print("nonlokale Zuweisung:", spam)
    do_global()
    print("globale Zuweisung:", spam)

scope_test()
print("globaler Gültigkeitsbereich:", spam)

# Klassen
class MyClass:
    """A Hello World class"""
    def __init__(self): #ctor
        self.data = { "Apfel", "Orange", "Apfel", "Birne", "Orange", "Banane"}
    i = 12345
    def f(self):
        return "Hello World"
x= MyClass()
print(x.i)
print(x.f())
print(x.data)

# sowas ist völlig absurd!! hier erstellt man einfach ein Feld in der Klasse!!
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

#Vererbung
class MyNextClass(MyClass):
    def __init__(self):
        super().__init__()
    i = 5678
    def f(self):
        return MyClass.f(self)+"blabla"
y = MyNextClass()
print(y.i)
print(y.f())
print(y.data)

