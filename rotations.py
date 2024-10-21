import time
def rotation(piece, masterRows, playingField):
  '''
  Z temporarily has bugs, so we have taken those commands down 

this facilitates the rotations 

  '''
  can_rotate = True
  if len(piece) == 1: #one block 
    pass
  elif len(piece) == 3: #three straight or small L
    if ((piece[0])[0].x == (piece[2])[0].x  and (piece[0])[0].x == (piece[1])[0].x)  or (piece[0])[0].y == (piece[2])[0].y and (piece[0])[0].y == (piece[1])[0].y:
      rotation_short_stick(piece, masterRows, playingField)
    else:
      small_L(piece, masterRows, playingField)
      
  elif len(piece) == 5:
    if (piece[4])[0].x == (piece[0])[0].x and (piece[1])[0].y == (piece[3])[0].y: #plus sign +
      pass

    elif (piece[0])[0].x == (piece[1])[0].x and (piece[2])[0].x == (piece[4])[0].x: #this means that it is the z is the s shape in the 1st or 3rd rotation
      if (piece[0])[0].x < (piece[4])[0].x: #this means that it is S shape in rotation 1, or Z shape in rotatoin 3
        #if (piece[0])[0].x < (piece[4])[0].x: #this means that this is the s shape in its first rotation
          S_rotation(piece, masterRows, playingField, 1)
        #else: #this means it is shape Z in rotation 3
 
         # Z_rotation(piece, masterRows, playingField, 3)
      else: #this is S in rotation 3 or Z in rotation 1
        #if (piece[0])[0].y < (piece[4])[0].x:#this means that it is Z in the first rotation \
          
          S_rotation(piece, masterRows, playingField, 3)
        #else:#this is S in rotation 3
         # Z_rotation(piece, masterRows, playingField, 1)
    elif (piece[0])[0].y == (piece[4])[0].y and (piece[1])[0].y == (piece[2])[0].y:#this is The 2nd or 4th rotation for S or Z shape 
      if (piece[0])[0].y > (piece[2])[0].y: #this means that it is esther S in rotation 2 or z in rotation 4
        #if (piece[2])[0].x < (piece[4])[0].x:
         # Z_rotation(piece, masterRows, playingField, 4)
        #else:
          S_rotation(piece, masterRows, playingField, 2)
      else:
        #if (piece[0])[0].x < (piece[2])[0].x:
         # Z_rotation(piece, masterRows, playingField, 2)
        #else:
          S_rotation(piece, masterRows, playingField, 4)


def Z_rotation(piece, masterRows, playingField, rotation):
  '''
  called when Z piece is rotated 

  parameters 
  ----------
  piece - list of the blocks that make up the Z piece 
  masterRows - a list of all the blocks on screen 
  playingField - pygame rectangle 
  roation - which rotation the piece is on 
  
  '''
  modify_left = False
  modify_right = False
  modify_up = False
  can_rotate = True
  if rotation == 1:
    piece_row = int((piece[2][0].y + piece[2][0].height)/10 -1)

    if (piece[1])[0].x-2*(piece[1])[0].width <= playingField.x:
      modify_right = True 
    if (piece[1])[0].x+2*(piece[1])[0].width >= playingField.x + playingField.width:
      modify_left = True 

    for block in masterRows[piece_row]:
      if (block)[0].x == (piece[1])[0].x + (piece[1])[0].width:
        can_rotate = False
    for block in masterRows[piece_row-1]:
      if (block)[0].x == (piece[1])[0].x-(piece[1])[0].width:
        can_rotate = False
    for block in masterRows[piece_row-1]:
      if (block)[0].x == (piece[1])[0].x-2*(piece[1])[0].width:
        can_rotate = False
    if can_rotate:
      (piece[0])[0].x -= 2*(piece[0])[0].width#moves left 2
      (piece[2])[0].x += 2*(piece[2])[0].width#moves right 2
      (piece[3])[0].y -= 2*(piece[3])[0].height#moves up 2
      (piece[4])[0].x += (piece[4])[0].width#moves right 1
      (piece[4])[0].y -= 3*(piece[4])[0].height#moves up 3
    
  elif rotation == 2:
    piece_row = int(((piece[1])[0].y + (piece[1])[0].height)/10 -1)
  for block in masterRows[piece_row]:
      if block[0].rect.x == (piece[1])[0].x - (piece[1])[0].width:
        can_rotate = False
  for block in masterRows[piece_row+1]:
      if (block)[0].x == (piece[1])[0].x - (piece[1])[0].width:
        can_rotate = False
  for block in masterRows[piece_row-2]:
      if (block)[0].x == (piece[1])[0].x:
        can_rotate = False
  if can_rotate:
    (piece[0])[0].x += (piece[0])[0].width#moves right 1
    (piece[0])[0].y += 2*(piece[0])[0].height#moves down 2
    (piece[1])[0].x -= (piece[1])[0].width#moves left 1
    (piece[2])[0].x -= (piece[2])[0].width#moves left 1
    (piece[3])[0].x += (piece[3])[0].width#moves right 1
    (piece[4])[0].y -= (piece[4])[0].height#moves up 1
    
    
