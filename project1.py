

# BÜTÇE TAKİBİ

print("Aylık mutfak harcamanız: ", (mutfak :=  int(input("Lutfen aylık mutfak harcamanızı giriniz:"))))
print("Aylık yemek harcamanız:" , (yemek :=  int(input("Lutfen aylık yemek harcamanızı giriniz:"))))
print("Aylık yol harcamanız:" , (yol :=  int(input("Lutfen aylık yol harcamnızı giriniz:"))))
print("Aylık kiranız:" , (kira :=  int(input("Lutfen aylık kiranızı giriniz:"))))
print("Aylık geliriniz:" , (gelir := int(input("Lutfen aylık gelirinizi giriniz:"))))

toplam_gider = mutfak + yemek + yol + kira

x = (gelir*20)/100

if toplam_gider > x :
    print("Gideriniz gelirinizin %20'sinden fazladır tasarruf yapmalısınız")
else:
    print("gideriniz gelirinizin %20'sinden azdır tasarruf yapmanıza gerek yok")

#Aylık zorunlu ihtiyaçlar harici giderler hasaplanmıştır

print(kıyafet := int(input("Lutfen almak istediğiniz kıyafetin fiyatını giriniz:")))
print(ayakkabı := int(input("Lutfen almak istediğiniz ayakkabının fiyatını giriniz:")))
print(tatil := int(input("Lutfen planlanan aylık tatil bütçenizi giriniz:")))

y = (gelir*10)/100
z = kıyafet + ayakkabı + tatil

if z<y:
    print("zorunlu ihtiyaçlar hariç aylık gidrleriniz geliriniziz %10'undan azdır. Bu harcamaları yapabilirsiniz")
else:
    print("Zorunlu ihtiyaçlar harici aylık giderleriniz gelirinizin %10'undan fazladır. Bu harcamaları yapmamalısınız")