app.background = "White"
### PROJECT SCORPOS GAME ENGINE IN CMU
minigame = 1

if minigame == 0:
    defaultText = Label("You should not be seeing this", 200, 200, size = 15)

if minigame == 1:
    app.background = "Lime"
    ### UI
    TextHealth = Label("Health: ",200,20, fill = "Red", border = "darkRed", borderWidth = 0.55, size = 20)
    Health = Label(100,245,20, fill = "Red", border = "darkRed", borderWidth = 0.55, size = 20)
    MovementInfo = Label("USE (WASD) TO MOVE",220,60, fill = "Grey", border = "darkGrey", borderWidth = 0.55, size = 10, opacity = 100)
    
    ### WORLD PROPERTIES (Used for setting up a map for a two dimensional world)
    
    Map = Group(
        Rect(-900000,140,900400,120, fill = 'darkBlue'),
        Rect(-900000,150,900400,100, fill = 'red'),
        Rect(0,190,400,20, fill = 'red')
        )
        
    Map.centerX = Map.centerX
    
    ### PLAYER PROPERTIES (Used for creating the player and the properties used)
    Player = Group(
        Rect(21.5,200,7.5,50, fill = 'black'),
        Rect(20,200,10,10, fill = 'white'),
    )
    
    Player.Jumping = False
    Player.jumpHeight = 40
    
    ### OBJECT PROPERTIES (Used for creating an environment and objects)
    
    MapEntities = Group(
        Rect(50,0,10,400, fill = 'aqua'),
        Rect(335,0,10,400, fill = 'aqua'),
        Rect(53.5,0,2.5,400, fill = 'Blue'),
        Rect(338.5,0,2.5,400, fill = 'Blue'),
        Star(100,250,15,10, fill = 'Tan'),
        Star(140,155,15,10, fill = 'Tan'),
        Star(0,155,15,10, fill = 'Tan'),
        Star(0,170,15,10, fill = 'Tan'),
        Star(0,185,15,10, fill = 'Tan'),
        Star(0,200,15,10, fill = 'Tan'),
        Star(0,215,15,10, fill = 'Tan'),
        Star(0,230,15,10, fill = 'Tan'),
        Star(0,245,15,10, fill = 'Tan'),
        Star(180,250,15,10, fill = 'Tan'),
        Star(220,155,15,10, fill = 'Tan'),
        Star(260,250,15,10, fill = 'Tan'),
        Star(300,155,15,10, fill = 'Tan'),
        Rect(400,170,40,60, fill = 'Gold', border = "Black", borderWidth = 2.5),
        Star(200,225,5,8, fill = 'Aqua'),
        Star(70,225,5,8, fill = 'Aqua'),
        Star(40,180,5,8, fill = 'Aqua')
        )
        
    ### KEYBINDS (Used for getting keyboard input)
    
    def onKeyPress(key):
        #Move Left
        if key == "d":
            MovementInfo.opacity = 0
            Player.centerX = Player.centerX + 10
            MapEntities.centerX = MapEntities.centerX - 10
            if Player.centerX >= 390:
                Player.centerX = 10
                MapEntities.centerX = MapEntities.centerX - 400
            
        #Move Right
        if key == "a":
            MovementInfo.opacity = 0
            Player.centerX = Player.centerX - 10
            MapEntities.centerX = MapEntities.centerX + 10
            
            if Player.centerX <= 0:
                Player.centerX = 390
                MapEntities.centerX = MapEntities.centerX + 400
        #Jump
        if key == "space" or key == "w" or key == "W":
            MovementInfo.opacity = 0
            Player.Jumping = True
            
            
    ### TIME PACING
                
    def onStep():
        #Player Jump/Gravity System
        if Player.centerY <= 220 and Player.Jumping == False:
            Player.centerY = Player.centerY + 5
        
        if Player.Jumping == True:
            Player.centerY = Player.centerY - 5
            
        if Player.centerY <= 220 - Player.jumpHeight:
            Player.Jumping = False
        #Enemy System (Note: Be careful with changing star colors or it could be detected as an enemy!)
        for Star in MapEntities.children:
            if Star.hitsShape(Player) and Star.fill == "Tan":
                MapEntities.remove(Star)
                if Health.value <= 100 and Health.value > 0:
                    Health.value = Health.value - 25
                if Health.value < 0:
                    Health.value = 0
                if Health.value <= 0:
                    Label(":( You Died :(", 200, 200, size = 20, fill = 'Maroon', bold = True)
                    app.stop()
            if Star.hitsShape(Player) and Star.fill == "Aqua":
                    #MapEntities.remove(Star2) (Used previously to destroy the stars but was changed)
                if Health.value <= 100 and Health.value > 0:
                    Health.value = Health.value - 1
                if Health.value < 0:
                    Health.value = 0
                if Health.value <= 0:
                    Label(":( You Died :(", 200, 200, size = 20, fill = 'Maroon', bold = True)
                    app.stop()
                        
            if Star.fill == "Aqua":
                if Star.centerX <= 200 and Star.centerX >=0:
                    Star.centerX = Star.centerX - 1
                if Star.centerX <= 0:
                    Star.centerX = Star.centerX + 200
                
        
                
        #Winning System
        for Rect in MapEntities.children:
            if Rect.hitsShape(Player) and Rect.fill == "Gold":
                Player.fill = 'Aqua'
                MapEntities.remove(Star)
                Label("!You Win!", 200, 200, size = 20, fill = "Green", bold = True)
                app.stop()
                
