input_string = "hello, world!"
# a,e, i,o,u.
# vowel ?

vowels = "aeiou"

vowel_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowel_count += 1
        result.append(char)

print(vowel_count)
print(result)