#importing our libraries 

import pygame
import time
import random
import os
import sys
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.font.get_fonts()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


#importing modules
from rotations import *
from main_menu_slides import *
from multiplayer import * 
from campaign import *

#font sizes for text display
blockWidth = 10
MEGA_FONT = pygame.font.SysFont('open sans', 80)
BIG_FONT = pygame.font.SysFont('open sans', 30)
REGULAR_FONT = pygame.font.SysFont('open sans', 20)
MIDDLE_FONT = pygame.font.SysFont('open sans', 14)
SMALL_FONT = pygame.font.SysFont('open sans', 10)




#The list with all of the game's blocks 
masterRows = []
for x in range(50):
  masterRows.append([])
  
#monitor size must be before WIN is created and if its before, then it will retrive the monitor dimensions
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode([WIDTH, HEIGHT] )
pygame.display.set_caption('FlipStack')

#colors 
BLACK = (15,15,15)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
YELLOW = (255, 255, 0)

colors = [RED, GREEN,BLUE, ORANGE]


FPS = 100

instructions1 = pygame.transform.scale(pygame.image.load(os.path.join('moveLeftAndRightInstructions.png')), (WIN.get_width(), WIN.get_height()))
instructions2 = pygame.transform.scale(pygame.image.load(os.path.join('moveDownInstructions.png')), (WIN.get_width(), WIN.get_height()))
instructions3 = pygame.transform.scale(pygame.image.load(os.path.join('screenshot.png')), (WIN.get_width(), WIN.get_height()))
instructions4 = pygame.transform.scale(pygame.image.load(os.path.join('fbla_pic_2_2.0.jpg')), (WIN.get_width(), WIN.get_height()))
instructions5 = pygame.transform.scale(pygame.image.load(os.path.join('rowDeleting.png')), (WIN.get_width(),  WIN.get_height()))
blocks = [(pygame.transform.scale(pygame.image.load(os.path.join('block_blue.png')), (blockWidth, blockWidth))),( pygame.transform.scale(pygame.image.load(os.path.join('block_green.png')), (blockWidth, blockWidth))), (pygame.transform.scale(pygame.image.load(os.path.join('block_orange.png')), (blockWidth, blockWidth))),( pygame.transform.scale(pygame.image.load(os.path.join('block_purple.png')), (blockWidth, blockWidth))), (pygame.transform.scale(pygame.image.load(os.path.join('block_red.png')), (blockWidth, blockWidth)))]






def makingGridlines(playingField):
  '''
  created the grid sequence of the game board 

  Parameters
  ------------
  playingField - pygame rectangle that serves as the user's playing area 

  '''
