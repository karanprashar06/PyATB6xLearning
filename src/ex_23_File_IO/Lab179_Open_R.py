try:
    with open('testdata.txt', 'r') as file:
        #content = file.read()
        content2 = file.readlines() # list manner
        #print(content)
        print(content2)
except FileNotFoundError as fnfe:
    print(fnfe)