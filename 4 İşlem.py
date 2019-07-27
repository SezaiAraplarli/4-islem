# Toplama İşlemi
def topla(a,b):
    top=(a+b)
    print(a,"+",b,"=",(a+b))

# Çıkarma İşlemi
def cikar(a,b):
    cik=(a-b)
    print(a,"-",b,"=",(a-b))

# Çarpma İşlemi
def carp(a,b):
    car=(a*b)
    print(a,"x",b,"=",(a*b))

# Bölme İşlemi
def bolme(a,b):
    bol=(a/b)
    print(a,"/",b,"=",(a/b))

print("Yapılacak İşlemi Seçin.")
print("-__-__-__-__-__-__-")
print("1)Toplama")
print("2)Çıkarma")
print("3)Çarpma")
print("4)Bölme")

# Hangi işlemin uygulanacağı kısım burası
while True:
    secim = (input("?"))
    x = int(input("İlk Sayıyı Giriniz"))
    y = int(input("İkinci Sayıyı Giriniz"))

    if secim=="1":
        topla(x,y)
    elif secim=="2":
        cikar(x,y)
    elif secim=="3":
        carp(x,y)
    elif secim=="4":
        bolme(x,y)
    else:
        print("Öyle bir işlem yok!")
        break

#Program gayet iyi çalışıyor ama
#1,2,3 veya 4 dışında bir sayı
#girilirse ilk ve ikinci sayıyı
#sorup ondan sonra geçersiz yazdırıyor.