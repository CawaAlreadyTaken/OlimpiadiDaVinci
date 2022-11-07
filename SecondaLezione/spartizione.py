with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split(" ")[0])
p = int(lines[0].split(" ")[1].replace("\n", ""))

tot = 0
k = 1
while n > 0:
    if (n <= k):
        tot += n
        print(tot)
        exit(0)
    n-=k
    n-=(p-1)
    tot += k
    k+=1

print(k)
