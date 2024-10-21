#this will maintain teh multiplayer functions and the draw windo function, aswell as anything else that we need 
import pygame 
from main import *
from rotations import * 


    







def multiplayer_move(masterRows1, masterRows2, runProgram, score1, score2, level, flipping1, flipping2, WIN):#flipping will be a 1 or a -1, and it will determine if the map flips everytime or not for levels 2, where the map flips
    '''
    manages the multiplayer game mode 

    parameters 

    masterRows1 - list of all of player 1's blocks
    masterRows2 - list of all of plater 2's blocks 
    score1 - player one's points, integer
    score2 - player two's points, integer 
    level - integer 1,2 or 3
    flipping1 - the direction player one is traveling 
    flipping2 - the direction player two is traveling 
    WIN - pygame window
    
    
    '''
    
    #wasd will be player one, and arrows will be player 2 
    
    playingField1, playingField2 = (pygame.Rect((0, 0), (300, WIN.get_height()))), (pygame.Rect((0, 0), (300, WIN.get_height()))     )
    playingField1.x, playingField2.x = 50, (WIN.get_width() - 350)
    
    rowNumber = 0
    
    gameOver = False
    player1_active, player2_active = True, True 

    timeTracker = 0
    movement = True
    if level == 1:
        speed = 3000
    elif level == 2:
        speed = 900
    elif level == 3:
        speed = 800
    while(runProgram):


        clock = pygame.time.Clock()
        timeTracker += 1 

        if timeTracker>=speed:
            timeTracker = 0
            piece1 = making_piece( flipping1, level, playingField1)
            piece2 = making_piece( flipping2, level, playingField2)
                     

            while movement:#more efficient if we use rows instead of checking every item
                clock = pygame.time.Clock()
                keys_pressed = pygame.key.get_pressed( )
                timeTracker += 1
                if timeTracker>=speed:
                    timeTracker = 0
                    score1 = add_row(masterRows1, score1, flipping1, level, playingField1)
                    score2 = add_row(masterRows2, score2, flipping2, level, playingField2) 
                    
                    pause = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.display.quit()
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                rotation(piece2, masterRows2, playingField2)
                                
                            if event.key == pygame.K_w:
                                rotation(piece1, masterRows1, playingField1)
                                
                            if event.key == pygame.K_ESCAPE:
                                pygame.display.quit()
                                pygame.quit()
                                movement = False
                                runProgram = False
                                break

                            if event.key == pygame.K_SPACE:
                                pause = not pause


                    while pause:
                        pause = pause_(WIN) 






                    score1 = player1_handle_movements(keys_pressed, piece1, playingField1, masterRows1, True, flipping1, score1, player1_active)
                    score2 = player2_handle_movements(keys_pressed, piece2, playingField2, masterRows2, True, flipping2, score2, player2_active)
                    if player1_active:
                        can_go_down = True
                        if flipping1 == 1:
                            for item in piece1:
                                
                                if item[0].y + item[0].height >= WIN.get_height():    
                                    can_go_down = False      

                                for row in masterRows1:
                                    for block in range(len(row)):
                                        if item[0].y + item[0].height == (row[block])[0].y:
                                            if item[0].x == (row[block])[0].x:
                                                can_go_down = False
                        else:
                            for item in piece1:
                                
                                if item[0].y <= 0:    
                                    can_go_down = False


                                for row in masterRows1:
                                    for block in range(len(row)):
                                        if item[0].y - item[0].height == (row[block])[0].y:
                                            if item[0].x == (row[block])[0].x:
                                                can_go_down = False


                        if can_go_down:

                            for item in piece1:
                                item[0].y+= item[0].height*flipping1
                            

                        else:
                            
                            for block in piece1:
                                masterRows1[int((block[0].y + block[0].height)/10 - 1)].append(block)
                                if block[0].y == 0:
                                        player1_active = False
                            if player1_active:
                                if level == 1 or level == 2:
                                    piece1 = making_piece( flipping1, level, playingField1)
                                else:
                                    piece1 = making_piece( flipping1*-1, level, playingField1)
                    if not player1_active: 
                        piece1 = [] 
                        masterRows1 = []
                        
                        
                    #Split between person one and person 2 
                    if player2_active:
                        can_go_down = True
                        if flipping1 == 1:
                            for item in piece2:
                                
                                if item[0].y + item[0].height >= WIN.get_height():    
                                    can_go_down = False      
                    
                                for row in masterRows2:
                                    for block in range(len(row)):
                                        if item[0].y + item[0].height == (row[block])[0].y:
                                            if item[0].x == (row[block])[0].x:
                                                can_go_down = False
                        else:
                            for item in piece2:
                                
                                if item[0].y <= 0:    
                                    can_go_down = False
                    
                    
                                for row in masterRows2:
                                    for block in range(len(row)):
                                        if item[0].y - item[0].height == (row[block])[0].y:
                                            if item[0].x == (row[block])[0].x:
                                                can_go_down = False
                    
                    
                        if can_go_down:
                    
                            for item in piece2:
                                item[0].y+= item[0].height*flipping2
                    
                        else:
                            for block in piece2:
                                masterRows2[int((block[0].y + block[0].height)/10 - 1)].append(block)
                                if block[0].y == 0:
                                    player2_active = False
                            if player2_active:
                                if level == 1 or level == 2:
                                    piece2 = making_piece( flipping2, level, playingField2)
                                else:
                                    piece2 = making_piece( -1*flipping2, level, -playingField2)
                                        
                    if not player2_active:
                        piece2 = []
                        masterRows2 = []
                      
                    if not player1_active and not player2_active:
                        multiplayer_end(WIN, score1, score2)
                        runProgram = False
                        break 
                    
                    while timeTracker != 5:
                        timeTracker+=1
                        clock.tick(FPS)      


                    multiplayerDrawWindow(playingField1, playingField2, piece1, piece2, masterRows1, masterRows2, score1, score2, level, flipping1, flipping2, player1_active,player2_active)
