x = {
    "LOL" : "Komik bir şeye verilen cevap",
    "CRINGE" : "Garip ya da utandırıcı bir şey",
    "ROFL" : "Bir şakaya karşılık cevap",
    "SHEESH" : "Onaylamamak",
    "CREEPY" : "Korkunç",
    "AGGRO" : "Agresifleşmek/Sinirlenmek",
    }

y = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if y in x.keys():
    print(x[y])
else:
    print("Kelimeyi Bizde Bilmiyoruz :(")
    
#----------------------------------------------------------------------------------------------------------------------#