#NEWWWWWWWWW SSSSSTOP POINT   #############################################################
  elif rotation == 3:
    piece_row = int(((piece[2])[0].y + (piece[2])[0].height)/10 -1)
    for block in masterRows[piece_row+1]:
      if (block)[0].rect.x == (piece[2])[0].x:
        can_rotate = False
    for block in masterRows[piece_row+1]:
      if (block)[0].rect.x == (piece[2])[0].rect.x + (piece[2])[0].rect.width:
        can_rotate = False
    if piece_row <49:
      for block in masterRows[piece_row+2]:
        if (block)[0].rect.x == (piece[2])[0].rect.x + (piece[2])[0].rect.width:
          can_rotate = False
    else:
      can_rotate = False
    if can_rotate:
      (piece[0])[0].x += (piece[0])[0].width#moves right 1
      (piece[1])[0].x += (piece[1])[0].width#moves right 1
      (piece[2])[0].x -= (piece[2])[0].width#moves left 1
      (piece[3])[0].x += (piece[3])[0].width#moves right 1
      (piece[3])[0].y += 2*(piece[3])[0].height#moves down 2
      (piece[4])[0].x += 2*(piece[4])[0].width#moves right 2
      (piece[4])[0].y += 3*(piece[4])[0].height#moves down 3



  else: #rotation 4
     piece_row = int(((piece[1])[0].y + (piece[1])[0].height)/10 -1)
     for block in masterRows[piece_row-1]:
      if (block)[0].rect.x == (piece[1])[0].x:
        can_rotate = False
     for block in masterRows[piece_row+1]:
      if (block)[0].rect.x == (piece[1])[0].x - (piece[1])[0].rect.width:
        can_rotate = False
     if piece_row <=47:
      for block in masterRows[piece_row+2]:
        if (block)[0].rect.x == (piece[1])[0].x - (piece[1])[0].rect.width:
          can_rotate = False
     else:
      can_rotate = False
     if can_rotate:
       (piece[0])[0].y += (piece[0])[0].height#moves up 2
       (piece[3])[0].x -= 2*(piece[3])[0].width#moves left 2
       (piece[4])[0].x -=3* (piece[4])[0].width#moves left 3
       (piece[4])[0].y += (piece[4])[0].height#moves down 1



          
