print("welcome to treasure island!")
print("your mission is to find the treasure")
choice1 = input("<----left.  Choose a path  .right----->\n")
if choice1 == "left":
    print("you find a red brick path leading to a clearing within the tomb, as you walk forward you see a lake with alot of debries flowing with a great speed.")
    choice2 = input("<----swim. Choose a path .wait----->\n")
    if choice2 == "wait":
     print("you decide its not wise to try to cross this river. as you look around for an alternative path, you see 3 doors that seem to appeared out of nowhare.")
     print("you can clearly see that the doors seem to lead to nowhare but there is a strange field of magic around them. perhaps they can directly lead you to the treasure!")
     print("choose a door")
     choice3 = input("<-----red <-----yellow-----> blue----->\n")
     if choice3 == "yellow":
       print("YOU DID IT! YOU FOUND THE TREASURE ^-^........how are you gonna get out?")
     elif choice3 =="red":
      print("                                                GAME OVER                                         ")
      print("you get sucked into an amber world full of fire, you burn to ashes before you even hit the ground.")
     elif choice3 == "blue":
      print("                                            GAME OVER                                                   ")
      print("you get sucked into the depths of the ocean. Before you can even react you are crushed into a fine mist.")
    else:
      print("                                          GAME OVER                                                           ")
      print("you overestimate you athletic capabilites, you could not keep up with the rapid stream and drown to your death")

else:
 print("    GAME OVER     ")
 print("you fell in a trap")
    


