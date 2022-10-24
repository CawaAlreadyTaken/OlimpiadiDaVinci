with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].replace('\n', '').split(' ')[0])
k = int(lines[0].replace('\n', '').split(' ')[1])
a = [int(x) for x in lines[1].replace('\n', '').split(' ')]

somma = 0
for i in range(k):
    somma += a[i]

mass = somma
for i in range(1, n-k+1):
    somma -= a[i-1]
    somma += a[i+k-1]
    if (somma > mass):
        mass = somma

with open("output.txt", "w") as f:
    f.write(str(mass)+'\n')
