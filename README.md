#ceaser cipher
char =""

#function
def rightshift():
 for character in tobeencrypt:
    global char
    if character.isupper():
        encrypted = chr((ord(character)+int(shiftno) -65)% 26 +65)
        char = char +encrypted
        #print('the characters encrypted are ', char)
    if character.islower():
        #y =ord(character)
        #print('ascii value',y)
        encrypted = chr((((ord(character)) + int(shiftno) -97 )% 26) +97)
        #print('',encrypted)
        #encrypted = str(((int(ord(character))) + shiftno -97)% 26 +97)
        char = char + encrypted
        #print('the results are ', char)

 print('the result is ', char)

    

def leftshift():
 for character in tobeencrypt:
    global char
    if character.isupper():
        encrypted = chr((ord(character)- int(shiftno) -65)% 26 +65)
        char = char +encrypted
        #print('the characters encrypted are ', char)
    if character.islower():
        #y =ord(character)
        #print('ascii value',y)
        encrypted = chr((((ord(character)) - int(shiftno) -97 )% 26) +97)
        #print('',encrypted)
        #encrypted = str(((int(ord(character))) + shiftno -97)% 26 +97)
        char = char + encrypted
        #print('the characters encrypted are ', char)

 print('the result is ', char)



#input from user
tobeencrypt = input('enter the characters which has to be encrypted or decrypted ')
shiftno = input ('enter the no of shift to be done for encryption')
rl = input(''' Choose:
            1 to shift left encrypt  / to decrypt right shift
            2 to shift  right encrypt  /to decrypt left shift
         ''')
if (rl == '1'):
    leftshift()
elif (rl == '2'):
    rightshift()
else:
   print('the option is invalid')



