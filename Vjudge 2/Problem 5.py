inp = input()
count = 1
flag = True
for i in range(1, len(inp)):
    if inp[i - 1] == inp[i]:
        count += 1
        if count == 7:
            print("YES")
            flag = False
            break
    else:
        count = 1
if flag:
    print("NO")