if minigame == 2: 
    app.background = fill = gradient("darkBlue", "aqua", "aqua","lightBlue", "Yellow", start = "bottom")
    
    app.PipeX = randrange(220,300)
    
    PipeDownward = Rect(app.PipeX,250,120,150,fill = 'lime')
    PipeDownward2 = Rect(app.PipeX,0,120,150,fill = 'lime')
    
    Bird = Circle(0,200,10, fill = 'Yellow')
    Cent = Label("C", 200, 10, size = 10)
    Cent2 = Label("|", 200, 10, size = 12)
    
    Points = Label(0, 380, 20, size = 20)
    Title = Label("Flappy Coin", 100, 20, size = 20)
    Bird.DefaultSpeed = 4.5
    Bird.Gravity = 1
    Jump = 40
    
    def onStep():
        Cent.centerX = Bird.centerX + 5
        Cent.centerY = Bird.centerY
        Cent2.centerX = Bird.centerX + 5
        Cent2.centerY = Bird.centerY - 1
        Bird.Gravity = Bird.Gravity + 0.025
        Bird.centerX = Bird.centerX + Bird.DefaultSpeed
        Bird.centerY = Bird.centerY + Bird.Gravity
        if Bird.centerX > 390:
            Bird.centerX = 0
            Bird.centerY = 200
            Bird.Gravity = 1
            Points.value = Points.value + 1
            Bird.DefaultSpeed = Bird.DefaultSpeed + 0.1
            PipeDownward.centerX = randrange(220,300)
            PipeDownward2.centerX = PipeDownward.centerX
        if(Bird.hitsShape(PipeDownward) == True):
            Bird.centerX = 0
            Bird.centerY = 200
            Points.value = 0
            Bird.Gravity = 1.2
            Bird.DefaultSpeed = 4.5
            PipeDownward.centerX = randrange(220,300)
            PipeDownward2.centerX = PipeDownward.centerX
        
        if(Bird.hitsShape(PipeDownward2) == True):
            Bird.centerX = 0
            Bird.centerY = 200
            Points.value = 0
            Bird.Gravity = 1.2
            Bird.DefaultSpeed = 4.5
            PipeDownward.centerX = randrange(220,300)
            PipeDownward2.centerX = PipeDownward.centerX
            
    def onKeyPress(key):
        if (key == "space"):
            Bird.centerY = Bird.centerY - Jump
            

        
        
    