def S_rotation(piece, masterRows, playingField, rotation):
  '''
    called when S piece is rotated 

  parameters 
  ----------
  piece - list of the blocks that make up the Z piece 
  masterRows - a list of all the blocks on screen 
  playingField - pygame rectangle 
  roation - which rotation the piece is on 
  '''
  modify_left = False
  modify_right = False
  modify_up = False
  can_rotate = True

  if rotation == 1:
    piece_row = int(((piece[1])[0].y + (piece[2])[0].height)/10 -1)
    if (piece[1])[0].x-(piece[1])[0].width <= playingField.x:
     
   
      can_rotate = False #this means that we need to modify the object ot shift right 
    if (piece[2])[0].x+2*(piece[2])[0].width >= playingField.x + playingField.width:

      can_rotate = False #this means the object most 


    for block in masterRows[piece_row]:
      if (block)[0].x == (piece[2])[0].x - (piece[2])[0].width*2:#
        can_rotate = False

    for block in masterRows[piece_row-1]:
      if (block)[0].x == (piece[0])[0].x + (piece[0])[0].width or (block)[0].x == (piece[0])[0].x + (piece[0])[0].width*2:
        can_rotate = False
    if can_rotate:
      (piece[0])[0].y += (piece[0])[0].height#moves down 1
      (piece[0])[0].x -= (piece[0])[0].width#moves left 1
      (piece[1])[0].x += (piece[1])[0].width#moves right 1
      (piece[1])[0].y -= (piece[1])[0].height#moves up 1
      (piece[2])[0].x += (piece[2])[0].width#moves right 1
      (piece[2])[0].y -= (piece[2])[0].height#moves up 1
      (piece[3])[0].y -= (piece[3])[0].height#moves up 1
      (piece[3])[0].x -= (piece[3])[0].width#moves left 1
      (piece[4])[0].y -= 2*(piece[4])[0].height#moves up 2
  if rotation == 2:
    piece_row = int(((piece[4])[0].y + (piece[4])[0].height)/10 -1)
    if (piece[4])[0].y + (piece[4])[0].height >= playingField.x:
     modify_up = True
    for block in masterRows[piece_row]:
      if (block)[0].x == (piece[4])[0].x + (piece[4])[0].width:#
        can_rotate = False
    for block in masterRows[piece_row+1]:
      if (block)[0].x == (piece[4])[0].x + (piece[4])[0].width:
        can_rotate = False
    for block in masterRows[piece_row-2]:
      if (block)[0].x == (piece[4])[0].x:
        can_rotate = False
    if can_rotate:
      (piece[0])[0].x += 3*(piece[0])[0].width#moves right 3
      (piece[0])[0].y += (piece[0])[0].height#moves down 1
      (piece[1])[0].x += (piece[1])[0].width#moves right 1
      (piece[1])[0].y += (piece[1])[0].height#moves down 1
      (piece[2])[0].y += (piece[2])[0].height#moves down 1
      (piece[2])[0].x -= (piece[2])[0].width#moves left 1 
      (piece[3])[0].x += (piece[3])[0].width
      (piece[3])[0].y -= (piece[3])[0].height
      (piece[4])[0].y -= 2*(piece[4])[0].height
#FINISH HERE ###################################################################################################################################################################
  if rotation == 3:
    modify_left = False
    modify_right = False
    can_rotate = True
    piece_row = int(((piece[4])[0].y + (piece[4])[0].height)/10 -1)
    if (piece[2])[0].x == playingField.x:
      can_rotate = False
    if (piece[2])[0].x + (piece[2])[0].width <= playingField.x + playingField.width:
      can_rotate = False
    for block in masterRows[piece_row]:
      if (block)[0].x == (piece[2])[0].x + 2*(piece[2])[0].width:
        can_rotate = False
    for block in masterRows[piece_row+1]:
      if (block)[0].x == (piece[2])[0].x:
        can_rotate = False
    for block in masterRows[piece_row+1]:
      if (block)[0].x == (piece[2])[0].x - (piece[2])[0].width:
        can_rotate = False
    if can_rotate:
      (piece[0])[0].y -= (piece[0])[0].height#moves up 1
      (piece[0])[0].x -= (piece[0])[0].width#moves left 1
      (piece[1])[0].y += (piece[1])[0].height#moves down 1
      (piece[1])[0].x -= (piece[1])[0].width#moves left 1
      (piece[2])[0].y += (piece[2])[0].height#moves down 1
      (piece[2])[0].x -= (piece[2])[0].width#moves left 1
      (piece[3])[0].x += (piece[3])[0].width#moves right 1
      (piece[3])[0].y += (piece[3])[0].height#moves down 1
      (piece[4])[0].x += 2*(piece[4])[0].width#moves right 2
      (piece[4])[0].y += 2*(piece[4])[0].height#moves down 2

    

  if rotation == 4:
    modify_left = False
    modify_right = False
    modify_up = False
    can_rotate = True
    piece_row = int(((piece[4])[0].y + (piece[4])[0].height)/10 -1)
    if (piece[0])[0].y + 2*(piece[0])[0].height == playingField.height:
      modify_up = False
    for block in masterRows[piece_row]:
      if (block)[0].x == (piece[0])[0].x - (piece[0])[0].width:
        can_rotate = False
    for block in masterRows[piece_row-1]:
      if (block)[0].x == (piece[0])[0].x:
        can_rotate = False
    if piece_row <=47:
      for block in masterRows[piece_row+2]:
        if (block)[0].y == (piece[0])[0].y:
          can_rotate = False
    else: 
      can_rotate = False
    if can_rotate:
      (piece[0])[0].y -= (piece[0])[0].height#moves up 1
      (piece[0])[0].x -= (piece[0])[0].width#moves left 1
      (piece[1])[0].x -= (piece[1])[0].width#moves left 1
      (piece[1])[0].y -= (piece[1])[0].height#moves up 1
      (piece[2])[0].y -= (piece[2])[0].height#moves up 1
      (piece[2])[0].x += (piece[2])[0].width#moves right 1
      (piece[3])[0].y += (piece[3])[0].height#moves down 1
      (piece[3])[0].x -= (piece[3])[0].width#moves left 1
      (piece[4])[0].y += 2*(piece[4])[0].height#moves down 2
      (piece[4])[0].x -= 2*(piece[4])[0].width#moves left 2




