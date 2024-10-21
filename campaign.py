import pygame
pygame.font.init()
BLACK = (15,15,15)
YELLOW = (255, 255, 0)
#requirements 
# level one: score must be more than 5,000, delete 35 rows, 8 thousand
#level 2: s ore more than 8 thousand
BIG_FONT = pygame.font.SysFont('open sans', 60)
REGULAR = pygame.font.SysFont('open sans', 40)

def campaign_end(level, score, rowsDeleted, WIN):
    ''' will facilitate the campaign gamemode
    
    parameters 
    ------------
    level - integer 1, 2 or 3 
    score - integer 
    rowsDeleted - integer 
    WIN - pygame window 
     '''
    requirements = 0#checking to see if they have enough requirements 
    if level==1: 
        if score >= 5000:
            requirements +=1
        if rowsDeleted >=35:
            requirements +=1
        if score >= 8000:
            requirements +=1
    elif level ==2: 
        if score >= 8000:
            requirements +=1
        if rowsDeleted >=50:
            requirements +=1
        if score >= 10000:
            requirements +=1 

    else: 
        if score >= 10000:
            requirements +=1
        if rowsDeleted >=70:
            requirements +=1
        if score >= 15000:
            requirements +=1 
    campaign_new_level(level, requirements, WIN)
    
    
            
            

def campaign_new_level(level, requirements, WIN):
    
    options = 1
    yes_no = "You didn't complete enough requirements"#this is the you lose
    if requirements >= 2:#they won the game, all three levels 
        if level ==3:
            one = []
            for i in range(50):
                one.append([])
            main_menu(WIN, 900, 500, one)
            
        options = 2 
        
        yes_no = "You completed level "+ str(level)+" and can go to level "+str(level+1)+"!!"
         
    run = True
    while(run):    #the screen that gives the end game options 
        WIN.fill(BLACK)
        text = BIG_FONT.render(yes_no, 1, YELLOW)
        WIN.blit(text, (900//2 - text.get_width()//2, 150 ))
    
        mainmenu = BIG_FONT.render("Main Menu", 1, YELLOW)#will always didsplay main menu
        if options ==1:
            next_level = BIG_FONT.render("Retry Level", 1, YELLOW)
        else:
            next_level = BIG_FONT.render("Next Level", 1, YELLOW)
            
        main_menu_rect = mainmenu.get_rect()
        next_level_rect = next_level.get_rect()
        
        main_menu_rect.x = WIN.get_width()//4 - main_menu_rect.width//2#setting position 
        main_menu_rect.y = 330
        next_level_rect.x = 900//4 *3 - next_level_rect.width//2
        next_level_rect.y = 330
        
        WIN.blit(mainmenu, (main_menu_rect.x, main_menu_rect.y))
        WIN.blit(next_level, (next_level_rect.x, next_level_rect.y))
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            
          if event.type == pygame.KEYDOWN:
    
        
            if event.key == pygame.K_ESCAPE:#escape key ends the program 
                pygame.display.quit()
                pygame.quit()
                break        
          if event.type == pygame.MOUSEBUTTONDOWN:#this checks where the mouse is clicked 
      
            if main_menu_rect.collidepoint(event.pos):
                one = []
                for i in range(50):
                    one.append([])                
                from main_menu_slides import main_menu
                
                main_menu(WIN,one)
                
                
                
            elif next_level_rect.collidepoint(event.pos):#calling the level if the player choses next level 
                one = [[] for i in range(50)]
                if options == 1:
                    from main import moving
                    moving(one, True, 2, level, 1,1, WIN)
                    
                if options == 2:
                    from main import moving
                    moving(one, True, 2, level +1, 1,1,WIN)
                    
                    
        
        
        
        pygame.display.update()
    

    
        
    
        
    
        
    