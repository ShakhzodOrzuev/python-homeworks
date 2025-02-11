#Ask the user for a sentence and create an acronym from the first letters of each word.
a = str(input('matnni kiriting: '))
i = 0
b =''
for i in range(len(a)):
    if a[i] == '':
        b.append(a[i+1])
    else:
        pass
    i =+1
print(b)