secret_number=78
t=0

i=1
while(i==1):
    t=t+1
    guess = int(input("try and make a guess to find the number."))
    dif=((guess)-(secret_number))
    if dif>=10:
        print("too large")
    elif dif in range (1,9):
        print("little large")
    elif dif<=(-10):
        print("too small")
    elif dif in range((-9),(-1)):
        print("little small")
    else:
        print("winner winner chicken dinner")
        break

print("tries=",t)