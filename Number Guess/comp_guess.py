import random
max_val = int(input("Enter the upper limit: "))
l = 0
h = max_val
cnt = 1
val = random.randint(l,h)
inp = input(f"Is the value {val} too high(h), too low(l) or correct(c)? ")
while inp!='c':
    if inp == 'l':
        l = val+1
    elif inp == 'h':
        h = val-1
    else:
        print("Error!")
        exit()
    cnt+=1
    val = random.randint(l,h)
    inp = input(f"Is the value {val} too high(h), too low(l) or correct(c)? ")

print(f"Answer {val} found in {cnt} tries")