def player1_handle_movements(keys_pressed, player, playingField, masterRows, canGoDown, flipping, score, player1_active):
    '''
    handles the player 1 controls 

    keys_pressed is a map of all the keys and weather or not they are being pressed
    player is the piece the user controls 
    playingField is the game board 
    masterRows is a list of all the blocks on the board
    canGoDows is a boolean that represents if the piece is blocked below or not 
    flipping is the pieces direction of traveling expressed as -1 or 1
    score is the players points 
    player1_active is a boolean of weather or not the game is running 
    
    
    '''
    can_move = True
    playerRow = None

    if keys_pressed[pygame.K_a]:
        can_move = True
        for piece in player:
            if piece[0].x == playingField.x:
                can_move = False
            else:
                for row in masterRows:
                    for block in row:
                        if piece[0].x - piece[0].width == block[0].x and (piece[0].y == block[0].y):
                            can_move = False 
        if can_move:
            for piece in player:
                piece[0].x -= WIN.get_width()/90
        else:
            pass #will play noise 

    if keys_pressed[pygame.K_d]:
        can_move = True
        for piece in player:
            if piece[0].x + piece[0].width == playingField.x + playingField.width:
                can_move = False
            else:
                for row in masterRows:
                    for block in row:
                        if piece[0].x  == block[0].x - block[0].width and (piece[0].y == block[0].y): #or piece.rect.y == block.rect.y + block.rect.height):#error here only messses up when going right 
                            can_move = False 
            # will play a sound 
        if can_move:
            for piece in player:
                piece[0].x +=WIN.get_width()/90
        else:
            pass
    if keys_pressed[pygame.K_s]:
        if flipping ==1:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == WIN.get_height() - piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y + piece[0].height)/10 - 1)
                        for block in masterRows[playerRow +1]:
                            if block[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        block[0].y += block[0].width
        if flipping ==1:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == WIN.get_height() - piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y + piece[0].height)/10 - 1)
                        for block in masterRows[playerRow +1]:
                            if block[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        block[0].y += block[0].width
                    if player1_active:
                        score += 1
        else:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == 0 +piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y)/10)
                        for block in masterRows[playerRow -1]:
                            if (block)[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        (block)[0].y -= (block)[0].width 
                    if player1_active:
                        score += 1
    return score
    
def player2_handle_movements(keys_pressed, player, playingField, masterRows, canGoDown, flipping, score, player2_active):
    ''' will facilitate the movement left and right, aswell as towards the ends of the map
    
    parameters
    ----------
    
    keys_pressed - a map that has every key on the keyboard, attached with 'True' if the key is being pressed, or 'False' if it is not pressed
    
    player -list of nested lists that contain rectangles and images
    
    playingField - a rectangle that is the area in which the game is played 
    
    masterRows - list
    
    canGoDown - True or False 
    
    flipping - integer that tells the program if the block is traveling up or down 
              1 or -1
              
              '''
    
    
    
    can_move = True
    playerRow = ''



    if keys_pressed[pygame.K_LEFT]:
        can_move = True
        for piece in player:
            if piece[0].x == playingField.x:
                can_move = False
            else:
                for row in masterRows:
                    for block in row:
                        if piece[0].x - piece[0].width == block[0].x and (piece[0].y == block[0].y):
                            can_move = False 
        if can_move:
            for piece in player:
                piece[0].x -=10
        else:
            pass #will play noise 

    if keys_pressed[pygame.K_RIGHT]:
        can_move = True
        for piece in player:
            if piece[0].x + piece[0].width == playingField.x + playingField.width:
                can_move = False
            else:
                for row in masterRows:
                    for block in row:
                        if piece[0].x  == block[0].x - block[0].width and (piece[0].y == block[0].y): #or piece.rect.y == block.rect.y + block.rect.height):#error here only messses up when going right 
                            can_move = False 
            # will play a sound 
        if can_move:
            for piece in player:
                piece[0].x +=10
        else:
            pass
    if keys_pressed[pygame.K_DOWN]:
        if flipping ==1:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == WIN.get_height() - piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y + piece[0].height)/10 - 1)
                        for block in masterRows[playerRow +1]:
                            if block[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        block[0].y += block[0].width
        if flipping ==1:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == WIN.get_height() - piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y + piece[0].height)/10 - 1)
                        for block in masterRows[playerRow +1]:
                            if block[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        block[0].y += block[0].width
                    if player2_active:
                        score += 1
        else:
            if canGoDown:
                can_move = True
                for piece in player:
                    if piece[0].y == 0 +piece[0].height:
                        can_move = False
                    else:
                        playerRow = int((piece[0].y)/10)
                        for block in masterRows[playerRow -1]:
                            if (block)[0].x == piece[0].x:
                                can_move = False
                if can_move:
                    for block in player:
                        (block)[0].y -= (block)[0].width 
                    if player2_active:
                        score += 1
    return score
                        
def multiplayerDrawWindow(playingField1, playingField2, piece1, piece2,  masterRows1, masterRows2, score1, score2, level, flipping1, flipping2, player1_active, player2_active):
    ''' this functions displays teh screen
    playingField1 and playingField2 aare both pygaem rectangles
    peice one and 2 are lists of the blocks that make up the objec5t the player is moving
    masterRows1 and masterRows2 are lists of all teh blocks in teh game 
    score1 and score2 are integers 
    level is an integer 
    flipping1 and flipping2 are both -1 or 1 and represent which way the block is moving'''
    WIN.fill(BLACK)
    leaders = openLeaderboard(level)
    leaderNames = leaders[0]
    leaderScores = leaders[1]
    displayingLeaders = []
    
 




    scoreText1 = REGULAR_FONT.render("P1: " + str(score1), 1, WHITE) 
    score1 = MEGA_FONT.render("SCORE:"+str(score1), 1, WHITE) 
    scoreText2 = REGULAR_FONT.render("P2: " + str(score2), 1, WHITE)
    score2 = MEGA_FONT.render("SCORE:" +str(score2), 1, WHITE) 
  
    you_died1 = MEGA_FONT.render('YOU DIED', 1, WHITE)
    you_died2 = MEGA_FONT.render('YOU DIED', 1, WHITE)

    space_to_pause = MIDDLE_FONT.render('Press space to pause', 1, WHITE)
    escape_to_leave = MIDDLE_FONT.render('Press escape to exit pygame', 1, WHITE)
    if player2_active:
        pygame.draw.rect(WIN,WHITE, playingField2)
    else:
        pygame.draw.rect(WIN,BLACK, playingField2)
        WIN.blit(you_died1,(playingField2.x +playingField2.width//2- .5*you_died1.get_width(), 80))
        WIN.blit(score2,(playingField2.x +playingField2.width//2- .5*score2.get_width(), 130))


    if player1_active:
        pygame.draw.rect(WIN, WHITE, playingField1)
    else:
        pygame.draw.rect(WIN,BLACK, playingField1)
        WIN.blit(you_died2,(playingField1.x +playingField2.width//2- .5*you_died2.get_width(), 80))
        WIN.blit(score1,(playingField1.x +playingField1.width//2- .5*score1.get_width(), 130))


    
    
    if flipping1 == 1:
      for block in piece1:
      
        rectangle = pygame.Rect(((block)[0].x, (block)[0].y), (10, WIN.get_height() - (piece1[0])[0].y))
        pygame.draw.rect(WIN, (0,128,128), rectangle)
        
        WIN.blit(block[1], (block[0].x, block[0].y))
   
        
    else:
      for block in reversed(piece1):
        rectangle = pygame.Rect(((block)[0].x, 0), (10, (block)[0].y))
          
        pygame.draw.rect(WIN, (0,128,128), rectangle)
        
        WIN.blit(block[1], (block[0].x, block[0].y))  
        
  
    if flipping2 == 1:
      for block in piece2:
      
        rectangle = pygame.Rect(((block)[0].x, (block)[0].y), (10, WIN.get_height() - (piece2[0])[0].y))
        pygame.draw.rect(WIN, (0,128,128), rectangle)
        
        WIN.blit(block[1], (block[0].x, block[0].y))
    
        
    else:
      for block in reversed(piece2):
        rectangle = pygame.Rect(((block)[0].x, 0), (10, (block)[0].y))
          
        pygame.draw.rect(WIN, (0,128,128), rectangle)
        
        WIN.blit(block[1], (block[0].x, block[0].y))
        
        
  
  
       
    
    for row in masterRows1:
        for block in row:
            WIN.blit(block[1], (block[0].x, block[0].y))

    for row in masterRows2:
        for block in row:
            WIN.blit(block[1], (block[0].x, block[0].y))
  
    
    WIN.blit(scoreText1,(WIN.get_width()//2 - .5*scoreText1.get_width(), 50))
    WIN.blit(scoreText2,(WIN.get_width()//2 - .5*scoreText2.get_width(), 80))
    
  
    WIN.blit(space_to_pause, (WIN.get_width()//2 - space_to_pause.get_width()*.5, WIN.get_height() - 30))
    WIN.blit(escape_to_leave, (WIN.get_width()//2 - escape_to_leave.get_width()*.5, WIN.get_height() - 50))
     
    leaderboard = REGULAR_FONT.render("LEADERBOARD", 1, YELLOW)
    WIN.blit(leaderboard, (WIN.get_width()//2 - .5*leaderboard.get_width(), 20))
    
  
  
  
    #grid:
    grid1 = []
    grid2 = []
    if player1_active:
        grid1 = makingGridlines(playingField1)
    if player2_active:
        grid2 = makingGridlines(playingField2)

    for line in grid1+grid2:
      pygame.draw.rect(WIN, BLACK, line)
    pygame.display.update()
  
  




def multiplayer_end(WIN, score1, score2):
    '''
    end screen of multiplayer

    parameters 
    ----------
    WIN - the pygame window 
    score1 - player one's score
    score2 - player two's score 
    
    
    '''
    
    temp_font = pygame.font.SysFont('open sans', 70)
    WIN.fill(BLACK)
    winner = MEGA_FONT.render("Tie Game", 1, WHITE)  
    if score1 > score2:
        winner =MEGA_FONT.render("Player One Wins by " + str(score1 - score2) +" Points", 1, WHITE)  
    elif score2 > score1: 
        winner =     MEGA_FONT.render("Player Two Wins by " + str(score2 - score1) +" Points", 1, WHITE) 

    WIN.blit(winner, (WIN.get_width()//2 - winner.get_width()//2, WIN.get_height()//3))
    mainmenu = temp_font.render("MAIN MENU", 1, RED)
    mainmenu_rect = mainmenu.get_rect()
    mainmenu_rect.x, mainmenu_rect.y =  computer_rect,y = WIN.get_width()//2  - mainmenu.get_width()//2, 300
    WIN.blit(mainmenu, (WIN.get_width()//2  - mainmenu.get_width()//2, 300))

    runProgram = True
    while runProgram:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    movement = False
                    runProgram = False
                    break
                if event.key == pygame.K_SPACE:
                    pause = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(3423432)
        
                if mainmenu_rect.collidepoint(event.pos):
                    one = []
                    for i in range(50):
                        one.append([])                
                    from main_menu_slides import main_menu
                    main_menu(WIN, one )        

        pygame.display.update()



                 


