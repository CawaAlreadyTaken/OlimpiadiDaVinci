with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].replace('\n', ''))
a = [int(x) for x in lines[1].replace('\n', '').split(' ')]

mass = 0
somma = 0
for el in a:
    somma += el
    if (somma > mass):
        mass = somma
    if (somma < 0):
        somma = 0

with open("output.txt", "w") as f:
    f.write(str(mass)+'\n')
    
