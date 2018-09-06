from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
#Colors

#Yellow path
Y = [255, 255, 0]
#black space
B = [0, 0, 0]
#blue piBel
pix = [0,0,248]
#finish line in red
R = [248, 0, 0]


#Paths for the different levels. Use: p1, p2, ...

#path for the first level
p1 = [
    Y,Y,Y,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,B,B,
    B,B,B,Y,Y,Y,Y,R,
    B,B,B,B,Y,Y,Y,R,
    B,B,B,B,B,Y,Y,R,
    B,B,B,B,B,B,B,B
    ]

#path for the second level
p2 = [
    Y,Y,Y,Y,Y,Y,B,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,B,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,Y,Y,Y,Y,B,
    B,B,B,R,R,R,R,B
    ]

#Different Levels

#start with level one being true
level1 = True

#all other levels should start as being false
level2 = False
level3 = False

#function to move piBel across the maze
def move_piBel(path, pix, black, finish, level):
    
    cB = 0
    cY = 0
    while True:
        sense.set_piBels(path)
        sense.set_piBel(cB, cY, pix)
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        
        if 280 < pitch < 320 and cB < 7:
            cB += 1
            
        if 45 < pitch < 90 and cB > 0:
            cB = cB - 1
            
        if 40 < roll < 90 and cY < 7:
            cY += 1
            
        if 270 < roll < 315 and cY > 0:
            cY -= 1
       
        current = sense.get_piBel(cB, cY)
     
        if current == black:
            cB = 0
            cY = 0
       
        if current == finish:
            sense.show_message(level)
            return False
        sleep(0.3)   
    

sense.show_message("LEVEL 1")
while level1 is True:

    level1 = move_piBel(p1, pix, B, R, "LEVEL 2")
    level2 = True
    
while level2 is True:
  
    level2 = move_piBel(p2, pix, B, R, "LEVEL 3")
    level3 = True
    
sense.show_message("You Did It")
    
    
    
    
    
   
    
    
    