def small_L(piece, masterRows, playingField):
  '''
    called when small L piece is rotated 

  parameters 
  ----------
  piece - list of the blocks that make up the Z piece 
  masterRows - a list of all the blocks on screen 
  playingField - pygame rectangle 
  '''
  #[1]     [1 3]   [1 3]    [3]   [3]  
  #[2 3]   [2]       [2]  [1 2]   [1 2]   



  #[1,3]        
  #[2]X    if 2 cannot go to the right, check if one can go to the left, and if it can, then move all three pieces one to the left 
  #  
  can_rotate = True
  modified_rotation = False
  piece_row = int(((piece[1])[0].y + (piece[1])[0].height)/10 -1) #determines the row that block 2 is in 
  if (piece[0])[0].y < (piece[1])[0].y: #rotation 1, 2, or 3 
    if (piece[2])[0].x > (piece[1])[0].x:#rotation 1 or 2 
      if (piece[0])[0].y < (piece[2])[0].y:#rotation 1
        for block in masterRows[piece_row -1]:
          if (block)[0].x == (piece[0])[0].x + (piece[0])[0].width :#cannot rotate as it is, but if may be able to rotate if it is one block lower
            for block in masterRows[piece_row +1]: #this will check if the spot below is available 
              if (block)[0].x == (piece[1])[0].x:
                can_rotate = False
            if can_rotate:
              for block in piece:
                (block)[0].y += (block)[0].height
            break

        if can_rotate:
          (piece[2])[0].y -= (piece[2])[0].height
        
      else: #rotation 2
        for block in masterRows[piece_row]:
          if (block)[0].x == (piece[1])[0].x + (piece[1])[0].width:
            for block in masterRows[piece_row -1]:
              if (block)[0].x == (piece[0])[0].x - (piece[0])[0].width:
                can_rotate = False
            if can_rotate:
              for block in piece:
                (block)[0].x -=(block)[0].width
            break

        if can_rotate:
          (piece[1])[0].x += (piece[1])[0].width
          

    else: #rotation 3 
      for block in masterRows[piece_row]:
        if (block)[0].x == (piece[1])[0].x - (piece[1])[0].width:
          for block in masterRows[piece_row -1]:
            if (block)[0].x == (piece[2])[0].x:
              can_rotate = False
          if can_rotate:
            for block in piece:
              (block)[0].y -=(block)[0].width
          break

      if can_rotate:
        (piece[0])[0].y += (piece[0])[0].height

       

  else: #rotation 4 
    for block in masterRows[piece_row-1]:
      if (block)[0].x == (piece[2])[0].x -(piece[2])[0].width:
        for block in masterRows[piece_row-1]:
          if (block)[0].x == (piece[2])[0].x:
            can_rotate = False
          if can_rotate:
            for block in piece:
              (block)[0].x -=(block)[0].width
          break

    if can_rotate:
      (piece[0])[0].y -= (piece[0])[0].height
      (piece[1])[0].x -= (piece[1])[0].width
      (piece[2])[0].y += (piece[2])[0].height



