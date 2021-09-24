#1
i = 30
while i < 31:
    print(i)
    if i == 1:
        break
    i += -1

print("LANCERING!!!")

print("--------------------------------------")

#2
i = 24
while i < 25:
    print(str(i) + "PM")
    i += -1
    if i <= 12:
        print(str(i) + "AM")
        if i == 0:
            break

print("--------------------------------------")

#3
i = 20 
while i<51:
    print(i)
    i += 2

print("--------------------------------------")

#4
dag = input("Kies uit ma, di, wo, do ,vr, za, zo :")

if dag == "ma":
    print("ma")
elif dag == "di":
    print("ma, di")
elif dag == "wo":
    print("ma, di, wo")
elif dag == "do":
    print("ma, di, wo, do")
elif dag == "vr":
    print("ma, di, wo, do, vr")
elif dag == "za":
    print("ma, di, wo, do, vr, za")
elif dag == "zo":
    print("ma, di, wo, do, vr, za, zo")
else:
    print("no")

print("---------------------------------------")

#5
word = True
while word:
    gok = input("Gok mijn word :")
    if gok == ("Quit"):
        word = False
        print("goed gedaan")

print("----------------------------------------")

#6
a = 50
b=0
while b < 1001:
    print(b)
    b += a + 1