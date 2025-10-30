#hangman
import random
import makeDashes
import layers

ran_word=['mouse','cat','dog','gamble']
chosen_word = random.choice(ran_word)
ln = len(chosen_word)
dashs = (makeDashes.make_dash(ln))
da = ""
game_over = 0
gussed = 0
layer = 1
while game_over == 0:

     da = "".join(dashs)
     print(da)
     print(layers.layer(layer))
     final = "".join(dashs)
     if final == chosen_word:
      game_over = 1
      print("YOU WON !!!!!")
      break
     guess = input("guess the letter : ").lower()
     pos = chosen_word.find(guess)
     if pos >= 0:
        dashs[pos] = guess

     else:
       if layer < 6:
        layer += 1
       else: 
        print("GAME OVER !!!!!!")
        game_over = 1  
       
     
     






    



    
    

