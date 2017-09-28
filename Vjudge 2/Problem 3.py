count = 0
n = int(input())
inp = input()
for i in range(n - 1):
    if inp[i] == inp[i + 1]:
        count += 1

print(count)