#grids:
  gridLines = []
  width_range = int(playingField.width//10+1)
  for x in range(0, width_range):#making vertical lines 
    line = pygame.Rect((0, 0), (1,WIN.get_height()))
    line.x = playingField.x + x*WIN.get_width()//90
    gridLines.append(line)
  for x in range(1, int(playingField.height // 10 +1)):#making horizontal lines 
    line = pygame.Rect((playingField.x, 0), (playingField.width,1))
    line.y = playingField.y + x*WIN.get_height()//50
    gridLines.append(line)
  return gridLines



def making_piece( flipping, level, playingField):
  '''
  this randomly generates a list of rectangles that will be used as the player's piece 

  parameters 
  -------------

  flipping = 1 or -1, describes if the piece is starting on the bottom or the top

  level = 1, 2, or 3  allows us to know which way to move the piece

  playingField = pygame rectangle used as the player's playing area
  
  '''
  
  piece = []
  option = random.randint(0, 4)
  block =  random.choice(blocks)

  if option == 0:#making the line piece
    #[1]
    #[2]
    #[3]
    part1 = pygame.Rect((playingField.x+playingField.width//2, 0), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth*2), (WIN.get_width()//90, WIN.get_height()//50))
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
  
  elif option == 1:#making the single block piece 
    #[1]
    pass
    part1=  pygame.Rect((playingField.x+playingField.width//2, 0), (blockWidth, blockWidth))
    piece = [[part1, block]]
  
  elif option == 5:#making the Z piece 
    #  [1] 
    #[3 2]   
    #[4]
    #[5]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part4 =pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part5 =pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part1.x = playingField.x+playingField.width//2
    part1.y = 0
    part3.x = playingField.x+playingField.width//2 -part2.width
    part3.y = part3.height
    part2.x = playingField.x+playingField.width//2
    part2.y = part2.height
    part4.x = playingField.x+playingField.width//2 -part4.width
    part4.y = part4.height*2
    part5.x = part5.x = playingField.x+playingField.width//2 -part5.width
    part5.y = part5.height*3
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
    piece.append([part4, block])
    piece.append([part5, block])
  

  elif option == 2: #making the S piece 
    #[1]
    #[2 3]
    #  [4]
    #  [5]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part4 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part5 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part1.x = playingField.x+playingField.width//2 -part1.width
    part1.y = 0
    part2.x = playingField.x+playingField.width//2 -part2.width
    part2.y = part2.height
    part3.x = playingField.x+playingField.width//2
    part3.y = part3.height
    part4.x = playingField.x+playingField.width//2
    part4.y = part4.height*2
    part5.x = playingField.x+playingField.width//2
    part5.y = part5.height*3
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
    piece.append([part4, block])
    piece.append([part5, block])
  

  elif option ==4:#Making small L
    #[1]
    #[2 3]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part1.x = playingField.x+playingField.width//2 -part1.width
    part1.y = 0
    part2.x = playingField.x+playingField.width//2 -part2.width
    part2.y = part2.height
    part3.x = playingField.x+playingField.width//2
    part3.y = part3.height
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
   
  elif option == 3:# making +  piece
  #  [1]
  #[2 3 4]
  #  [5]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part4 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part5 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part1.x = playingField.x+playingField.width//2
    part1.y = 0
    part2.x = playingField.x+playingField.width//2 -part2.width
    part2.y = part2.height
    part3.x = playingField.x+playingField.width//2
    part3.y = part3.height
    part4.x = playingField.x+playingField.width//2+part4.width
    part4.y = part4.height
    part5.x = playingField.x+playingField.width//2
    part5.y = part5.height*2
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
    piece.append([part4, block])
    piece.append([part5, block])

  elif option == 6:#making big L piece 
  #[1]
  #[2]
  #[3 4 5]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part4 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part5 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))

    part1.x = playingField.x+playingField.width//2 -part1.width
    part1.y = 0
    part2.x = playingField.x+playingField.width//2 -part2.width
    part2.y = part2.height
    part3.x = playingField.x+playingField.width//2 -part3.width
    part3.y = part3.height*2
    part4.x = playingField.x+playingField.width//2
    part4.y = part4.height*2
    part5.x = playingField.x+playingField.width//2+part4.width
    part5.y = part4.height*2
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
    piece.append([part4, block])
    piece.append([part5, block])
 


  elif option == 7:#making thick rectangle piece
  #[1,2]
  #[3,4]
  #[5,6]
    part1 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part2 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part3 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part4 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part5 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part6 = pygame.Rect((playingField.x+playingField.width//2, blockWidth), (WIN.get_width()//90, WIN.get_height()//50))
    part1.x = playingField.x+playingField.width//2 -part1.width
    part1.y = 0
    part2.x = playingField.x+playingField.width//2
    part2.y = 0
    part3.x = playingField.x+playingField.width//2 -part3.width
    part3.y = part3.height
    part4.x = playingField.x+playingField.width//2
    part4.y = part4.height
    part5.x = playingField.x+playingField.width//2 -part5.width
    part5.y = part5.height*2
    part6.x = playingField.x+playingField.width//2
    part6.y = part6.height*2
    piece.append([part1, block])
    piece.append([part2, block])
    piece.append([part3, block])
    piece.append([part4, block])
    piece.append([part5, block])
    piece.append([part6, block])
  

  if level == 3:#sets teh block to the middle since thats where hard mode starts
    for block in piece:
      block[0].y += WIN.get_height()//2
 
    
      
    
    
  elif flipping == -1:#the piece will be moving up, so it must start at the bottom 
    for block in piece:
      block[0].y += WIN.get_height() - blockWidth*3
  
    
  return piece 



  
  
def openLeaderboard(level):
  '''
  opens a txt file and outputs the data in an array

  parameters
  ---------
  level = 1,2, or 3 used to decide which file to open 
  
  '''

  leaders = [] #gets outputted
  leaderNames = [] #we use two lists instead of a map in case a player gets on teh leaderboard twice
  leaderScores = []
  file = ''
  if level == 1:
    file = 'leaderBoard.txt'
  elif level == 2:
    file = 'level_2_leaderboard.txt'
  else: 
    file = 'level_3_leaderboard.txt'
  leaderBoardFile = open(file,'r+')#uploading the file
  for myLine in leaderBoardFile:#formatting
      if(bool(myLine.rstrip())):
          leader = myLine.split(':')
          leaderNames.append(leader[0])
          leaderScores.append(leader[1].rstrip())
  leaders.append(leaderNames)
  leaders.append(leaderScores)
          
  return leaders
    
def drawWindow(playingField, piece,  masterRows, score, level, flipping, campaign, rowsDeleted, powers, power_button, selected):
  '''
  controls updating the window display 

  parameters 
  ----------
  playing field - a pygame rectangle used as the players playing area
  piece - a list of pygame rectangles that make up the object the user controls 
  masterRows - list containing all the pieces that stopped moving and are set on the board
  score - integer that represents the amount of points we contain 
  level - inrteger 1, 2, or 3
  flipping - 1 or -1. represents the direction teh block traveles
  campaign - tells us if our game mode is infinite or campaign 
  rowsDeleted - tracks the amount of rows deleted for campaign mode
  powers - integer that describes how many powers the user has left
  power_button - the icon to activate power ups
  selected- weather or not the power up is activated

  
  '''
  playingField = pygame.Rect((0, 0), (WIN.get_width()//3, WIN.get_height()))#this is the game screen being resized
  playingField.x = WIN.get_width()//2 - .5*playingField.width 
  playingFieldDisplay = pygame.transform.scale(pygame.image.load(os.path.join('FBLA_logo.jpg')), (WIN.get_width()//3, WIN.get_height()))
  instruction = None 

  if selected: #making instructions for power ups 
    instruction = REGULAR_FONT.render("Click A Tile To Delete It", 1, WHITE)
  else:
    instruction = REGULAR_FONT.render("Click to Activate Power ->", 1, WHITE)


  powerText = None
  if bool(powers):#if the player has deletion left, the image will be colored, otherwise it will be grey
    display_power = pygame.transform.scale(pygame.image.load(os.path.join('got_powers.png')), (power_button.width, power_button.height))
    powerText = REGULAR_FONT.render("You have " + str(powers)+ " deletions left", 1, WHITE)
  else:
    display_power = pygame.transform.scale(pygame.image.load(os.path.join('no_more_power.png')), (power_button.width, power_button.height))
    powerText = REGULAR_FONT.render("Out of powers", 1, WHITE)



  WIN.fill(BLACK)
  leaders = openLeaderboard(level)
  leaderNames = leaders[0]
  leaderScores = leaders[1]
  displayingLeaders = []

  WIN.blit(display_power, (power_button.x, power_button.y))#displaying the images 
  WIN.blit(powerText, (WIN.get_width()//7 - powerText.get_width()*.5, WIN.get_height()* (7/8)))
  WIN.blit(instruction, (WIN.get_width()//7 - instruction.get_width()*.5, WIN.get_height()* (15/16)))

  texts = game_instructions(level)
  for text in range(len(texts)):#texts is a list of rendered text that we need to display
    WIN.blit(texts[text], (WIN.get_width()*(5/6) - texts[text].get_width()*.5, 100+text*20))

  for x in range(10):#displaying the top 10 leaderboard 
    dots = 0
    
    if len(leaderNames[x].strip()) + len(leaderScores[x].strip()) < 20:
      dots += 20 - (len(leaderNames[x].strip()) + len(leaderScores[x].strip()))

    displayText = REGULAR_FONT.render(leaderNames[x].strip() + '.'*dots + leaderScores[x].strip(), 1, YELLOW)
    displayingLeaders.append(displayText)




  scoreText = REGULAR_FONT.render("Score: " + str(score), 1, WHITE)
  rowsDeleted_text = REGULAR_FONT.render("Rows Deleted: " + str(rowsDeleted), 1, WHITE)
  
  space_to_pause = REGULAR_FONT.render('Press space to pause', 1, WHITE)
  escape_to_leave = REGULAR_FONT.render('Press escape to exit pygame', 1, WHITE)
  WIN.blit(playingFieldDisplay, (playingField.x, playingField.y))
 
  if flipping == 1:#displays the tiles differently depending on the direction its traveling 
    for block in piece:
    
      rectangle = pygame.Rect(((block)[0].x, (block)[0].y), (10, WIN.get_height() - (piece[0])[0].y))
      pygame.draw.rect(WIN, (0,128,128), rectangle)
       
      WIN.blit(block[1], (block[0].x, block[0].y))    
  else:
    for block in reversed(piece):
      rectangle = pygame.Rect(((block)[0].x, 0), (10, (block)[0].y))
        
      pygame.draw.rect(WIN, (0,128,128), rectangle)
      
      WIN.blit(block[1], (block[0].x, block[0].y))
      

  for row in masterRows:#displaying all the tiles that aren't activiely being moved
    for shape in row:
      WIN.blit(shape[1], (shape[0].x, shape[0].y))
      

  #displaying all of the text 
  WIN.blit(scoreText,(WIN.get_width()//6 - .5*scoreText.get_width(), WIN.get_height()//10))
  WIN.blit(rowsDeleted_text,(WIN.get_width()//6 - .5*rowsDeleted_text.get_width(), WIN.get_height()//(50//7)))
  
  WIN.blit(space_to_pause, (WIN.get_width()*(5/6) - space_to_pause.get_width()*.5, WIN.get_height() - 50))
  WIN.blit(escape_to_leave, (WIN.get_width()*(5/6) - escape_to_leave.get_width()*.5, WIN.get_height() - 20))
  
  leaderY = 160 
  
  #infinite displays leaderboard 
  if not bool(campaign):
    leaderboard = BIG_FONT.render("LEADERBOARD", 1, YELLOW)#the title of the section 
    WIN.blit(leaderboard, ((WIN.get_width() * (1/6) - .5*leaderboard.get_width(), WIN.get_height()//5)))#displays the title 
    
    for leader in displayingLeaders:#accessing the array 
      WIN.blit(leader,(WIN.get_width() * (1/6) - .5*leader.get_width(), leaderY)) #displaying each leader
      leaderY += 20
    
  else:#campaign displays the chalenges 
    
    CHALLENGES = BIG_FONT.render("CHALLENGES", 1, YELLOW)#making the title of the section 
    WIN.blit(CHALLENGES, ((WIN.get_width() * (1/6) - .5*CHALLENGES.get_width(), 100)))#displaying the title 
    #below we get the challenges for that section 
    challenges = [['Get 5000 Points', 'Delete 35 Rows', 'Get 8000 Points'], ['Get 8000 points', 'Delete 50 Rows', 'Get 10000 points'], ['Get 10000 points', 'Delete 70 Rows', "Get 15000 Points"]]
      
    for leader in challenges[level-1]:#displaying the challanges for that level 
      leader = REGULAR_FONT.render(leader.strip(), 1, YELLOW)
      WIN.blit(leader,(WIN.get_width() * (1/6) - .5*leader.get_width(), leaderY))
      leaderY += 20    
      
      
      


  #grid:displaying the grid 
  for line in makingGridlines(playingField):
    pygame.draw.rect(WIN, BLACK, line)
  pygame.display.update()








def add_row(masterRows_, score, flipping, level ,playingField):
  '''
  If a player completes a row, this will remove it, shorten the tower, and award points

  parameters 
  ---------------
  masterRows - a list with all the tiles on board
  score - an interger that tells us how many points the player has
  flipping - tells us what direction the pieces are going so that we can shorten the tower accordingly 
  level - 1,2 or 3 
  playingField - pygame rectangle 

  
  '''
  row_deleted = ''
  rowNumber = 0

  
  for row in masterRows_:
    
    if len(row) >= playingField.width/blockWidth : #however big the stadium is
    
      score += 100
      for x in range(len(row)):
        row_deleted = (row[0])[0].y#finding out what row it is 
        row.remove(row[0])#deleting all teh tiles 
      if level == 3:  #level three has 2 towes, so we only want to shorten one of them 
        if flipping ==  -1:
          #moves the rows above the deleted row down 
          for row in range(48,25 ,-1):
            for block in masterRows_[row]:
              if block[0].y < row_deleted:
                for also in masterRows_[row]:
                  masterRows_[row + 1].append(also)
                block[0].y+=10 
                masterRows_[row] = []
                
        
        else:#moving the rows above the deleted row down 
          for row in range(0,25):
            for block in masterRows_[row]:
                if block[0].y > row_deleted:
                  for also in masterRows_[row]:
                    masterRows_[row -1].append(also)
                  block[0].y-=10
                    
                  masterRows_[row] = []
            
            
      else:
        if flipping ==-1:#same thing as the line before but for mormal
          for alsoRow in range( len(masterRows_)):        
            for alsoBlock in masterRows_[alsoRow]:
              if alsoBlock[0].y > row_deleted:
                for block in masterRows_[alsoRow]:
                  masterRows_[alsoRow -1].append(block)
                masterRows_[alsoRow] = []
                alsoBlock[0].y -= 10
                
          
      
        else: # same as above for medium mode 
          for alsoRow in range( len(masterRows_)-1, -1 , -1):
            
            for alsoBlock in masterRows_[alsoRow]:
              if alsoBlock[0].y < row_deleted:
                for block in masterRows_[alsoRow]:
                  masterRows_[alsoRow +1].append(block)
                masterRows_[alsoRow] = []
                alsoBlock[0].y += 10
                
                
  return score




      

          
          
def player_handle_movements(keys_pressed, player, playingField, masterRows, canGoDown, flipping, score):
  ''' this will control the user interface for moving the peice
  
  variable
  --------
  keys_pressed contains all of the keys pressed
  player is a list of the squares that make up the moving piece
  playingField is a pygame rectanfe
   masterRows is a list of all the blocks on the board
   canGoDown is a bool True or False that tells the module if the platyer can use the down arrow key
   flipping is 1 or -1 and tells the program which way the piece is moving 
   score is an integer 
  
  
  '''
  can_move = True
  playerRow = ''


    
  if keys_pressed[pygame.K_LEFT]:#moves piece left
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

  if keys_pressed[pygame.K_RIGHT]:#moving the piece right 
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
  if keys_pressed[pygame.K_DOWN]:#movinf the piece closer to the ends of the map 
    if flipping ==1:
      if canGoDown:
        can_move = True
        for piece in player:
          if piece[0].y == WIN.get_height() - piece[0].height:
            can_move = False
          else:
            playerRow = int((piece[0].y + piece[0].height)//10 - 1)
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
            playerRow = int((piece[0].y + piece[0].height)//10 - 1)
            for block in masterRows[playerRow +1]:
              if block[0].x == piece[0].x:
                can_move = False
        if can_move:
          for block in player:
            block[0].y += block[0].width
          score += 1
    else:
      if canGoDown:#this moves the piece down 
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
          score += 1
  return score 


        

def instructions(phrase, press_space, picture):
  ''' this will handle what happens if the instructisns item is selected in the main menu
  
  variable
  --------
  phrase is a string 
  press_space is a string 
  picture is an uploaded file'''
  quit = False
  for letter in range(len(phrase)+1):#simulates the typing look 
    WIN.blit(picture, (-5,-5)) #the background for that screen 
    text = REGULAR_FONT.render(phrase[0:letter], 1, WHITE)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()

       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:       #this can be used to skip the typinf animation 
             text = REGULAR_FONT.render(phrase, 1, WHITE)
             quit = True
          if event.key == pygame.K_ESCAPE:#ends the program 
            pygame.display.quit()
            pygame.quit()
            break
    WIN.blit(text, (int(WIN.get_width()//2 - .5*text.get_width()), WIN.get_height()//10))
    pygame.display.update()
    time.sleep(.1)#this delay makes the typing action 
    if quit:
      break

 
  pressSpace = REGULAR_FONT.render(press_space, 1, WHITE)
             
  run = True
  blinking = 0
  while run:
    blinking +=1
    for event in pygame.event.get():
       if event.type == pygame.QUIT:#press the X button of the tab
          pygame.display.quit()
          pygame.quit()

       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:#goes to the next slide 
             run = False
             
    WIN.blit(picture,(-5,-5))
    WIN.blit(text, (int(WIN.get_width()//2 - .5*text.get_width()), 50))

    if blinking == 2:#blinking animation 
      blinking = 0
      WIN.blit(pressSpace, (int(WIN.get_width()//2 - .5*pressSpace.get_width()), 450))
      pygame.display.update()
    pygame.display.update()
    time.sleep(.5)

def intro():#facilitates calling the instructions modules 
  ''' this handles calling all of the instructions slides'''
  press_space = 'Press space to continue'
  phrase1 = 'Press the arrow keys to move your piece left and right'
  phrase2 = 'Press the down arrow to move the piece down'
  instructions(phrase1, press_space, instructions1)
  instructions(phrase2, press_space, instructions2)
  instructions("press the up arrow to rotate the shape", press_space, instructions3)
  instructions("By completely filling up a row, you will get points", press_space, instructions4)
  instructions("Filling a row will also delete the row and move all the blocks above it down!", press_space, instructions5)
  instructions("Try and keep the tower as small as possible and keep it from touching the top!", press_space, instructions5)
  from main_menu_slides import main_menu
  main_menu(WIN,  masterRows)
  


def tempGameOver(score, level):#this is calling the leaderboard if they 
  '''This handles end game for infinite mode
  variable
  --------
  score - integer 
  level - integer'''
  
  file = ''
  if level == 1:
    file = 'leaderBoard.txt'
  elif level == 2:
    file = 'level_2_leaderboard.txt'
  else: 
    file = 'level_3_leaderboard.txt'
  leaders = openLeaderboard(level)#this is going to see if they made the leaderboard 

  leaderNames = leaders[0]
  leaderScores = leaders[1]


  placement = None
  for value in range(len(leaderScores)-1, -1, -1):#this is where we check to see if the score was able to make the leaderboard 
    if score > int(leaderScores[value]):
      placement = value 

  if placement != None:#= got on the leaderboard 
    name = getName()
    leaderNames.insert(placement , name)
    leaderScores.insert(placement, score)

    leaderFile = open(file, 'w+')#write to the fiel 
    for x in range(10):
      leaderFile.write('%s: %s \n'%(leaderNames[x], leaderScores[x]))

    leaderFile.close()     
    
    
  from main_menu_slides import main_menu
  main_menu(WIN, masterRows)
  

def getName():#create a button to leave the thing
  '''THis is how the game gets user's name
  
  '''
  input_rectangle = pygame.Rect(WIN.get_width()//2 - 60, int(WIN.get_height()*(1/3)+50), 120, 30)#where the input is displayed
  press_to_continue = pygame.Rect(WIN.get_width()//2 - 60, int(WIN.get_height()*(1/3)+100), 120, 30)#confirmation button 
  Congrats = REGULAR_FONT.render('Amazing! You made the leaderboard!', 1, YELLOW)#celebratory messages 
  type_name = REGULAR_FONT.render('Type your name and press continue', 1, YELLOW)#instructios 
  continue_ = BIG_FONT.render('CONTINUE', 1, BLUE)#the text for the next level botton 

  user_text = ''
  active = False #used to see if they are selecting the text box  
  runProgram = True
  while runProgram:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:#quit the program 
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:#tracks the mouth position 
        if input_rectangle.collidepoint(event.pos):#does it colide with the input box?
          active = True
        else:
          active = False 
        if press_to_continue.collidepoint(event.pos):#stops the while loop 
          runProgram = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:#escape ends the prgram 
          pygame.display.quit()
          pygame.quit()
          break
        if event.key == pygame.K_BACKSPACE:#remove a letter of the input 
          if len(user_text) > 0 and active:
            user_text = user_text[:-1]
        elif event.key == pygame.K_RETURN:#we dont want the enter key to be added as \n and mess up the array, so we pass
          pass
        else:
          if active and len(user_text)<9:#all other characters will be added here
            user_text += event.unicode
    typed = REGULAR_FONT.render(user_text, 1, RED)
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, press_to_continue)
    pygame.draw.rect(WIN, WHITE, input_rectangle)

  #displayign everything 
    WIN.blit(Congrats, (WIN.get_width()//2- .5*Congrats.get_width(), WIN.get_height()/6))
    WIN.blit(type_name, (WIN.get_width()//2 - .5*type_name.get_width(), WIN.get_height()/6 + type_name.get_height()*2))
    WIN.blit(continue_, (press_to_continue.x+.5*press_to_continue.width - continue_.get_width() *.5, press_to_continue.y+10))
    WIN.blit(typed, (input_rectangle.x+.5*input_rectangle.width - typed.get_width() *.5, input_rectangle.y + .5*input_rectangle.height - .5*typed.get_height()))
    pygame.display.update()
  return user_text




    
    

  

 



def moving(masterRows, runProgram, score, level, flipping, campaign, WIN):#flipping will be a 1 or a -1, and it will determine if the map flips everytime or not for levels 2, where the map flips 
  '''
  Facilitates the game. The main module 
  
  parameters 
  -----------
  masterRows - list with all of the game's pieces
  runProgram - makes sure that we want the game to be running, boolean value
  score - integer 
  level - 1,2, or 3 
  flipping - tells us what direction the pieces move 
  campaign - tells us what game mode we are playing 
  WIN - the pygame window 
  
  '''
  
  
  rowsDeleted = 0 
  rowNumber = 0
  gameOver = False
  timeTracker = 0
  movement = True
  powers = 3 
  selected = False 
  fullscreen = False
  if level == 1:
    speed = 20
  elif level == 2:
    speed = 30
  elif level == 3:
    speed = 40

  clock = pygame.time.Clock( )
  clock.tick(40)

  while(runProgram):

    #making the palying field 
    playingField = pygame.Rect((0, 0), (300, 500))

    playingField.x = 450 - .5*playingField.width

    playingFieldDisplay = pygame.transform.scale(pygame.image.load(os.path.join('FBLA_logo.jpg')), (300, 500))
    power_button = pygame.Rect((230, 430), (60, 60))



   
    piece = making_piece( flipping, level, playingField)
      
            
          
    while movement:
  

      for row in masterRows:#this checks if the game has to end because the piece reached teh top 
        for block in row:
          for also_block in piece:
            if block[0].colliderect(also_block[0]):
              if bool(campaign):
          
                campaign_end(level, score, rowsDeleted, WIN)
                
              else:
                tempGameOver(score, level)
              main_menu(WIN,  masterRows)
              
              break
            
      
      keys_pressed = pygame.key.get_pressed( )#a map of all the game's keyboard keys and if they are pressed or not 

      score = player_handle_movements(keys_pressed, piece, playingField, masterRows, True, flipping, score)#moving the piece 
        
      timeTracker = 0
      tempScore = add_row(masterRows, score, flipping, level, playingField)#deleting a row
      if tempScore != score:
        rowsDeleted += 1#this increased if a row was deleted 
      score = tempScore
      pause = False
      for event in pygame.event.get():#all the events 
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
        elif event.type == pygame.VIDEORESIZE:#full screen isnt enebled but this checks if the windo size is changed 
          if not fullscreen:
            WIN = pygame.display.set_mode([event.w, event.h],pygame.RESIZABLE )

        if event.type == pygame.MOUSEBUTTONDOWN:#checks the mouse's position when clicked 
          if power_button.collidepoint(event.pos):#if it hit the power up button 
            selected = not selected 
          elif selected:#if it is activated, then this checks if the power up was used 
            if powers >0:
              for row in masterRows:
                for item in row:
                  if item[0].collidepoint(event.pos):
                    row.remove(item) 
                    powers -=1  
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            rotation(piece, masterRows, playingField)

          if event.key == pygame.K_ESCAPE:#ends program 
            pygame.display.quit()
            pygame.quit()
            movement = False
            runProgram = False
            break
          
          if event.key == pygame.K_SPACE:#facilitates pausing 
            pause = not pause

         # if event.key == pygame.K_f:
            #fullscreen = not fullscreen 
            #if fullscreen:
            #  WIN = pygame.display.set_mode([monitor_size[0], monitor_size[1]],pygame.FULLSCREEN )
            #else:
             # WIN = pygame.display.set_mode([WIN.get_width(), WIN.get_height()],pygame.RESIZABLE )


            
      while pause:
        pause = pause_(WIN)#the pause module 
        
      
      can_go_down = True
      if flipping == 1:#moving the piece
        for item in piece:#checks to see if the piece is going above the baord or below it
          if item[0].y + item[0].height >= WIN.get_height():    
            can_go_down = False      
          
          for row in masterRows:
            for block in row:
              if item[0].y + item[0].height == block[0].y:
                if item[0].x == block[0].x:
                  can_go_down = False
      else:
        for item in piece:#Checking if the tile is at the top for if the tile is traveling up not down 
          if item[0].y <= 0:    
            can_go_down = False
            

          for row in masterRows:
            for block in range(len(row)):
              if item[0].y - item[0].height == (row[block])[0].y:
                if item[0].x == (row[block])[0].x:
                  can_go_down = False


      if can_go_down:
        
        for item in piece:
          item[0].y+= item[0].height*flipping#moving the piece 
      
      else:
        for block in piece:
          masterRows[int((block[0].y + block[0].height)/10 - 1)].append(block)
        if level == 1 or level == 2:
          piece = making_piece( flipping, level, playingField)
        else:
          flipping*= -1
          piece = making_piece( flipping, level, playingField)
        #runProgram = False
        #movement = False


      while timeTracker != 5:
        timeTracker+=1
        clock.tick(FPS)      
          

      drawWindow(playingField, piece, masterRows, score, level, flipping, campaign, rowsDeleted, powers, power_button, selected)
      
def game_instructions(level):
  '''
  returns the text that needs to be outputted

  level - 1,2 or 3 and decides what the text is
  
  '''
  instructions = []
  if level == 1:#redering the instructions and adding it to a list 
    instructions1_ = REGULAR_FONT.render("Press side arrows to move ", 1, WHITE)
    instructions_1 = REGULAR_FONT.render('the piece left and right', 1, WHITE)
    empty = REGULAR_FONT.render('_', 1, BLACK)
    instrucitons2_ =  REGULAR_FONT.render("Press the up arrow to", 1, WHITE) 
    instructions_2 = REGULAR_FONT.render("rotate the piece", 1, WHITE)
    instrucitons3_ =  REGULAR_FONT.render("Press the down arrow to ", 1, WHITE)
    instructions_3 = REGULAR_FONT.render("move the piece down", 1, WHITE)
    instructions = [instructions1_,instructions_1,empty, instrucitons2_, instructions_2, empty, instrucitons3_,instructions_3 ]     
  elif level == 2:#redering the instructions and adding it to a list 
    instructions1_ = REGULAR_FONT.render("Press side arrows to move ", 1, WHITE)
    empty = REGULAR_FONT.render('_', 1, BLACK)
    
    instructions_1 = REGULAR_FONT.render('the piece left and right', 1, WHITE)
    instrucitons2_ =  REGULAR_FONT.render("Press the up arrow to", 1, WHITE) 
    instructions_2 = REGULAR_FONT.render("rotate the piece", 1, WHITE)
    instrucitons3_ =  REGULAR_FONT.render("Press the down arrow to ", 1, WHITE)
    instructions_3 = REGULAR_FONT.render("move the piece down", 1, WHITE)
    instructions  = [instructions1_,instructions_1,empty, instrucitons2_, instructions_2, empty, instrucitons3_,instructions_3 ]     
  
  else:#redering the instructions and adding it to a list 
    instructions1_ = REGULAR_FONT.render("Press side arrows to move ", 1, WHITE)
    empty = REGULAR_FONT.render('_', 1, BLACK)
    
    instructions_1 = REGULAR_FONT.render('the piece left and right', 1, WHITE)
    instrucitons2_ =  REGULAR_FONT.render("Press the up arrow to", 1, WHITE) 
    instructions_2 = REGULAR_FONT.render("rotate the piece", 1, WHITE)
    instrucitons3_ =  REGULAR_FONT.render("If the piece is moving down,", 1, WHITE)
    instruction_3 = REGULAR_FONT.render("press the down arrow to move the piece down", 1, WHITE)  
    instructions4_=  REGULAR_FONT.render("If the piece is moving up", 1, WHITE)
    instructions_4=  REGULAR_FONT.render("press the down arrow to move the piece up", 1, WHITE)
    instructions = [instructions1_, instructions_1, empty, instrucitons2_, instructions_2, empty, instrucitons3_, instruction_3, empty,instructions4_, instructions_4]     
  return instructions

def pause_(WIN):
  '''
  pauses the game and gives the user the option to unpause or go to main menu

  WIN - the pygame window
  
  '''
  
  pause = True
  temp_font = pygame.font.SysFont('open sans', 70)
  while(pause):
    WIN.fill(BLACK)
    text = temp_font.render("Press The Space Bar To Continue", 1, YELLOW)
    WIN.blit(text, (WIN.get_width()//2  - text.get_width()//2, 100))
    mainmenu = temp_font.render("MAIN MENU", 1, RED)
    mainmenu_rect = mainmenu.get_rect()
    mainmenu_rect.x, mainmenu_rect.y =  computer_rect,y = WIN.get_width()//2  - mainmenu.get_width()//2, 300
    WIN.blit(mainmenu, (WIN.get_width()//2  - mainmenu.get_width()//2, 300))
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:#press the X out 
        pygame.display.quit()
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:#escape key must end the program 
          pygame.display.quit()
          pygame.quit()
          movement = False
          runProgram = False
          break
        if event.key == pygame.K_SPACE:
          pause = False
      if event.type == pygame.MOUSEBUTTONDOWN:
  
        if mainmenu_rect.collidepoint(event.pos):#this is if they chose to return to main menu 
          one = []
          for i in range(50):
            one.append([])                
          from main_menu_slides import main_menu
          main_menu(WIN, one )        

    pygame.display.update()
  return False         
  
     

  
  



if __name__ == "__main__":

  main_menu(WIN,  masterRows)

