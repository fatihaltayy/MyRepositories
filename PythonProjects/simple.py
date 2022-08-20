print("#############################################")
print("Lütfen yapmak istediğiniz işlemi giriniz:")
print("1 - Kare Alanı Bulma")
print("2 - Dikdörtgen alanı bulma ")
print("3 - Ortalama Hız bulma")
print("4 - Merkezcil ivme hesaplama")
print("5 - KAtı cisimlerdeki yüzey basınç hesaplama")
a = int(input())
    
def kare(x):
    print("#############################################")
    print("Bir kenarı girilen karenin alanı bulma")
    x=int(input("Lütfen Karenin bir kenarını giriniz:"))
    Alan = x*x
    print("Alan :",Alan)

    
def dikdortgen():
    print("#############################################")
    print("Dikdörtgenin Alanını Bulma ")
    x=int(input("Lütfen bir kenarı giriniz :"))
    y=int(input("Lütfen diğer kenarı giriniz :"))
    alan = x*y
    print("Alanı :",alan)

def orthiz():
    print("#############################################")
    print("Ortalama hız Bulma ")
    x=int(input("Gidilen Toplam Yolu Giriniz :"))
    y=int(input("Gidilen Toplam Zamanı Giriniz :"))
    ort= x/y
    print("Ortamalam Hız :",ort)
def merivme():
    print("#############################################")
    print("Merkezcil ivme bulma :")
    x =int(input("Lütfen hızı giriniz :"))
    y =int(input("Lütfen cismin döndüğü veya hareket ettiği çember veya dairenin yarıçapını giriniz :"))
    ivme = (x*x)/y
    print("Merkezcil İvme :",ivme)

def katıyüzeybasinc():
    print("#############################################")
    print("Katılarda Yüzeye yapılan basıncı bulma ")
    x=int(input("Lütfen yapılan kuvveti giriniz :"))
    y=int(input("Katı cismin yüzey alanını giriniz :"))
    basinc =x/y
    print("Yüzeye yapılan basınç",basinc)


if a == 1:
    kare()
elif a == 2:
    dikdortgen()
elif a == 3:
    orthiz()
elif a == 4:
    merivme()
elif a == 5:
    katıyüzeybasinc()






    
