def dicerollsim():
    dice = {"1" ,"2", "3", "4", "5", "6"} # using dictionary or set because the data will be unordered

    list_dice = list(dice) # converting the dictionary or set to list so that data can be access
    
    dice1 = int(list_dice[0])
    dice2 = int(list_dice[5])
    
    print("Dice 1: ", dice1) 
    print("Dice 2: ", dice2)
    print("Total Move: ", dice1 + dice2) # count total move
    
dicerollsim()
