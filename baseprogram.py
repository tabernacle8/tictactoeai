import random
def printboard(s1,s2,s3,s4,s5,s6,s7,s8,s9):
  print("        |        |")
  print("    "+str(s1)+"   |    "+str(s4)+"   |   "+str(s7)+"")
  print("        |        |   ")
  print("--------------------------")
  print("        |        |")
  print("    "+str(s2)+"   |    "+str(s5)+"   |   "+str(s8)+"")
  print("        |        |   ")
  print("--------------------------")
  print("        |        |")
  print("    "+str(s3)+"   |    "+str(s6)+"   |   "+str(s9)+"")
  print("        |        |   ")

  
def godefence(s1,s2,s3,s4,s5,s6,s7,s8,s9,talk,botmode,s1occ,s2occ,s3occ,s4occ,s5occ,s6occ,s7occ,s8occ,s9occ,turnnumber):
  #ACCROSS CHECKING
  #Middle row
  if(botmode==3):
    #print(""+str(s1)+","+str(s2)+","+str(s3)+","+str(s4)+","+str(s5)+","+str(s6)+","+str(s7)+","+str(s8)+","+str(s9)+","+str(talk)+","+str(botmode)+","+str(s1occ)+","+str(s2occ)+","+str(s3occ)+","+str(s4occ)+","+str(s5occ)+","+str(s6occ)+","+str(s7occ)+","+str(s8occ)+","+str(s9occ)+",")
    if(talk==1):
      print("\n*The bot is now checking if it can win")
    if(s1=="O" and s7=="O" and s4occ==False):
      return("s4")
    elif(s2=="O" and s8=="O" and s5occ==False):
      return("s5")
    elif(s3=="O" and s9=="O" and s6occ==False):
      return("s6")
  #First row
    elif(s4=="O" and s7=="O"and s1occ==False):
     return("s1")
    elif(s5=="O" and s8=="O" and s2occ==False):
      return("s2")
    elif(s6=="O" and s9=="O" and s3occ==False):
     return("s3")
  # Last row
    elif(s1=="O" and s4=="O" and s7occ==False):
      return("s7")
    elif(s2=="O" and s5=="O" and s8occ==False):
      return("s8")
    elif(s3=="O" and s6=="O" and s9occ==False):
      return("s9")
  #UP AND DOWN CHECKING
  #first row
    elif(s2=="O" and s3=="O" and s1occ==False):
      return("s1")
    elif(s5=="O" and s6=="O" and s2occ==False):
      return("s4")
    elif(s8=="O" and s9=="O" and s7occ==False):
      return("s7")
    elif(s1=="O" and s3=="O" and s2occ==False):
     return("s2")
    elif(s4=="O" and s6=="O" and s5occ==False):
     return("s5")
    elif(s7=="O" and s9=="O" and s8occ==False):
      return("s8")
  #bottom row
    elif(s1=="O" and s2=="O" and s3occ==False):
      return("s3")
    elif(s4=="O" and s5=="O" and s6occ==False):
      return("s6")
    elif(s7=="O" and s8=="O" and s9occ==False):
      return("s9")
  #DIAGONAL CHECK
  #Left to right
    elif(s5=="O" and s7=="O" and s3occ==False):
     return("s3")
    elif(s3=="O" and s7=="O" and s5occ==False):
      return("s5")
    elif(s3=="O" and s5=="O" and s7occ==False):
      return("s7")
    elif(s1=="O" and s5=="O" and s9occ==False):
     return("s9")
    elif(s5=="O" and s9=="O" and s1occ==False):
     return("s1")
    elif(s1=="O" and s9=="O" and s5occ==False):
      return("s5")
  if(talk==1):
    print("\n\n*The bot is now seeing if you are about to win..")
  if(s1=="X" and s7=="X" and s4occ==False):
    return("s4")
  elif(s2=="X" and s8=="X" and s5occ==False):
    return("s5")
  elif(s3=="X" and s9=="X"and s6occ==False):
    return("s6")
  #First row
  elif(s4=="X" and s7=="X" and s1occ==False):
    return("s1")
  elif(s5=="X" and s8=="X" and s2occ==False):
    return("s2")
  elif(s6=="X" and s9=="X"and s3occ==False):
    return("s3")
  # Last row
  elif(s1=="X" and s4=="X" and s7occ==False):
    return("s7")
  elif(s2=="X" and s5=="X" and s8occ==False):
    return("s8")
  elif(s3=="X" and s6=="X" and s9occ==False):
    return("s9")
  #UP AND DOWN CHECKING
  #first row
  elif(s2=="X" and s3=="X" and s1occ==False):
    return("s1")
  elif(s5=="X" and s6=="X" and s4occ==False):
    return("s4")
  elif(s8=="X" and s9=="X" and s7occ==False):
    return("s7")
  #Second (middle)
  elif(s1=="X" and s3=="X" and s2occ==False):
    return("s2")
  elif(s4=="X" and s6=="X" and s5occ==False):
    return("s5")
  elif(s7=="X" and s9=="X" and s8occ==False):
    return("s8")
  #bottom row
  elif(s1=="X" and s2=="X" and s3occ ==False):
    return("s3")
  elif(s4=="X" and s5=="X" and s6occ==False):
    return("s6")
  elif(s7=="X" and s8=="X" and s9occ == False):
    return("s9")
  #DIAGONAL CHECK
  #Left to right
  elif(s5=="X" and s7=="X" and s3occ==False):
    return("s3")
  elif(s3=="X" and s7=="X" and s5occ==False):
    return("s5")
  elif(s3=="X" and s5=="X" and s7occ == False):
    return("s7")
  elif(s1=="X" and s5=="X" and s9occ == False):
    return("s9")
  elif(s5=="X" and s9=="X" and s1occ == False):
    return("s1")
  elif(s1=="X" and s9=="X" and s5occ==False):
    return("s5")
  elif(botmode==2):
    if(talk==1):
      print("\n*The bot did not find any way for you to win. Since this is medium mode, it will randomly pick a space...")
    test = random.randint(1,9)
    if(test ==1):
      return("s1")
    if(test ==2):
      return("s2")
    if(test ==3):
      return("s1")
    if(test ==4):
      return("s4")
    if(test ==5):
      return("s5")
    if(test ==6):
     return("s6")
    if(test ==7):
      return("s7")
    if(test ==8):
      return("s8")
    if(test ==9):
     return("s9")
  elif(botmode==3):
    if(s1=="O" and s7=="O" and s4occ==False):
      return("s4")
    elif(s2=="O" and s8=="O" and s5occ==False):
      return("s5")
    elif(s3=="O" and s9=="O" and s6occ==False):
      return("s6")
  #First row
    elif(s4=="O" and s7=="O"and s1occ==False):
     return("s1")
    elif(s5=="O" and s8=="O" and s2occ==False):
      return("s2")
    elif(s6=="O" and s9=="O" and s3occ==False):
     return("s3")
  # Last row
    elif(s1=="O" and s4=="O" and s7occ==False):
      return("s7")
    elif(s2=="O" and s5=="O" and s8occ==False):
      return("s8")
    elif(s3=="O" and s6=="O" and s9occ==False):
      return("s9")
  #UP AND DOWN CHECKING
  #first row
    elif(s2=="O" and s3=="O" and s1occ==False):
      return("s1")
    elif(s5=="O" and s6=="O" and s2occ==False):
      return("s4")
    elif(s8=="O" and s9=="O" and s7occ==False):
      return("s7")
    elif(s1=="O" and s3=="O" and s2occ==False):
     return("s2")
    elif(s4=="O" and s6=="O" and s5occ==False):
     return("s5")
    elif(s7=="O" and s9=="O" and s8occ==False):
      return("s8")
  #bottom row
    elif(s1=="O" and s2=="O" and s3occ==False):
      return("s3")
    elif(s4=="O" and s5=="O" and s6occ==False):
      return("s6")
    elif(s7=="O" and s8=="O" and s9occ==False):
      return("s9")
  #DIAGONAL CHECK
  #Left to right
    elif(s5=="O" and s7=="O" and s3occ==False):
     return("s3")
    elif(s3=="O" and s7=="O" and s5occ==False):
      return("s5")
    elif(s3=="O" and s5=="O" and s7occ==False):
      return("s7")
    elif(s1=="O" and s5=="O" and s9occ==False):
     return("s9")
    elif(s5=="O" and s9=="O" and s1occ==False):
     return("s1")
    elif(s1=="O" and s9=="O" and s5occ==False):
      return("s5")
    else:
      if(talk==1):
        print("\n*The bot could not find a way to win. Randomly picking a space...")
      if(s5==5):
        print("\n*The bot found that the middle space is not occupied. It is taking that space...")
        return("s5")
      if(turnnumber<=3 and s5=="X" and botmode==3):
        if(talk==1):
          print("\n *The bot found that you took the middle space. It will pick a corner to have the best chance of winning")
        test = random.randint(1,4)
        if(test==1):
          return("s1")
        if(test==2):
          return("s3")
        if(test==3):
          return("s7")
        if(test==4):
          return("s9")
      
      if(s5=="O"):
      if(s1=="X" and s7=="X"):
        test2= random.randint(1,4)
      elif(s1=="X" and s3=="X"):
        test2 = random.randint(1,4)
      elif(s1=="X" and s9=="X"):
        test2 = random.randint(1,4)
      elif(s7=="X" and s3=="X"):
        test2= random.randint(1,4)
      elif(s7=="X" and s9=="X"):
        test2 = random.randint(1,4)
      elif(s7=="X" and s1=="X"):
        test2 = random.randint(1,4)
      elif(s3=="X" and s7=="X"):
        test2 = random.randint(1,4)
      elif(s3=="X" and s9=="X"):
        test2 = random.randint(1,4)
      elif(s3=="X" and s1=="X"):
        test2 = random.randint(1,4)
      elif(s9=="X" and s7=="X"):
        test2 = random.randint(1,4)
      elif(s9=="X" and s3=="X"):
        test2 = random.randint(1,4)
      elif(s9=="X" and s1=="X"):
        test2 = random.randint(1,4)
      if(test2==1):
        if(talk==1):
          print("\n *You occupy two corners. The bot must pick a inside square to win...")
        return("s4")
      if(test2==2):
        if(talk==1):
          print("\n *You occupy two corners. The bot must pick a inside square to win...")
        return("s8")
      if(test2==3):
        if(talk==1):
          print("\n *You occupy two corners. The bot must pick a inside square to win...")
        return("s6")
      if(test2==4):
        if(talk==1):
          print("\n *You occupy two corners. The bot must pick a inside square to win...")
        return("s2")
      
      
      test = random.randint(1,9)
      if(test ==1):
        return("s1")
      if(test ==2):
        return("s2")
      if(test ==3):
        return("s1")
      if(test ==4):
        return("s4")
      if(test ==5):
        return("s5")
      if(test ==6):
       return("s6")
      if(test ==7):
        return("s7")
      if(test ==8):
        return("s8")
      if(test ==9):
       return("s9")
  
  
  
  
  
  
  
  
