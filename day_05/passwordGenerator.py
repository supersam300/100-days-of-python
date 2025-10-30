
# Creating a random password generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
sp_char = ['!','@','#','$','%','&','*']

n_let = int(input("How many letters do you need in your password? "))
n_num = int(input("How many numbers do you need in your password? "))
n_sp = int(input("How many special characters do you need in your password? "))

passwo = []
for _ in range(n_let):
    passwo.append(random.choice(letters))
for _ in range(n_num):
    passwo.append(random.choice(numbers))
for _ in range(n_sp):
    passwo.append(random.choice(sp_char))

random.shuffle(passwo)
final_pass = "".join(passwo)

print(final_pass)