#Kullanıcıdan veri alarak iç içe fonksiyon kullanmadan ekrana yazdıran program yazın
spor_dali = input ("Lutfen yaptığınınz spor dalını giriniz:")
yas = input ("Spora başladığınız yaşı giriniz:")
yil = input ("Kaç yıl spor yaptığınızı yazıyla giriniz:")

print (spor_dali)
print (yas)
print (yil)
#print fonksiyonunda metin (string) ifadesinin hemen ardından virgül koymadan 
#başka bir fonksiyon ya da değişken yazamazsın
print ("spor dalının karakter sayısı:", len(spor_dali))
print ("yasşın karakter sayısı:", len(yas))
print ("yılın karakter sayısı:", len(yil))