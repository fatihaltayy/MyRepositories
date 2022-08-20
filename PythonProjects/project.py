from random import randint
from tkinter import*
import time
import random
import sys

print("#############################################")
print("Lütfen yapmak istediğiniz işlemi giriniz:")
print("1 - Kare Alanı Bulma")
print("2 - Dikdörtgen alanı bulma ")
print("3 - Fibanacci Dizisi Oluşturma")
print("4 - Faktoriyel hesaplama ")
print("5 - Sayı Tahmin Oyunu")
print("6 - Vur-Kaç Oyunu")
print("7 - Hesap Makinesi")

a = int(input())

def fibonacci():
    print("Fibonacci Dizisi, her sayının kendisinden bir önceki sayı ile toplanması ile elde edilen sayılar serisidir.")
    nterms = int(input("Kaç adet Sayı oluştursun ?"))


    n1 = 0
    n2 = 1
    count = 2

    if nterms <= 0:
       print("Lütfen Pozitif Sayı giriniz.")
    elif nterms == 1:
       print("Oluşan fibonacci dizisi ",nterms,":")
       print(n1)
    else:
       print("Oluşan fibonacci dizisi",nterms,":")
       print(n1,",",n2,", ")
       while count < nterms:
           nth = n1 + n2
           print(nth,' , ')
           n1 = n2
           n2 = nth
           count += 1

def kare():
    print("#############################################")
    print("Bir kenarı girilen karenin alanı bulma")
    x = int(input("Lütfen Karenin bir kenarını giriniz:"))
    Alan = x * x
    print("Alan :", Alan)

def dikdortgen():
    print("#############################################")
    print("Dikdörtgenin Alanını Bulma ")
    x = int(input("Lütfen bir kenarı giriniz :"))
    y = int(input("Lütfen diğer kenarı giriniz :"))
    alan = x * y
    print("Alanı :", alan)

def faktoriyel():
    num = int(input("Hesaplanıcak Faktoriyeli giriniz: "))

    factorial = 1

    if num < 0:
        print("Faktoriyel negatif olamaz")
    elif num == 0:
        print("Sıfır faktoriyel 1 dir.")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(num, "faktoriyel :", factorial)

