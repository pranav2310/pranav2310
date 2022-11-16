import random 
 print("~~~Welcome to Snake Water Gun Game~~~") 
 t=10 
 u=0 
 c=0 
 d=0 
 while t>0: 
     l=["s", "w", "g"] 
     compchoice=random.choice(l) 
     uinput=input("Choose Snake , Water or Gun by typing s for Snake , w for water and g for Gun enter n if you don't want to play the game") 
     if uinput=="s": 
         if compchoice=="w": 
             print("~You won this round~ ") 
             print("Snake Drank the Water") 
             u=u+1 
         elif compchoice=="g": 
             print("~You lost this round~") 
             print("Computer Shot your Snake") 
             c=c+1 
         elif compchoice=="s": 
             print("~Draw~") 
             print("You and Computer both Chose Snake") 
             d=d+1 
     if uinput=="w": 
         if compchoice=="g": 
             print("~You won this round~ ") 
             print("Gun Sank in the water") 
             u=u+1 
         elif compchoice=="s": 
             print("~You lost this round~") 
             print("Your water was drunk by Snake") 
             c=c+1 
         elif compchoice=="w": 
             print("~Draw~") 
             print("You and Computer both Chose Water") 
             d=d+1 
     if uinput=="g": 
         if compchoice=="s": 
             print("~You won this round~ ") 
             print("You Shot computers Snake") 
             u=u+1 
         elif compchoice=="w": 
             print("~You lost this round~") 
             print("Your Gun sank in the Water") 
             c=c+1 
         elif compchoice=="g": 
             print("~Draw~") 
             print("You and Computer both Chose Gun") 
             d=d+1 
     t=t-1 
 print("~~~Game Over~~~") 
 if u>c: 
     print("~~User Won~~") 
     print("User's Points are", u, "Computer's points are", c, "Number of Draw Rounds", d) 
 elif u<c: 
     print("~~Computer Won~~") 
     print("User's Points are", u, "Computer's points are", c, "Number of Draw Rounds", d) 
 else: 
     print("~~Draw~~ ")
