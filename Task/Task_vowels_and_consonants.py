input_string ="Goodbye"

vowels ="aeiou"

vowel_count = 0
result=[]
consonant_result=[]
consonant_count = 0
for i in input_string:
    if i in vowels:
        vowel_count += 1
        result.append(i)
    else:
        consonant_count += 1
        consonant_result.append(i)

print(vowel_count)
print(result)
print(consonant_count)
print(consonant_result)