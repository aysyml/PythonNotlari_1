""" syntax to output"""
print("Hello World")

""" COMMENT"""
# Bu yorum satırıdır,yada """...""""

"""Değişken Tanımlama"""
# _pythonogrenme , PythonOgrenme ,Pythonogrenme,python_ogrenme...
# Örneğin bu kullanım olmaz == >  python-ogrenme

"""Değeri 3 olan değişkeni tanımlama"""
# x = 3 , x =int(3) ikiside olur.Python veri tiplerini otomatik algılar.
# y = 2.8 , y = float(2.8)....

"""Değişkenin veya Nesnenin veri tipini öğrenmek için"""
# type() kullanılır.
# Örn : print(type(x))

"""Fonksiyon Tanımlamak"""
# def fonksiyon1():

"""Bir dizedeki ilk karakteri döndürmek için"""
# z = "python notları " [0]
# print(z)  ==>Bize p sonucunu verir.

"""Başındaki ve sonundaki boşlukları atmak için"""
# strip()   kullanılır

"""Bir dizeyi büyük harflere döndürmek için"""
# upper()  kullanılır.

"""Bir dizenin elemanlarını değiştirmek için """
# replace()   kullanılır

"""LIST tanımlama"""
# ["java", "python", "php"]

"""TUPLE tanımlama"""
# ("java", "python", "php")

"""SET tanımlama"""
# {"java", "python", "php"}

"""DICTIONARY tanımlama"""
# {"marka": "mercedes", "renk": "beyaz"}

"""LIST:Sıralanır, Değiştirilebilir ve Yinelenen üyelere izin verir"""
"""SET: Yinelenen üyelere izin vermez"""

"""IF ifadesi yazma """
# if x > y:

"""While döngüsü yazma """
# while x > y:

"""FOR dongusu yazma"""
# for x in y:

"""Döngüyü durdurmak,kırmak için """
# break ifadesi kullanılır.

"""Lambda fonksiyonu"""
# Avantajları
# Az kod yazılır,tek satırlık koddan ibarettir.
# Daha düzenli kod
"""Normal Fonksiyon Tanımlaması"""


# 3 ile çarpma
def sayiCarp(sayi):
    return sayi * 3


print("Normal Fonksiyon :", sayiCarp(2))
# sayiCarp fonksiyonumuzu 2 ile çarptık.2*3 olacak.Sonuc=6

"""Lambda Fonksiyonu Tanımlaması"""
# FonksiyonAdi = lambda paremetre1,paremetre2: dönüş değeri
# Normal fonksiyon tanımlamasındaki örnek üzerinden
sayiCarp2 = lambda parametre1: parametre1 * 3
print("Lambda Fonksiyonu:", sayiCarp2(2))

"""Kullanıcı Girdi işlemleri"""
kullaniciAdiniz = input("Kullanıcı adınız :")
print("Kullanıcı Adınız :" + kullaniciAdiniz)

"""Veri Türleri"""
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

"""Operatorler"""
"""

Operator	Adı	             Örneğin 
+	        Toplama	        x + y	
-	        Çıkarma     	x - y	
*	        Çarpma	        x * y	
/	        Bölme	        x / y	
%	        Modül	        x % y	
**	        Üs alma     	x ** y	
"""

"""Sınıf Tanımlama"""


class Araba:
    x = 5


print(Araba)

"""Sınıftan nesne oluşturma"""

nesne1 = Araba()
print(nesne1.x)

""" __init__"""
# Bir classtan nesne türeteceksek __init__ kullanırız.(Classın ilk metodu olmak zorundadır)
# Class içinden türetilen nesnelere ait özellikler bu metotla nesnelere atanır.

"""Örneğin"""


class Kisi:
    def __init__(self, ad, yas, sehir):
        self.isim = ad
        self.yas = yas
        self.yasadigiSehir = sehir


kisi1 = Kisi("Ayşe", 22, "Bursa")
print(kisi1.isim)
print(kisi1.yas)
print(kisi1.yasadigiSehir)

"""Nesneler ayrıca metotlar,fonksiyonlar içerebilir"""


class Insanlar:
    def __init__(self, kisiAd, kisiYas, kisiSehir):
        self.kisiAd = kisiAd
        self.kisiYas = kisiYas
        self.kisiSehir = kisiSehir

    def fonksiyonum(self):
        print("Selam benim adım " + self.kisiAd)


insan = Insanlar("Mehmet", 16, "İstanbul")
insan.fonksiyonum()

# Not : Eğer eksik parametre girerseniz     insan = Insanlar("Mehmet", 16)
# TypeError: __init__() missing 1 required positional argument: 'kisiSehir' hatası alırsınız.

"""Detaylar"""
# sınıfa ait erişim için self kullanılır.
