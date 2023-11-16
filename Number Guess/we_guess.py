import random
num = random.randint(0,20)
x = int(input(f"Guess the number between 1 and 20: "))
cnt = 1
while x != num:
    cnt+=1
    if x>num:
        x = int(input(f"Too high, try again: "))
    else:
        x = int(input(f"Too low, try again: "))
print(f"Congrats you got it on try number: {cnt}")