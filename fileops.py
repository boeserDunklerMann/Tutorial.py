# Reading files
f = open('D:\\git\\Python\\Tutorial.py\\BTW2025-Leipzig-Wahlbezirk.csv', 'r')
#f.read()
#print(f.readlines())

# alternativ kann man auch über das Dateiobjekt iterieren, was effizienter und schneller ist:
for line in f:
    print(line, end='')

f.close()

#writing files
# tmp = open('D:\\git\\temp\\test.txt', 'w')
with open('D:\\git\\temp\\test.txt', 'w') as tmp:   # so ähnlich, wie using in C#
    anzahloutput = tmp.write('Dies ist ein Test\n')
print("Zeichen geschrieben", anzahloutput)
value = ('Die Antwort', 42)
s = str(value)  # um was anderes als ein string zu schreiben, muss dies erst in einen string konvertiert werden
#tmp.write(s)
tmp.closed

# das Standardmodul pickle erlaubt es (fast) jedes pythonobjekt zu serialisieren
import pickle
f = open("D:\\git\\temp\\pickle.txt", "w")
basket = { "Apfel", "Orange", "Apfel", "Birne", "Orange", "Banane"}
pickle.dump(basket, f) # das geht aber so nicht
f.close()
