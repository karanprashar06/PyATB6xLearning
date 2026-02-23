import os

print(os.name)
print(os.getcwd())
# print(os.mkdir("AI"))

print(os.listdir())
print(os.path)
#print(os.remove("AI.txt"))
# print(os.rename("AI.txt","testdata.txt"))
ok = os.path.join(os.getcwd(), "data.txt")
print(ok)

print(os.environ.get("PATH"))
