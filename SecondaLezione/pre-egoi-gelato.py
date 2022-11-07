with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split(" ")[0])
c = int(lines[0].split(" ")[1].replace("\n", ""))

P = [int(x) for x in lines[1].replace("\n", "").split(" ")]

print(P)
P.sort(reverse=True)
print(P)

somma = 0
ris = 0
while somma < c:
    somma += P[ris]
    ris+=1

print(ris)
