"""Basic Python exercises with simple examples.

Open this file and try the exercises below. Each function includes a short description
and a small sample implementation.
"""


def story_exercise():
    """Ask for name and city, then print a short story."""
    name = input("Lütfen adınızı giriniz: ")
    city = input("Lütfen yaşadığınız şehri giriniz: ")
    story = f"""
{name} sabah erkenden uyanıp {city} sokaklarında yürümeye başladı.
Güneş yeni doğuyordu ve hava hafif serindi. Küçük bir kafe bulup sıcak bir çay içti.
Birden dışarıda bir köpek havlamaya başladı. Merakla dışarı çıkıp köpeğin yanına gitti.
Köpek ona dostça baktı ve kuyruğunu salladı. {name} köpeğin aç olabileceğini düşündü.
Hemen bir fırına gidip biraz ekmek aldı. Köpeğe uzattığında köpek hızla yedi.
Bu olay {name} i mutlu etti. Günün geri kalanında {city} in güzel yerlerini keşfetti.
{name}, {city} in ne kadar güzel olduğunu düşündü. Akşam olunca eve dönmek için yürümeye başladı.
Yolda eski bir arkadaşını gördü. Arkadaşıyla kahve içip sohbet etti. Sonra eve dönerken gökyüzüne baktı.
Yıldızlar parlıyordu ve {name} huzur doluydu.
"""
    print(story)


def rectangle_area_exercise():
    """Calculate the area of a rectangle from width and height."""
    width = float(input("Dikdörtgenin genişliğini giriniz: "))
    height = float(input("Dikdörtgenin yüksekliğini giriniz: "))
    area = width * height
    print(f"Dikdörtgenin alanı: {area}")


def vowel_count_exercise():
    """Count the number of vowels in a user-input string."""
    text = input("Bir cümle yazınız: ")
    vowels = "aeiouAEIOUıİöÖüÜâÂêÊîÎôÔûÛ"
    count = sum(1 for ch in text if ch in vowels)
    print(f"Cümlenizde {count} sesli harf var.")


def even_odd_exercise():
    """Check whether a number is even or odd and positive or negative."""
    number = int(input("Bir sayı giriniz: "))
    parity = "çift" if number % 2 == 0 else "tek"
    sign = "pozitif" if number > 0 else "negatif" if number < 0 else "sıfır"
    print(f"Girdiğiniz sayı {parity} ve {sign}.")


def favorite_things_exercise():
    """Ask for a few favorite things and print them with indexes."""
    favorites = []
    for i in range(3):
        item = input(f"Favori şey {i + 1} i giriniz: ")
        favorites.append(item)
    print("Senin favorilerin:")
    for index, value in enumerate(favorites, start=1):
        print(f"{index}. {value}")


def main():
    print("Temel Python alıştırmalarına hoş geldiniz!")
    print("1 - Hikaye oluşturma")
    print("2 - Dikdörtgen alanı")
    print("3 - Sesli harf sayısı")
    print("4 - Çift/tek kontrol")
    print("5 - Favori şeyler")
    choice = input("Hangi alıştırmayı çalıştırmak istersiniz? (1-5): ")

    if choice == "1":
        story_exercise()
    elif choice == "2":
        rectangle_area_exercise()
    elif choice == "3":
        vowel_count_exercise()
    elif choice == "4":
        even_odd_exercise()
    elif choice == "5":
        favorite_things_exercise()
    else:
        print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı giriniz.")


if __name__ == "__main__":
    main()
