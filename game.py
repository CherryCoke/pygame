import pygame, player, os, sys, fileinput, random #@UnusedImport #@UnresolvedImport

#Setting Version Number
global version_number
version_number = "0.0.9"

class tile(pygame.sprite.Sprite):
    """
    Takes and loads a sprite from a spritesheet
    """
    
    def __init__(self, sheetx, sheety, width, height, blitx, blity, sheet):
        
        #Calling the parent (Sprite) class constructor
        pygame.sprite.Sprite.__init__(self)
        
        """
        Sheetx/y are the coords on the spritesheet
        width/height are the height of the spritesheet cells
        blitx/y are where the image will be put on screen
        """
        
        self.sheetx = sheetx
        self.sheety = sheety
        self.width = width
        self.height = height
        self.blitx = blitx
        self.blity = blity
        self.sheet = sheet
        
        #Defining which spritesheet will be used (for now)
        tile_sheet = pygame.image.load('assets/spritesheets/' + str(self.sheet)+ ".png")

        
        #Getting specific image
        tile_sheet.set_clip(pygame.Rect(self.sheetx, self.sheety,
                                   self.width, self.height))
        #Setting sprite to that image
        self.image = tile_sheet.subsurface(tile_sheet.get_clip())
        
        #Getting the size of the image
        self.rect = self.image.get_rect()
        
        #Chooseing where to blit the image
        self.rect.x = blitx
        self.rect.y = blity
    
    def loadTiles(self):
        """Assigns sprites to go with each character from the level.dat files"""
        x, y = self.blitx, self.blity
        for line in fileinput.input(os.path.join\
        ("assets", "levels", "level" + str(currentLevel) + ".dat")): #@UndefinedVariable
            for currentTile in line:
                if currentTile == "1":
                    newTile = tile(253, 253,  self.width, self.height, x, y, "tileSheet")
                    level_tiles.add(newTile)
                elif currentTile == "4":
                    newTile = tile(26, 0, self.width, self.height, x, y, "tileSheet")
                    level_tiles.add(newTile)
                elif currentTile == "3":
                    newTile = tile(26, 0, self.width, self.height, x, y, "tileSheet")
                    level_tiles.add(newTile)
                elif currentTile == "*":
                    newTile = tile(26, 0, self.width, self.height, x, y, "tileSheet")
                    level_walls.add(newTile)
                    
                x += 22 #Edit this x
                   
            x = 0 #Don't touch this x; used to reset tiles to next line/row
            y += 22 #And this Y to change space width and height between tiles respectively

def controls():
    
    player_x = "x = " + str(player.rect.x) #@UndefinedVariable
    player_y = "y = " + str(player.rect.y) #@UndefinedVariable
    
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                """If the red 'x' is hit, end for loop and close pygame_cal"""
                pygame.quit()
                sys.exit()
        
            #Next two sections of events handle player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5,0) #@UndefinedVariable
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5,0) #@UndefinedVariable
                if event.key == pygame.K_UP:
                    player.changespeed(0,-5) #@UndefinedVariable
                if event.key == pygame.K_DOWN:
                    player.changespeed(0,5) #@UndefinedVariable
                     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5,0) #@UndefinedVariable
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5,0) #@UndefinedVariable
                if event.key == pygame.K_UP:
                    player.changespeed(0,5) #@UndefinedVariable
                if event.key == pygame.K_DOWN:
                    player.changespeed(0,-5)  #@UndefinedVariable
                if event.key == pygame.K_a:
                    print (player_x, player_y)
       
#Setting currentLevel for "level#.dat" # is replaced with the value here
global currentLevel
currentLevel = 1
 
#Sets a group (or list) of sprites
level_tiles = pygame.sprite.Group()
level_walls = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

#Creating the player sprite and adding it to its own group
player = player.Player(24,24)
player_sprite.add(player)

#Creating clock to keep track of ticks and (later) fps
clock = pygame.time.Clock()

