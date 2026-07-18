"""#Kullanıcıdan veri alarak iç içe fonksiyon kullanmadan ekrana yazdıran program yazın
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
print ("yılın karakter sayısı:", len(yil))"""

"""
Walrus (:=) operatörü, bir fonksiyonun içinde hem kullanıcıdan veri alıp (atama yapıp) 
hem de aynı satırda o veriyi başka bir fonksiyona paslamanı sağlar. 
Kodunu tam olarak senin istediğin mantığa kavuşturur:
print("Yaptığınız dpor dalı ve karakter sayısı:",(spor_dali := input( "Lutfen yapacağınız spor dalını giriniz:")),len(spor_dali))
print("Spora başladığınız yaş ve girdinin veri türü:",(yas := input ("Spora başladığınız yaşı giriniz:")),type(yas))
print("Spora başladığınız yıl ve girdinin veri türü:",(yil := input("Spora başladığınız yılı giriniz:")),type(yil))
"""

print( "yaptığınız spor dalının türü:", type(input( "yaptığınınz spor dalını giriniz:" )))
print("spora başladığınız yaşın veri türü:", type(input("spora başladığınız yaş:")))
print("spora başaldığınız yılın veri türü:", type(input("spora başdığınız yıl:")))

"""durum = "Ehliyet alabilirsin" if(int(input("yaşınınz:"))) >=18 else "yaşın tutmuyor"
print(durum)"""

