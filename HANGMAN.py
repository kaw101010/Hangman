import random
import turtle
import csv

turtle.title('HANGMAN GAME')
l2 = []
def string_to_list(s):
    for j in s:
        l2.append(j)

def list_to_string(l,s):
    for k in l:
        s = s + k + ' '
    print(s)

b = turtle.Turtle()
b.up()
b.backward(300)
b.left(90)
b.forward(180)
b.down()
b.right(90)
b.forward(500)
b.backward(100)
b.up()
b.right(90)
b.down()
b.forward(400)
b.up()


print('WELCOME! You and the computer will now play Hangman.The rules are simple: The computer chooses a hidden word and you guess any letter that you think will be in that word. If the guessed letter is correct, it will be placed in the correct place in the word. If it is incorrect, the game will move one step closer to Hangman. All the letters are in uppercase.')
l = []
with open("words.txt","r") as wordfile:
    reader = csv.reader(wordfile)
    for row in reader:
        if row!=[]:
            l.append(row[0].strip().upper())

t = random.choice(l)
x = '_'*len(t) 
a = 7
l1 = []
d = ''
string_to_list(x)
list_to_string(l2,d)
while 1<=a<=7:
    p = input('Enter a guess: ')
    for i in range(0,len(t)):
        if p == t[i] and len(p) == 1:
            l2[i] = p
    list_to_string(l2,d)
    if '_' not in l2:
        print('Correct answer!','You have found the word.',sep = '\n')
        a = 0
        
    if p not in t and a == 7 and len(p) == 1:
        b.down()
        b.backward(400)
        b.right(90)
        b.forward(280)
        b.down()
        b.left(90)
        b.forward(100)
        b.up()
    elif p not in t and a == 6 and len(p) == 1:
        b.right(90)
        b.forward(25)
        b.left(90)
        b.forward(25)
        b.down()
        b.circle(25)
        b.up()
        
    elif p not in t and a == 5 and len(p) == 1:
        b.forward(25)
        b.left(90)
        b.forward(25)
        b.right(90)
        b.down()
        b.forward(120)
        b.up()
    elif p not in t and a == 4 and len(p) == 1:
        b.backward(80)
        b.down()
        b.right(120)
        b.forward(80)
        b.up()
    elif p not in t and a == 3 and len(p) == 1:
        b.backward(80)
        b.right(120)
        b.down()
        b.forward(80)
        b.up()
    elif p not in t and a == 2 and len(p) == 1:
        b.backward(80)
        b.right(120)
        b.forward(80)
        b.down()
        b.right(45)
        b.forward(90)
        b.up()          
    elif p not in t and a == 1 and len(p) == 1:
        b.backward(90)
        b.down()
        b.left(90)
        b.forward(90)
    
    if p not in t and len(p) == 1 and len(p) == 1:
        a = (a - 1)
        l1.append(p)
        print(l1)
        
    if p == '' or len(p) > 1:
        print('Input Invalid')
    if p not in t and a == 0:
        print('HANGMAN! You lost!','\nThe correct answer is',t)

print('If you enjoyed the game, please play again.')
        
            
            

        
        
        
