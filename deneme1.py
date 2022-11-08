print("işlemler:")
print("1 toplama")
print("2 çıkarma")
print("3 çarpma")
print("4 bölme")

islem = str(input("işlem gir lan: "))

if islem == "1":
    sayi1 = int(input("sayı1 gir : "))
    sayi2 = int(input("sayı2 gir : "))
    print("toplam:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("Sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 / sayi2)
else :
    print("yanlış sayı girdin robotmusun lan sen")
