import random
import rpc_module

rpc_choice = [rpc_module.rock,rpc_module.paper,rpc_module.scissor]
com_choice = random.randint(0,2)

print("WELCOME TO ROCK PAPER SCISSORS!")
choice = int(input("enter your choice : rock(0),paper(1),scissors(2)\n"))
if choice == com_choice:
    print("you chose")
    print(rpc_choice[choice],"\n")
    print("computer chose")
    print(rpc_choice[com_choice],"\n")
    print("its a tie!")
elif choice == 0 & com_choice == 2:
     print("you chose")
     print(rpc_choice[choice],"\n")
     print("computer chose")
     print(rpc_choice[com_choice],"\n")
     print("you win!")
elif choice == 1 & com_choice == 0:
     print("you chose")
     print(rpc_choice[choice],"\n")
     print("computer chose")
     print(rpc_choice[com_choice],"\n")
     print("you win!")    
elif choice == 2 & com_choice == 1:
     print("you chose")
     print(rpc_choice[choice],"\n")
     print("computer chose")
     print(rpc_choice[com_choice],"\n")
     print("you win!")     
else:
     print("you chose")
     print(rpc_choice[choice],"\n")
     print("computer chose")
     print(rpc_choice[com_choice],"\n")
     print("you lose!")