def main():
    """Main Menu"""
    
    #Keeps track of the current level
    global currentLevel
    global version_number
    #Setting the width and height of the screen before creating the 
    #screen surface
    SCREEN_X = 922
    SCREEN_Y = 700
    SIZE = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(SIZE)
    
    #Setting the text to be displayed at the top of the pygame_cal window
    pygame.display.set_caption("Main Menu - " + version_number)
    backgroundnum = random.randint(1, 1)
    
    # Loading and position graphics
        #Background-Related
    background_image = pygame.image.load("assets/images/background" +  
                        str(backgroundnum) + ".jpg").convert()
    background_position = [0,0]
        #Button-Related
    button_image = pygame.image.load("assets/images/button.png")
    button_size = 225
    extra_space = 80 #Leaves extra space at the top for main menu/welcome/whatever
    button_one_position = [SCREEN_X/4 - button_size/4, SCREEN_Y/4 
                           + button_size/4 + extra_space]
    button_two_position  = [SCREEN_X/4 * 2 + button_size/4, SCREEN_Y/4 
                            + button_size/4 + extra_space]
    button_three_position = [SCREEN_X/4 - button_size /4, SCREEN_Y/4 
                             + button_size + extra_space]
    button_four_position = [SCREEN_X/4 * 2 + button_size/4, SCREEN_Y/4 
                            + button_size + extra_space]
    
    done = False
    while not done:
        
        #Retrieves the coordinates of the mouse pointer/cursor
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                """If the red 'x' is hit, end for loop and close pygame_cal"""
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #For now clicking gives you the mouse coordinates
                print ("Mouse clicked")
                print ("x coord: " + str(x))
                print ("y coord: " + str(y))
                print (" ")
                
                if x >= 176 and x <= 398 and y >= 312 and y <= 370:
                    levelOne()
                    pygame.quit()
        
        #Blitting images onto screen
        screen.blit(background_image, background_position)
        screen.blit(button_image, button_one_position)
        screen.blit(button_image, button_two_position)
        screen.blit(button_image, button_three_position)
        screen.blit(button_image, button_four_position)
    
        #Updates/applies changes the game window/screen surface
        pygame.display.flip()
    
        #Setting FPS for the games
        clock.tick(60)

def levelOne():
    
    #Keeps track of current Level
    global currentLevel
    
    #Defining the color to be used "behind" the tiles
    BACKGROUNDCOLOR = (255,255,255)
    
    #Creating object to test tiles                
    tileTest = tile(0, 0, 23 , 23, 0, 0, "tileSheet") 
    tileTest.loadTiles() #Loading information for tiles/walls
    
    #Setting the width and height of the the current level 
    SCREEN_X = 500
    SCREEN_Y = 500
    SIZE = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(SIZE)
    
    #Setting the text to be displayed at the top of the pygame_cal window
    pygame.display.set_caption("Level One Title")


    done = False
    while not done:
    
        controls()
        
        #Setting the background of the screen (as white)
        screen.fill(BACKGROUNDCOLOR)
    
        #Setting which tiles will be the player's walls
        player.move(level_walls)
        
        """Actually drawing the walls and tiles on-screen.
        Unlike the player, they do not need to be updated because
        they are static and do not change throught the entirety of 
        a level """
        level_tiles.draw(screen) 
        level_walls.draw(screen)
    
        #Drawing and updating the player
        player_sprite.draw(screen)
        player_sprite.update() #Update is required to "move"
    
  
        #Updates/applies changes the game window/screen surface
        pygame.display.flip()
        
        #Victory conditions for level
        if player.rect.x >= 399 and player.rect.y >= 169:
            print ("yay")
            
            #Empty all levels/tile groups from this level
            #Then remove them from the screen/game surface
            level_tiles.empty()
            level_tiles.remove()
            level_walls.empty()
            level_walls.remove()
            pygame.display.flip() #Update change
            
            #Sets the next level
            currentLevel = 2
            
            #Loads the next level and quits/exits current one
            levelTwo()
            pygame.quit()
            
    
        #Setting FPS for the games
        clock.tick(60)
     
def levelTwo():

    global currentLevel
    
    #Defining the color white to be used later
    BACKGROUNDCOLOR = (0, 0, 255)
    
    player.rect.x = 24
    player.rect.y = 24
    
    #Creating object     to test tiles 
    print (currentLevel)             
    tileTest = tile(0, 0, 23 , 23, 0, 0, "tileSheet") 
    tileTest.loadTiles() #Loading information for tiles/walls

    #Setting the width and height of the screen before creating the 
    #screen surface
    SCREEN_X = 500
    SCREEN_Y = 500
    SIZE = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(SIZE)
    
    #Setting the text to be displayed at the top of the pygame_cal window
    pygame.display.set_caption("Level Two Title")


    done = False
    while not done:
    
        controls()
        
        screen.fill(BACKGROUNDCOLOR)
        
        player.move(level_walls)
        level_tiles.draw(screen) 
        level_walls.draw(screen)
        player_sprite.draw(screen)
        player_sprite.update()
    
        pygame.display.flip()
        
        #Victory conditions for level
        if player.rect.x >= 399 and player.rect.y >= 169:
            print ("yay")
            
            #Empty all levels/tile groups from this level
            #Then remove them from the screen/game surface
            level_tiles.empty()
            level_tiles.remove()
            level_walls.empty()
            level_walls.remove()
            pygame.display.flip() #Update change
            
            #Sets the next level
            currentLevel = 3
            
            #Loads the next level and quits/exits current one
            levelThree()
            pygame.quit()
            
        clock.tick(60)

# Call the main function, start up the game
if __name__ == "__main__":
    main()