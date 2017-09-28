num = int(input())
for x in range(0, num):
    inp = input()
    if len(inp) > 10:
        print(inp[0] + str(len(inp)-2) + inp[-1])
    else:
        print(inp)
