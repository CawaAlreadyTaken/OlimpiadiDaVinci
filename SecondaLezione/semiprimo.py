def isPrime(n):
    i = 2
    while i * i <= n:
        if (n % i == 0):
            return False
        i+=1
    return True

with open("input.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split(" ")[0].replace("\n", ""))

i = 2
while i * i <= n:
    if n % i == 0:
        if (isPrime(i) and isPrime(n//i)):
            print(i, n//i)
            exit(0)
        else:
            print(-1)
            exit(0)
    i += 1

print(-1)
