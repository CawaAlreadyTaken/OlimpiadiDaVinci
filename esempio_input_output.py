with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].replace('\n', ''))
a = [int(x) for x in lines[1].replace('\n', '').split(' ')]
print(a)
#soluzione

with open("output.txt", "a") as f:
    f.write(str(soluzione)+'\n')
    
