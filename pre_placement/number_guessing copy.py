import random

p1 = int(input("P1"))
p2 = int(input("P2"))
guess_lst = []
while len(guess_lst)<5:
    d = random.randint(1,11)
    if d in guess_lst:
        continue
    else:
        guess_lst.append(d)

for i in range(3):
    