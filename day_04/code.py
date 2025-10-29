import random

#random number from 1-10
"""""
random_int = random.randint(1,10)
print(random_int)
"""""

#random number from 0-1
"""""
random_num_0_1 = random.random()
print(random_num_0_1)
"""""

#mini project heads or tails

"""""
choice = random.randint(1,2)
hd = 1
ti = 2
u_choice = input("heads or tails : ")
if u_choice == "heads":
    if choice == hd:
     print("HEADS! you win")
    else:
     print("TAILS! you lose")
if u_choice == "tails":
    if choice == ti:
     print("TAILS! you win")
    else:
     print("HEADS! you lose")
"""""

#understanding offset and appending lists to items
"""""
#creates list

states_of_america = ["delaware","Pennsylvania","california","nebraska"]
print(states_of_america)

#manipulate element in list

states_of_america[1] = "africa"
print(states_of_america)

#append item to list

states_of_america.append("india")
print(states_of_america)
"""""

#using rand in lists

"""""
names = ["tine","mina","fein","yobo"]
#name = random.randint(0,3)
#print(names[name])
print(random.choice(names))
"""""

#nested lists
"""""
list1 = ["hi","hello","bye"]
list2 = ["bim","tim","fim"]
list3 = list1,list2
print(list3[1][1])

"""""

