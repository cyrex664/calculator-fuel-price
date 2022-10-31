print("Witaj! Wersja aplikacji 1.0.0")
print()

while True:
    try:
        trip = float(input("Podaj długość trasy w kilometrach: "))
        fuel_gets = float(input("Podaj średnie spalanie na 100 km: "))
        fuel_price = float(input("Podaj cenę litra paliwa: "))       
    except ValueError:
        print("BŁĄD!")
        print("Podaj poprawne wartości! Upewnij się, że jeśli wpisywałeś liczbę dziesiętną to użyłeś kropki, a nie przecinka")
        continue
    else:
        fuel_gets_one_km = fuel_gets/100
        s = fuel_gets_one_km * trip
        trip_price = fuel_price * s
        print("Koszt podróży wynosi",round(trip_price,2),"zł")
        break