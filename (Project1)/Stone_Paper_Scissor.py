import random


def gamewin(c, y):
    if c == y:
        return None
    elif c == 's':
        if y == 'p':
            return False
        elif y == 'sc':
            return True
    elif c == 'p':
        if y == 's':
            return False
        elif y == 'sc':
            return True
    elif c == 'sc':
        if y == 's':
            return True
        elif y == 'p':
            return False
out=1
i=0
while(out==1):
   
    print("Computers Turn : Computer will choose between Stone(S),Paper(P) & Scissor(S)")
    randno = random.randint(1,3)
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'p'
    else:
        comp = 'sc'
    print("Your Turn : Please choose between Stone(S),Paper(P) & Scissor(S)")
    you=input()
    
    print("The Computer Chose : ", comp)
    
    print("You Chose : ", you)
    
    a = gamewin(comp, you)
    
    if(a is None):
        print("Its a tie")
        i=i+0
        print("Your Score is unchanged")
        continue
    elif(a==False):
        
        print("Your Lose :-( ")
        print("Play Again")
        print(i)
        out=0
          
    else:
        print("You Win !!!")
    i=i+1
    print("Your Score is :",i)
    score=i
    
    with open('hiscore.txt') as f:
        hiscore=int(f.read())
        score=score-1
    
    if score>hiscore:
        with open('hiscore.txt','w') as f:
            f.write(str(score))
    i=0