def SayiTahmin():
    rand = randint(1, 100)
    sayac = 0

    while True:
        sayac += 1
        sayi = int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
        if (sayi == 0):
            print("Oyunu İptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha Yüksek Bir Sayı Girin.")
            continue
        elif sayi > rand:
            print("Daha Düşük Bir Sayı Girin.")
            continue
        else:
            print("Rastele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))

def oyun():

    class Oyuncu():
        def __init__(self, isim, can=5, enerji=100):
            self.isim = isim
            self.darbe = 0
            self.can = can
            self.enerji = enerji

        def mevcut_durumu_görüntüle(self):
            print('darbe:', self.darbe)
            print('can:', self.can)
            print('enerji:', self.enerji)

        def saldır(self, rakip):
            print('Bir saldırı gerçekleştirdiniz.')
            print('Saldırı sürüyor. Bekleyiniz')

            for i in range(10):
                time.sleep(.3)
                print(".", end="", flush=True)

            sonuç = self.saldırı_sonucunu_hesapla()

            if sonuç == 0:
                print("\nSONUÇ:kazanan taraf yok")

            if sonuç == 1:
                print("\nSONUÇ:rakibinize hasar verdiniz")
                self.darbele(rakip)
            if sonuç == 2:
                print("\nSONUÇ:rakibinizden darbe aldınız")
                self.darbele(self)

        def saldırı_sonucunu_hesapla(self):
            return random.randint(0, 2)

        def kaç(self):
            print("Kaçılıyor...")
            for i in range(10):
                time.sleep(.3)
                print("\n", flush=True)

            print("Rakibiniz sizi yakaladı")

        def darbele(self, darbelenen):
            darbelenen.darbe += 1
            darbelenen.enerji -= 1
            if (darbelenen.darbe % 5) == 0:
                darbelenen.can -= 1
            if darbelenen.can < 1:
                darbelenen.enerji = 0
                print("Oyunu {} kazandı !".format(self.isim))
                self.oyundan_çık()

        def oyundan_çık(self):
            print("Çıkılıyor...")
            sys.exit()

    ##################################
    # Oyuncular
    siz = Oyuncu('Ahmet')
    rakip = Oyuncu('Mehmet')
    # Oyun başlangıcı
    while True:
        print('Şu anda rakibinizle karşı karşıyasınız.',
              'Yapmak istediğiniz hamle: ',
              'Saldır: s',
              'Kaç: k',
              'Çık: q', sep='\n')
        hamle = input('\n> ')
        if hamle == 's':
            siz.saldır(rakip)

            print('Rakibinizin durumu')
            rakip.mevcut_durumu_görüntüle()

            print('Sizin durumunuz')
            siz.mevcut_durumu_görüntüle()
        if hamle == 'k':
            siz.kaç()

        if hamle == 'q':
            siz.oyundan_çık()

def HesapMakinesi():
    # GitHub dan yararlanılarak yapılmıştır......
    class App(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.parent = parent
            self.initUI()

        def initUI(self):
            self.parent.title("Hesap Makinesi")
            self.pack(fill=BOTH, expand=True)
            global value
            value = 0
            global num1
            num1 = StringVar()
            global num2
            num2 = StringVar()
            global res
            res = StringVar()

            frame1 = Frame(self)
            frame1.pack(fill=X)

            lbl1 = Label(frame1, text=" 1. Sayı :", width=15)
            lbl1.pack(side=LEFT, padx=5, pady=5)

            entry1 = Entry(frame1, textvariable=num1)
            entry1.pack(fill=X, padx=5, expand=True)

            frame2 = Frame(self)
            frame2.pack(fill=X)

            lbl2 = Label(frame2, text="2. Sayı :", width=15)
            lbl2.pack(side=LEFT, padx=5, pady=5)

            entry2 = Entry(frame2, textvariable=num2)
            entry2.pack(fill=X, padx=5, expand=True)

            frame3 = Frame(self)
            frame3.pack(fill=X)

            btnplus = Button(frame3, text="+", width=8, command=self.plus)
            btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

            btnminus = Button(frame3, text="-", width=8, command=self.minus)
            btnminus.pack(side=LEFT, anchor=N, padx=5, pady=5)

            btnmul = Button(frame3, text="*", width=8, command=self.mul)
            btnmul.pack(side=LEFT, anchor=N, padx=5, pady=5)

            btndiv = Button(frame3, text="/", width=8, command=self.div)
            btndiv.pack(side=LEFT, anchor=N, padx=5, pady=5)

            frame4 = Frame(self)
            frame4.pack(fill=X)

            lbl3 = Label(frame4, text="Sonuç", width=10)
            lbl3.pack(side=LEFT, padx=5, pady=5)

            result = Entry(frame4, textvariable=res)
            result.pack(fill=X, padx=5, expand=True)

        def errorMsg(self, msg):
            if msg == 'error':
                tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
            elif msg == 'divisionerror':
                tkinter.messagebox.showerror('Division Error', 'The value of input number 2 is 0. No dividing by 0')

        def plus(self):
            try:
                value = float(num1.get()) + float(num2.get())
                res.set(self.makeAsItIs(value))
            except:
                self.errorMsg('error')

        def minus(self):
            try:
                value = float(num1.get()) - float(num2.get())
                res.set(self.makeAsItIs(value))
            except:
                self.errorMsg('error')

        def mul(self):
            try:
                value = float(num1.get()) * float(num2.get())
                res.set(self.makeAsItIs(value))
            except:
                self.errorMsg('error')

        def div(self):
            # checks if user is trying to divide by zero
            if num2.get() == '0':
                self.errorMsg('divisionerror')
            elif num2.get() != '0':
                try:
                    value = float(num1.get()) / float(num2.get())
                    res.set(self.makeAsItIs(value))
                except:
                    self.errorMsg('error')

        def makeAsItIs(self, value):
            if (value == int(value)):
                value = int(value)
            return value

    def main():
        root = Tk()
        root.geometry("300x140")
        app = App(root)
        root.mainloop()

    if __name__ == '__main__':
        main()



if a == 1:
    kare()
elif a == 2:
    dikdortgen()
elif a == 3:
    fibonacci()
elif a == 4:
    faktoriyel()
elif a == 5:
    SayiTahmin()
elif a == 6:
    oyun()
elif a == 7:
    HesapMakinesi()