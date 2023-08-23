#rock paper scissor
def rockpaperscissors():
    RPS_dict = {"Rock", "Paper", "Scissor"}
    
    RPS_list = list(RPS_dict)
    
    return RPS_list[0]
    
def fight(user, comp):
    str_fight = user + ", " + comp
    draw = ["Rock, Rock", "Paper, Paper", "Scissor, Scissor"]
    win = ["Rock, Scissor", "Paper, Rock", "Scissor, Paper"]
    loss = ["Rock, Paper", "Paper, Scissor", "Scissor, Rock"]
    
    if str_fight in draw:
        print("Both user and computer DRAWS!")
    elif str_fight in win:
        print(user, " VS ", comp, ". User win with ", user)
    elif str_fight in loss:
        print(user, " VS ", comp, ". Computer win with ", comp)
    else:
        pass
    
print("1 - Rock, 2 - Paper, 3 - Scissor")    
user_choice = input ("Enter number :")
print(user_choice)

RPS_user = ""
RPS_comp = ""

if user_choice == "1":
    RPS_choice = "Rock"
    print("User: ", RPS_choice)
    RPS_comp = rockpaperscissors()
    print("Computer: ", RPS_comp)
    fight(RPS_choice, RPS_comp)
elif user_choice == "2":
    RPS_choice = "Paper"
    print("User: ", RPS_choice)
    RPS_comp = rockpaperscissors()
    print("Computer: ", RPS_comp)
    fight(RPS_choice, RPS_comp)
elif user_choice == "3":
    RPS_choice = "Scissor"
    print("User: ", RPS_choice)
    RPS_comp = rockpaperscissors()
    print("Computer: ", RPS_comp)
    fight(RPS_choice, RPS_comp)
else:
    print("Please choose the right input.")
