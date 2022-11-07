with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split(" ")[0])

P = [int(x) for x in lines[1].replace("\n", "").split(" ")]

P.sort()

somma = sum(P)
ris = 0
while somma <= 0:
    somma += (-2)*P[ris]
    ris+=1

print(ris)