def checkwin(s1,s2,s3,s4,s5,s6,s7,s8,s9):
  if(s1=="O" and s2=="O" and s3=="O"):
    return("O")
  elif(s4=="O" and s5=="O" and s6=="O"):
    return("O")
  elif(s7=="O" and s8=="O" and s9=="O"):
    return("O")
  elif(s1=="X" and s2=="X" and s3=="X"):
    return("X")
  elif(s4=="X" and s5=="X" and s6=="X"):
    return("X")
  elif(s7=="X" and s8=="X" and s9=="X"):
    return("X")
    
    
  elif(s1=="O" and s4=="O" and s7=="O"):
    return("O")
  elif(s2=="O" and s5=="O" and s8=="O"):
    return("O")
  elif(s3=="O" and s6=="O" and s9=="O"):
    return("O")
  elif(s1=="X" and s4=="X" and s7=="X"):
    return("X")
  elif(s2=="X" and s5=="X" and s8=="X"):
    return("X")
  elif(s3=="X" and s6=="X" and s9=="X"):
    return("X")
    
  elif(s1=="X" and s5=="X" and s9=="X"):
    return("X")
  elif(s7=="X" and s5=="X" and s3=="X"):
    return("X")
  elif(s1=="O" and s5=="O" and s9=="O"):
    return("O")
  elif(s7=="O" and s5=="O" and s3=="O"):
    return("O")
  else:
    return(False)
  
