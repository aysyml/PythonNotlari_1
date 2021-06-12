# open()İşlevi, iki parametre alır; dosya adı ve mod .
"""Bir dosyayı açmak için dört farklı yöntem (mod) vardır:"""
"""
"r"- Read  - Varsayılan değer. Okumak için bir dosya açar, dosya yoksa hata verir

"a" - Append  - Eklemek üzere bir dosya açar, mevcut değilse dosyayı oluşturur

"w" - Write  - Yazmak için bir dosya açar, yoksa dosyayı oluşturur

"x" - Create  - Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür
"""

"""Bir dosyayı okumak üzere açmak için"""
# dosyaAdi = open("demofile.txt")

"""Dosya farklı bir konumda bulunuyorsa"""
#f = open("D:\\myfiles\welcome.txt", "r") #yolunu belirtin
#print(f.read())

"""Dosyayı satır satır dolaşmak için"""
f = open("dosyalarim.txt", "r")
for x in f:
  print(x)

"""İşimiz bittiğinde dosyayı kapatmak iyidir :)"""
f = open("dosyalarim.txt", "r")
print(f.readline())
f.close()

"""Dosyaları yazma """
#Mevcut bir dosyaya yazmak için open()fonksiyona bir parametre eklemeliyiz.
"""
"a" - Ekle - dosyanın sonuna eklenir
"w" - Yaz - mevcut içeriğin üzerine yazar"""

f = open("dosyam.txt", "a")
f.write("Dosyam....")
f.close()

#open and read the file after the appending:
f = open("dosyam.txt", "r")
print(f.read())