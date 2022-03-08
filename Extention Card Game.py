import random
from random import randint

Hand = 4chro
RandCards = 0

Spades = ["1Ace", "1Two", "1Three", "1Four", "1Five", "1Six", "1Seven", "1Eight", "1Nine", "1Ten", "1Jack", "1Queen", "1King"]
Clubs = ["2Ace", "2Two", "2Three", "2Four", "2Five", "2Six", "2Seven", "E2ight", "Nin2e", "2Ten", "Ja2ck", "Qu2een", "Kin2g"]
Diamonds = ["3Ace", "T3wo", "Th3ree", "Four3", "Fiv3e", "S3ix", "Seve3n", "Eigh3t", "Ni3ne", "T3en", "J3ack", "Quee3n", "K3ing"]
Hearts = ["4Ace", "Tw4o", "T4hree", "F4our", "Fi4ve", "S4ix", "Se4ven", "Ei4ght", "N4ine", "T4en", "Ja4ck", "Qu4een", "Ki4ng"]
TotalDeck = [Spades, Clubs, Diamonds, Hearts]
Suite = randint(0,3)
CardNum = 4
y=randint(0,207)
x=TotalDeck[Suite]
Shuffled = random.shuffle(TotalDeck)
aasdasdasd = Suite[y]
print(TotalDeck[aasdasdasd])
Input_Loop = True
while Input_Loop == True:
    try:
        Players = int(input("How Many Players? (2-4)"))
        if Players < 2:
            print("Please input an integer between 2 - 4")
        elif Players > 4:
            print("Please input an integer between 2 - 4")
        elif 2 <= Players <= 4:
            print("There are {} players".format(Players))
            Input_Loop = False
    except ValueError:
        print("Please input an integer between 2 - 4")