str = input().lower()
vowels = ['a', 'o', 'y', 'e', 'u', 'i']
result = ""
for letter in str:
    if letter not in vowels:
        result += "." + letter
print(result)