def rotation_short_stick(piece, masterRows, playingField):
  can_rotate = True
  modified_rotate_right = False 
  modified_rotate_left = False
  if (piece[0])[0].x == (piece[2])[0].x:
      #the blocks look like:
      #[0]
      #[1]    ->  [0, 1, 2]
      #[2]
    piece_row =int(((piece[1])[0].y + (piece[1])[0].height)/10 ) #this is the row that the middle piece(2) is in, and where 1 and 3 will move to
    if (piece[1])[0].x == playingField.x:
      modified_rotate_right = True 

    for block in masterRows[piece_row]:  
      if (block)[0].x == (piece[1])[0].x - (piece[1])[0].width :  #checks if theres a block to the left of the piece 
        modified_rotate_right = True#this will not be able to rotate normally, but we may be able to rotate it by shifting it over to the right one block
    if modified_rotate_right: #this will check to see if the piece will be able to shift right and rotate
      for also_block in masterRows[piece_row]:
        if (also_block)[0].x == (piece[1])[0].x + (piece[1])[0].width or (block)[0].x == (piece[1])[0].x + (piece[1])[0].width*2: #this checks that the new spots where pieces will move to are free
          can_rotate = False
          break
      if can_rotate:#if the spots are open, then we will shift everything over to the right 
        for block in piece:
            (block)[0].x += (block)[0].width  
            
    if can_rotate: #if the left side is good, or it has shifted to be good, we need to confirm the right side 
      if (piece[1])[0].x + (piece[1])[0].width == playingField.x + playingField.width:    
        modified_rotate_left = True#means that it can't rotate normal, since it will go outside the playing field, but you might be able to if the piece shifts left one 

      for block in masterRows[piece_row]:  
        if (block)[0].x == (piece[1])[0].x + (piece[1])[0].width:  #checks if theres a block to the right of the piece or if the block is on the righy edge
          modified_rotate_left = True
          #this will not be able to rotate normally, but we may be able to rotate it by shifting it over to the left one block
      if modified_rotate_left:
        for also_block in masterRows[piece_row]:
          if (also_block)[0].x == (piece[1])[0].x + (piece[1])[0].width or (block)[0].x == (piece[1])[0].x + (piece[1])[0].width*2:
            can_rotate = False
            break
        if can_rotate:
          for block in piece:
              (block)[0].x -= (block)[0].width    
      if can_rotate:
        (piece[0])[0].y += (piece[0])[0].height
        (piece[0])[0].x -= (piece[0])[0].width        
        (piece[2])[0].y -= (piece[2])[0].height
        (piece[2])[0].x += (piece[2])[0].width  
        # ends with [0, 1, 2]  

  else: #the block is [0, 1, 2] this is simple. all we have to do is check is the block above and below are free, and that it isnt going below the playing field 
    piece_row =int(((piece[1])[0].y + (piece[1])[0].height)/10 -1) #this is the row that the middle piece(2) is in. We will check the row above and below it

    for block in masterRows[piece_row-1]:#checks if the spot above is free
      if (block)[0].x == (piece[1])[0].x:
        can_rotate = False
    if can_rotate:
      if  (piece[1])[0].y == playingField.height - (piece[1])[0].height:#this means it is at the bottom level, so we will need to shift everything up 1 
        for block in masterRows[piece_row - 2]:
          if (block)[0].x == (piece[1])[0].x:
            can_rotate = False
        if can_rotate:
          for block in piece:
            (block)[0].y -=( block)[0].height

        if piece_row != 50:
            for block in masterRows[piece_row]:# I a plus one idsk if it will break it so check 
              if (block)[0].x == (piece[1])[0].x:
                can_rotate = False
    
    if can_rotate : #m

      (piece[0])[0].y -= (piece[0])[0].height # moves it up 
      (piece[0])[0].x += (piece[0])[0].width # moves it right 
      (piece[2])[0].y += (piece[2])[0].height # moves it down 
      (piece[2])[0].x -= (piece[2])[0].width # moves it right 





     

