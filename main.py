from smtplib import SMTP
import random

a = random.randint(10000, 99999)

dosya = open("Mail.txt", "r", encoding="utf-8")
hesap = (dosya.readline())
sifre = (dosya.readline())

gonderilecekadres = input("Sisteme kayıt olmak için mail adresinizi giriniz size bir kod yollayacağız! : ")
try:
    # Mail Mesaj Bilgisi
    konu = "Orçun Ünlü Mail Gönderme"
    mesaj = ("Orçun Ünlü Mail Gönderme sistemi için kodunuz" + "  :" + str(a))
    icerik = "Subject: {0}\n\n{1}".format(konu, mesaj)

    # Hesap Bilgileri
    mailadresi = hesap
    sifre = sifre

    # Kime Gönderilecek Bilgisi
    sendTo = gonderilecekadres

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(mailadresi, sifre)
    mail.sendmail(mailadresi, sendTo, icerik.encode("utf-8"))
    print("Kodunuz başarıyla gönderildi!")
    kod = int(input("Lütfen gönderdiğimiz kodu giriniz : "))
    if kod == a:
        print("Sisteme başarıyla kayıt oldunuz!")
        print("Giriş Ekranına Yönlendirliyor")
        print("Designed By OrçunPars")
    else:
        print("Kod hatalı yazılımı baştan çalıştırıp yeni bir kod alınız :)")
        print("Designed By OrçunPars")

except Exception as e:
    print("Hata Oluştu!\n {0}".format(e))