inp = int(input())
number = 0
for x in range(inp):
    inp = input()
    if inp == "++X":
        number += 1
    elif inp == "X++":
        number += 1
    elif inp == "--X":
        number -= 1
    elif inp == "X--":
        number -= 1
print(number)