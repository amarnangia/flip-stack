
from calendar import c
import pygame
import os
pygame.font.init()
from multiplayer import multiplayer_move

RED = (255, 0 ,0)
BLUE = (10,20,238)
VIOLET = (127, 0, 255)
BLACK = (0,0,0)
YELLOW = (255,255,0)





def main_menu(WIN, masterRows):

  ''' This will manage the title screen and will call other functions based on what the user chooses 
  
  WIN is the window 
  Width is the width of the window 
  Height is the height of the window 
  masterrows is a list with nested lists that all represent a row in the playing field. each row contains the blocks in that row'''
  
  
  runProgram = True
  on_off = pygame.mixer.music.get_busy()
  
  
  while runProgram:
    SMALL_FONT = pygame.font.SysFont('comicsans', WIN.get_height()//50)
    REGULAR_FONT = pygame.font.SysFont('comicsans', WIN.get_height()//25)
    MIDDLE_FONT =  pygame.font.SysFont('comicsans', WIN.get_height()//20)
    BIG_FONT = pygame.font.SysFont('comicsans', (WIN.get_height()//(50//3)))
    MEGA_FONT = pygame.font.SysFont('comicsans', (WIN.get_height()//(500//35)))
    title = pygame.transform.scale(pygame.image.load(os.path.join('title.png')), ((WIN.get_width()//3.6), (WIN.get_height()//4)))
    
    WIN.fill(BLACK)
    levels = MEGA_FONT.render('INFINITE', 1, BLUE)
    levels_rect = levels.get_rect()
    instructions = MEGA_FONT.render('INSTRUCTIONS', 1, BLUE)
    instructions_rect = instructions.get_rect()
    multiplayer = MEGA_FONT.render("MULTIPLAYER", 1, BLUE) 
    multiplayer_rect = multiplayer.get_rect()
    campaign = MEGA_FONT.render("CAMPAIGN", 1, BLUE)
    campaign_rect = campaign.get_rect()
    WIN.fill(BLACK)
    WIN.blit(title, (WIN.get_width()//2 - title.get_width()//2, WIN.get_height()//12.5))
    music = REGULAR_FONT.render('MUSIC',1, BLUE)
    music_rect = music.get_rect()
    

    levels_rect.x = WIN.get_width()//2 - levels.get_width()//2
    levels_rect.y = WIN.get_height()//2.5

    music_rect.x = WIN.get_width() - music.get_width() *2
    music_rect.y =  WIN.get_height() - music.get_height()*2
    multiplayer_rect.x = WIN.get_width()//2 - multiplayer_rect.width//2
    multiplayer_rect.y = WIN.get_height()/2.5 + multiplayer_rect.height*1.5
    campaign_rect.x = WIN.get_width()//2 - campaign.get_width() //2
    campaign_rect.y = campaign_rect.height *1.5 + multiplayer_rect.y  

 
    instructions_rect.x = (WIN.get_width()//2 - instructions.get_width()//2)
    instructions_rect.y = instructions_rect.height *1.5 + campaign_rect.y  
    
    WIN.blit(levels, (levels_rect.x, levels_rect.y))
    WIN.blit(instructions, (instructions_rect.x, instructions_rect.y))
    WIN.blit(music, (music_rect.x, music_rect.y))
    WIN.blit(multiplayer, (multiplayer_rect.x, multiplayer_rect.y))
    WIN.blit(campaign, (campaign_rect.x, campaign_rect.y))

    pygame.display.update()
          
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.display.quit()
          pygame.quit()
          break
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
  
        if levels_rect.collidepoint(event.pos):
          select_levels(WIN, masterRows)
          
        if multiplayer_rect.collidepoint(event.pos):#fix this 
          
          one = [ []  for i in range(50)]
          two =[ []  for i in range(50)]
          print(one)
          multiplayer_move(one, two, 1, 0, 0, 1, 1,1, WIN) 
          
        if instructions_rect.collidepoint(event.pos):
          from main import intro
          intro()  
          
        if campaign_rect.collidepoint(event.pos):
          from main import moving
          moving(masterRows, True, 2, 1, 1,1, WIN)
          
        if music_rect.collidepoint(event.pos):
          if on_off:
            pygame.mixer.music.stop()
            on_off = False
     
          else:
            pygame.mixer.music.play()
            on_off = True



def select_levels(WIN, masterRows):
  ''' This function controlls chosing levels for infinite game mode 
  variables
  ---------
  WIN - the window 
  WIDTH and HEIGHT are the dimentions of the window 
  master rows constains all of the blocks on the board'''
  
  from main import moving #moving will be called here, and if I import moving before, the whole game breaks 

  WIN.fill(BLACK)

  selected = None 
  highlighted_box = pygame.Rect((0,0), (1,1))
  texts = []

  
  runProgram = True
  while runProgram:
    SMALL_FONT = pygame.font.SysFont('comicsans', WIN.get_height()//50)
    REGULAR_FONT = pygame.font.SysFont('comicsans', WIN.get_height()//25)
    MIDDLE_FONT =  pygame.font.SysFont('comicsans', WIN.get_height()//20)
    BIG_FONT = pygame.font.SysFont('comicsans', (WIN.get_height()//(50//3)))
    MEGA_FONT = pygame.font.SysFont('comicsans', (WIN.get_height()//(500//35)))
    select = BIG_FONT.render('Click A Level and Press Enter to Play', 1, BLUE)
    title = pygame.transform.scale(pygame.image.load(os.path.join('title.png')), ((WIN.get_width()//3.6), (WIN.get_height()//4)))
    go_main_menu = REGULAR_FONT.render('<- Main Menu', 1, RED ) 
    main_menu_rect = go_main_menu.get_rect()
    level1 = BIG_FONT.render('NORMAL', 1, RED )
    level2 = BIG_FONT.render('MEDIUM', 1, RED )
    level3 = BIG_FONT.render('HARD', 1, RED )
    level1_rect = pygame.Rect(( WIN.get_width()//3 - 200, WIN.get_height() *(2/5)), (WIN.get_width()//6,WIN.get_height()//10))
    level2_rect = pygame.Rect((WIN.get_width()//2 - 75,WIN.get_height() *(2/5)  ), (WIN.get_width()//6,WIN.get_height()//10))
    level3_rect = pygame.Rect((WIN.get_width()*(2/3) + 50, WIN.get_height() * (2/5)), (WIN.get_width()/6,WIN.get_height()//10))
    main_menu_rect.x = WIN.get_width()/90
    main_menu_rect.y = WIN.get_height()/50
    WIN.fill(BLACK)
    if bool(selected): #this is going to make sure a level has been selected
      highlighted_box = pygame.Rect((selected.x -1, selected.y - 1), (selected.width+2, selected.height + 2))
      pygame.draw.rect(WIN, YELLOW, highlighted_box )
      pygame.draw.rect(WIN, BLACK, selected )


    WIN.blit(go_main_menu, (10,10))
    WIN.blit(level1, (WIN.get_width()//3 - .5*level1.get_width()- WIN.get_width()//7.2, level1_rect.y+ level1_rect.height*.5 - .5*level1.get_height()))
    WIN.blit(level2, (WIN.get_width()//2 - .5*level2.get_width(), level2_rect.y+ level2_rect.height*.5 - .5*level2.get_height()))
    WIN.blit(level3, (WIN.get_width()*(2/3) - .5*level3.get_width()+WIN.get_width()//7.2, level3_rect.y+ level3_rect.height*.5 - .5*level3.get_height()))
    WIN.blit(select, (WIN.get_width()//2 - select.get_width()*.5, 50))
   
    for text in range(len(texts)):
      WIN.blit(texts[text], (WIN.get_width()//2 - texts[text].get_width()*.5, 350+text*50))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if main_menu_rect.collidepoint(event.pos):
          from main_menu_slides import main_menu
          main_menu(WIN, masterRows)
          runProgram = False

        if level1_rect.collidepoint(event.pos):
          selected = level1_rect
          text = REGULAR_FONT.render("Blocks spawn at the top of the playing field and fall down.", 1, YELLOW)
          text2 = REGULAR_FONT.render("Try and keep the tower from getting too big!", 1, YELLOW)
          texts = [text, text2]
        if level2_rect.collidepoint(event.pos):
          text = REGULAR_FONT.render("Blocks will start at the top and move up.", 1, YELLOW)
          text2 = REGULAR_FONT.render("Try and keep the tower from reaching the bottom!", 1, YELLOW)
          texts = [text, text2]

          selected = level2_rect   
        if level3_rect.collidepoint(event.pos):
          selected = level3_rect 
          text = REGULAR_FONT.render("Blocks will start in the middle and will", 1, YELLOW)
          text2 = REGULAR_FONT.render("alternate between going up or going down!", 1, YELLOW)
          
          texts = [text, text2]          

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.display.quit()
          pygame.quit()
          break
        if event.key == pygame.K_RETURN:
          if bool(selected): #making sure something is selected\
            
            if selected == level1_rect: 
              
              moving(masterRows, True, 2, 1, 1,0, WIN)

            elif selected == level2_rect:
              moving(masterRows, True, 2, 2, -1,0, WIN)
            else: 
              moving(masterRows, True, 2, 3, -1, 0, WIN)
            runProgram ==False
            break 

        if event.type == pygame.MOUSEBUTTONDOWN:
      
          if main_menu_rect.collidepoint(event.pos):
            one = []
            for i in range(50):
              one.append([])                
            from main_menu_slides import main_menu
      
            main_menu(WIN,one )        
         
    
    



