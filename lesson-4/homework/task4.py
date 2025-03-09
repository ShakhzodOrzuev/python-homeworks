import random
a = random.randint(1,100)
b = int(input('taxmin qilinayotgan sonni kiriting: '))
i = 1
list_answer = ['Y', 'YES', 'y', 'yes', 'ok']
while i < 11: 
    if i == 10: 
            c = str(input("You lost. Want to play again?" ))
            if c in list_answer:
                 i = 1
            else: 
                print('good bye') 
                break                
    if a < b: 
        print("Too high"); i +=1; b = int(input('taxmin qilinayotgan sonni kiriting: '))
    elif a > b: 
        print("Too low"); i +=1;  b = int(input('taxmin qilinayotgan sonni kiriting: '))
    elif a == b: 
        print('you guessed it right');
        break
 