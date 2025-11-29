# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.


string = "automation"

string1 = input("\n Enter the input string : ")

char_count ={}
for char in string1:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)