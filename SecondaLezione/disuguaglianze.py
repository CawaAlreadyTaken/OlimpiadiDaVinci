with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].replace("\n", ""))
s = lines[1].replace("\n", "")

alto = n
basso = 1

for x in s:
    if (x == ">"):
        print(alto, end=" ")
        alto-=1
    else:
        print(basso, end=" ")
        basso+=1

print()
print(alto)
print(alto == basso)
