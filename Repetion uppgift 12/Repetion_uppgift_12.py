print("Omvandla fran celsius till fahrenheit: tryck 1")
print("Omvandla fran fahrenheit till celsius: tryck 2")
omvandla=int(input("Tryck 1 eller 2: "))

if omvandla==1:
    C=int(input("Celsius: "))
    F=9*C/5 + 32
    print(C,"celsius ar ",F,"fahrenheit")
elif omvandla==2:
    F=int(input("Fahrenheit: "))
    C=5/9 * (F-32)
    print(F,"fahrenheit ar ",C,"celsius")