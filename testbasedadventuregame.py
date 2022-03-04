# text-based adventure game
# here many way to make text-based game

answer=input("You want to try text-based adventure game?[yes/No]: ")
if answer=="yes":
        choose=input("choose cave/jungle: ")
        if choose=="cave":
            print("alert!!!")
            choice=input("infront of you lion stand what you do?[run/fight]: ")
            if choice=="run":
                print("smart choice you save, YOU WON !!!")
            else:
                print("wrong choice, YOU DIE !!!")
        else:
            print("wrong choice, YOU DIE !!!")      
else:
    print("you missed so much adventure")  

