#bonus challenge
import random
score_player = 0
score_computer = 0
choices = ['rock', 'paper', 'scissors']
while score_player < 5 or score_computer < 5:
    player_choice = str(input('tanlovingizni kiriting: '))
    computer_choice = random.choice(choices)
    if player_choice not in choices: 
        print("noto'g'ri so'zni kiritdingiz")
        break
    if player_choice == choices[0]:
        if computer_choice == choices[0]:
            score_player = score_player + 1
            score_computer = score_computer + 1
        if computer_choice == choices[1]: score_computer =+1
        if computer_choice == choices[2]: score_player =+1
    if player_choice == choices[1]:
        if computer_choice == choices[0]: score_player =+1        
        if computer_choice == choices[1]: 
            score_player =+1
            score_computer =+1
        if computer_choice == choices[2]: score_computer =+1
    if player_choice == choices[2]:
        if computer_choice == choices[0]: score_computer =+1        
        if computer_choice == choices[1]: score_player =+1    
        if computer_choice == choices[2]: 
            score_computer =+1
            score_player =+1
print(score_computer, ':', score_player)

