#ceaser cypher
import encode
print("welcome to the cypher")
word = input("enter the cypher ")
shift = input("enter the shift ")
print(encode.cypher(word,shift))

def cypher(word,shift):
    cipher_text = ""
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in word:
        shift_pos = letters.index(letter) + shift
        cipher_text = cipher_text + letters[shift_pos]
    return cipher_text
    
    









    

 
    
