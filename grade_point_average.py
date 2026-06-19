# Not ortalamasını hesaplayan program yazınız

not1 = input("Lutfen 1. notu giriniz:")
not2 = input("Lutfen 2. notu giriniz:")
not3 = input("Lutfen 3. notu giriniz:")

ortalama = ( int(not1) + int(not2) + int(not3) ) /3
yeni_ortalama = round(ortalama,2)

print(yeni_ortalama)