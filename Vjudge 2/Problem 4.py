inp = input()

arr = []
for i in range(len(inp)):
	if inp[i] not in arr:
		arr.append(inp[i])

if len(arr) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")