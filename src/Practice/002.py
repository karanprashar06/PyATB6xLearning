#Write the code for first non reoccuring string character in a string


s=set()
print(s)
def first_non_repeating(str):
    for i in str:
        if str.count(i)==1:
            s.add(i)

    return s


print(first_non_repeating("inidnsdnasindnqk"))
print(s)