running =1
player = 1
playagainstbot = 1

space1 = 1
space2 = 2
space3 = 3
space4 = 4
space5 = 5
space6 = 6
space7 = 7
space8 = 8
space9 = 9
space1occ = False
space2occ = False
space3occ = False
space4occ = False
space5occ = False
space6occ = False
space7occ = False
space8occ = False
space9occ = False
turnnumber = 0

while(running==1):
  x = int(input("Would you like to play against a player or a bot. Enter 1 for a player and 2 for a bot"))
  playing = 1
  printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
  if(x==2):
    botmode = int(input("Please pick a difficulty:\n\n1) Easy\n2) Medium\n3) Hard\n\n(Enter the number)"))
    if(botmode==2 or botmode==3):
      talkingmove = int(input("Enter 1 if you would like to see what the bot is thinking. Enter 0 if you dont want to see what the bot is thinking"))
  if(x==2 and botmode==2):
    while(playing==1):
      turnnumber = turnnumber+1
      if(player==2):
        pickspace = 1
        times = 0
        while(pickspace==1):
          times = times +1
          if(space1occ ==True and space2occ==True and space3occ==True and space4occ==True and space5occ==True and space6occ==True and space7occ==True and space8occ==True and space9occ==True):
            print("Its a tie!!!")
            exit()
            playing =0
            running = 0
            continue;

          pickedspace = godefence(space1,space2,space3,space4,space5,space6,space7,space8,space9,talkingmove,botmode,space1occ,space2occ,space3occ,space4occ,space5occ,space6occ,space7occ,space8occ,space9occ,turnnumber)
          print("The bot is now choosing a space... (Try #"+str(times)+")")
          if(times>=9):
            text = random.randint(1,9)
            if(text==1):
              pickedspace="s1"
            if(text==2):
              pickedspace=="s2"
            if(text==3):
              pickedspace="s3"
            if(text==4):
              pickedspace="s4"
            if(text==5):
              pickedspace="s5"
            if(text==6):
              pickedspace="s6"
            if(text==7):
              pickedspace="s7"
            if(text==8):
              pickedspace="s8"
            if(text==9):
              pickedspace="s9"
          if(pickedspace =="s1" and space1occ==False):
            space1 = "O"
            space1occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s2" and space2occ==False):
            space2 = "O"
            space2occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s3" and space3occ==False):
            space3 = "O"
            space3occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s4" and space4occ==False):
            space4 = "O"
            space4occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s5" and space5occ==False):
            space5 = "O"
            space5occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s6" and space6occ==False):
            space6 = "O"
            space6occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s7" and space7occ==False):
            space7 = "O"
            space7occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s8" and space8occ==False):
            space8 = "O"
            space8occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s9" and space9occ==False):
            space9 = "O"
            space9occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "O"):
          print("You lost :( !!!")
          playing =0
          running = 0
          continue;

            
            
            
            
            
      if(player==1):
        space = int(input("(PLAYER 1): Please enter a space coresponding to the board number"))
        if(space==1 and space1occ == False):
          space1 = "X"
          space1occ = True
        elif(space==2 and space2occ == False):
         space2 = "X"
         space2occ = True
        elif(space==3 and space3occ == False):
          space3 = "X"
          space3occ = True
        elif(space==4 and space4occ == False):
          space4 = "X"
          space4occ = True
        elif(space==5 and space5occ == False):
          space5 = "X"
          space5occ = True
        elif(space==6 and space6occ == False):
          space6 = "X"
          space6occ = True
        elif(space==7 and space7occ == False):
          space7 = "X"
          space7occ = True
        elif(space==8 and space8occ == False):
          space8 = "X"
          space8occ = True
        elif(space==9 and space9occ == False):
          space9 = "X"
          space9occ = True
        else:
          print("You chose an invalid or occupied space. Your turn was skipped :( ")
        player = 2
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "X"):
          print("You win!!!")
          playing =0
          running = 0
          continue;
  if(x==2 and botmode==3):
    while(playing==1):
      turnnumber = turnnumber + 1
      if(player==2):
        pickspace = 1
        times = 0
        while(pickspace==1):
          times = times +1
          if(space1occ ==True and space2occ==True and space3occ==True and space4occ==True and space5occ==True and space6occ==True and space7occ==True and space8occ==True and space9occ==True):
            print("Its a tie!!!")
            exit()
            playing =0
            running = 0
            continue;

          pickedspace = godefence(space1,space2,space3,space4,space5,space6,space7,space8,space9,talkingmove,botmode,space1occ,space2occ,space3occ,space4occ,space5occ,space6occ,space7occ,space8occ,space9occ,turnnumber)
          print("The bot is now choosing a space... (Try #"+str(times)+")")
          if(times>=9):
            text = random.randint(1,9)
            if(text==1):
              pickedspace="s1"
            if(text==2):
              pickedspace=="s2"
            if(text==3):
              pickedspace="s3"
            if(text==4):
              pickedspace="s4"
            if(text==5):
              pickedspace="s5"
            if(text==6):
              pickedspace="s6"
            if(text==7):
              pickedspace="s7"
            if(text==8):
              pickedspace="s8"
            if(text==9):
              pickedspace="s9"
          if(pickedspace =="s1" and space1occ==False):
            space1 = "O"
            space1occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s2" and space2occ==False):
            space2 = "O"
            space2occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s3" and space3occ==False):
            space3 = "O"
            space3occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s4" and space4occ==False):
            space4 = "O"
            space4occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s5" and space5occ==False):
            space5 = "O"
            space5occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s6" and space6occ==False):
            space6 = "O"
            space6occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s7" and space7occ==False):
            space7 = "O"
            space7occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s8" and space8occ==False):
            space8 = "O"
            space8occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace =="s9" and space9occ==False):
            space9 = "O"
            space9occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "O"):
          print("You lost :( !!!")
          playing =0
          running = 0
          continue;

            
            
            
            
            
      if(player==1):
        space = int(input("(PLAYER 1): Please enter a space coresponding to the board number"))
        if(space==1 and space1occ == False):
          space1 = "X"
          space1occ = True
        elif(space==2 and space2occ == False):
         space2 = "X"
         space2occ = True
        elif(space==3 and space3occ == False):
          space3 = "X"
          space3occ = True
        elif(space==4 and space4occ == False):
          space4 = "X"
          space4occ = True
        elif(space==5 and space5occ == False):
          space5 = "X"
          space5occ = True
        elif(space==6 and space6occ == False):
          space6 = "X"
          space6occ = True
        elif(space==7 and space7occ == False):
          space7 = "X"
          space7occ = True
        elif(space==8 and space8occ == False):
          space8 = "X"
          space8occ = True
        elif(space==9 and space9occ == False):
          space9 = "X"
          space9occ = True
        else:
          print("You chose an invalid or occupied space. Your turn was skipped :( ")
        player = 2
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "X"):
          print("You win!!!")
          playing =0
          running = 0
          continue;
  if(x==2 and botmode==1):
    while(playing==1):
      if(player==2):
        pickspace = 1
        times = 0
        while(pickspace==1):
          times = times +1
          if(space1occ ==True and space2occ==True and space3occ==True and space4occ==True and space5occ==True and space6occ==True and space7occ==True and space8occ==True and space9occ==True):
            print("Its a tie!!!")
            exit()
            playing =0
            running = 0
            continue;
          pickedspace = random.randint(1,9)
          print("The bot is now choosing a space... (Try #"+str(times)+")")
          if(pickedspace ==1 and space1occ==False):
            space1 = "O"
            space1occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==2 and space2occ==False):
            space2 = "O"
            space2occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==3 and space3occ==False):
            space3 = "O"
            space3occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==4 and space4occ==False):
            space4 = "O"
            space4occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==5 and space5occ==False):
            space5 = "O"
            space5occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==6 and space6occ==False):
            space6 = "O"
            space6occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==7 and space7occ==False):
            space7 = "O"
            space7occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==8 and space8occ==False):
            space8 = "O"
            space8occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)

          if(pickedspace ==9 and space9occ==False):
            space9 = "O"
            space9occ = True
            pickspace=0
            player=1
            printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "O"):
          print("You lost :( !!!")
          playing =0
          running = 0
          continue;

            
            
            
            
            
      if(player==1):
        space = int(input("(PLAYER 1): Please enter a space coresponding to the board number"))
        if(space==1 and space1occ == False):
          space1 = "X"
          space1occ = True
        elif(space==2 and space2occ == False):
         space2 = "X"
         space2occ = True
        elif(space==3 and space3occ == False):
          space3 = "X"
          space3occ = True
        elif(space==4 and space4occ == False):
          space4 = "X"
          space4occ = True
        elif(space==5 and space5occ == False):
          space5 = "X"
          space5occ = True
        elif(space==6 and space6occ == False):
          space6 = "X"
          space6occ = True
        elif(space==7 and space7occ == False):
          space7 = "X"
          space7occ = True
        elif(space==8 and space8occ == False):
          space8 = "X"
          space8occ = True
        elif(space==9 and space9occ == False):
          space9 = "X"
          space9occ = True
        else:
          print("You chose an invalid or occupied space. Your turn was skipped :( ")
        player = 2
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "X"):
          print("You win!!!")
          playing =0
          running = 0
          continue;
          
          
          
          
          
          
          
          
          
          
          
  if(x==1):
    while(playing==1):
      if(space1occ ==True and space2occ==True and space3occ==True and space4occ==True and space5occ==True and space6occ==True and space7occ==True and space8occ==True and space9occ==True):
        print("Its a tie!!!")
        playing =0
        running = 0
        continue;
      if(player==1):
        space = int(input("(PLAYER 1): Please enter a space coresponding to the board number"))
        if(space==1 and space1occ == False):
          space1 = "X"
          space1occ = True
        elif(space==2 and space2occ == False):
         space2 = "X"
         space2occ = True
        elif(space==3 and space3occ == False):
          space3 = "X"
          space3occ = True
        elif(space==4 and space4occ == False):
          space4 = "X"
          space4occ = True
        elif(space==5 and space5occ == False):
          space5 = "X"
          space5occ = True
        elif(space==6 and space6occ == False):
          space6 = "X"
          space6occ = True
        elif(space==7 and space7occ == False):
          space7 = "X"
          space7occ = True
        elif(space==8 and space8occ == False):
          space8 = "X"
          space8occ = True
        elif(space==9 and space9occ == False):
          space9 = "X"
          space9occ = True
        else:
          print("You chose an invalid or occupied space. Your turn was skipped :( ")
        player = 2
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "X"):
          print("Player 1 wins!!!")
          playing =0
          running = 0
          continue;
      if(player==2):
        space = int(input("(PLAYER 2): Please enter a space coresponding to the board number"))
        if(space==1 and space1occ == False):
          space1 = "O"
          space1occ = True
        elif(space==2 and space2occ == False):
         space2 = "O"
         space2occ = True
        elif(space==3 and space3occ == False):
          space3 = "O"
          space3occ = True
        elif(space==4 and space4occ == False):
          space4 = "O"
          space4occ = True
        elif(space==5 and space5occ == False):
          space5 = "O"
          space5occ = True
        elif(space==6 and space6occ == False):
          space6 = "O"
          space6occ = True
        elif(space==7 and space7occ == False):
          space7 = "O"
          space7occ = True
        elif(space==8 and space8occ == False):
          space8 = "O"
          space8occ = True
        elif(space==9 and space9occ == False):
          space9 = "O"
          space9occ = True
        else:
          print("You chose an invalid or occupied space. Your turn was skipped :( ")
        player = 1
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printboard(space1,space2,space3,space4,space5,space6,space7,space8,space9)
        if (checkwin(space1,space2,space3,space4,space5,space6,space7,space8,space9)== "X"):
          print("Player 1 wins!!!")
          playing =0
          running = 0
          continue;
      
        
        
  
