while True:
    try:
        x = int(input("Gib ne int-Zahl ein: "))
        break   #bricht die while ab
    except ValueError:
        print("keine gültige Zahl noch ein Versuch.")
    finally: pass
