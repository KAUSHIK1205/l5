import random
playing = True
num=str(random.randint(10,20))
print("lets plaay a game in this you will have to guess my number i think between 10 to 20 !")

while playing:
    guess= input("pls enter your guess :")
    if num==guess:
        print("wow you found it")
        break
    else:
        print("wrong guess")





    