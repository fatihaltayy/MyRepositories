
print("Kâr ve Yüzde Hesaplama\n")

def karHesap():
    first = input("Lütfen ilk  alınan malzemenin fiyatını giriniz:")
    firstAdet =input("Lütfen ilk  alınan malzemenin adedini giriniz:")
    second =input("Lütfen satış anındaki malzemenin fiyatını giriniz:")
    secondAdet =input("Lütfen satış anındaki malzemenin adedini giriniz:")
    
    formul=((float(second)*int(secondAdet))-(int(firstAdet)*float(first)))
    
    if formul > 0:
        print("Kar :",formul)
    elif formul < 0:
        print("Zarar :",formul)
    else :
        print("Kâr veya Zarar yoktur", formul)

while True:
    try:
        karHesap()
    except ValueError:
        print("Lütfen tam sayı giriniz!")
        print("Yeniden Hesaplama:a\n",
              "Quit             :b")
        end=str(input())
    if end=="a":
        karHesap()
    else:
        break







