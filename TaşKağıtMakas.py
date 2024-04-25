import random
import time

secenek = {"t": "taş", "k": "kağıt", "m": "makas"}

def oyun():
    kazanç = 0
    kayıp = 0
    print("Oyun başlıyor")

    while True:
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        rakip = random.choice(list(secenek.values()))
        hamle = input("Taş, kağıt, makas? ('q' veya 'Q' ile çıkış): ").lower()

        if hamle == 'q':
            print("Çıkış yapılıyor...")
            time.sleep(1)
            print("Siz {}, bilgisayar {} puanla bitirdiniz".format(kazanç, kayıp))
            break        
        elif hamle in secenek.keys():
            hamle = secenek[hamle]
        elif hamle.startswith(tuple(secenek.keys())):
            hamle = secenek[hamle[0]]
        else:
            print("Geçersiz seçim!!")
            continue

        if hamle == rakip:
            print("Berabere!")
        elif (hamle == "taş" and rakip == "kağıt") or \
             (hamle == "kağıt" and rakip == "makas") or \
             (hamle == "makas" and rakip == "taş"):
            print("Kaybettiniz!")
            kayıp += 1
        else:
            print("Kazandınız!")
            kazanç += 1

        print("Skor: Siz {} - Bilgisayar {}".format(kazanç, kayıp))

oyun()
