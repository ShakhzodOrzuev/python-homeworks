Password = str(input('enter password: '))
i = 0
j = 0
a = int(len(Password))
if a < 8: 
    print('Password is too short.')
else:
    while i < a: 
        if Password[i].isupper():
            j += 1
        else: pass
        i += 1 
    if j == 0: 
        print('Password must contain an uppercase letter.')
    else: 
        print('Password is strong.')