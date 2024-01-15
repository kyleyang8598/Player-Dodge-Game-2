'''
Author: Kyle Yang
Creation Date: 5/15/22
Last Modified: 5/20/22
Project Description: This is a game where you have to avoid all of the obstacles
that are thrown at you like fireballs, cars, rockets, and cannons for 20 rounds.
There are 10 different types of obstacles including 5 different fireball colors,
2 different car and rocket sizes, and cannons with lots of animation and colors.
Stormy weather will reduce visibility while fireflies can help you see at night.
This Creative Project is a combination of the Unit 2 Project and Unit 8 Project.
Instructions: Avoid the obstacles by pressing the arrow keys to move the player.
You can also collect the snowflakes on the screen to gain points for each round.
The player will have to survive for 20 rounds or gain 20 points to win the game.
Credits: Mom Dad
Updates: Add new types of obstacles. Combine the Unit 2 and the Unit 8 Projects.
'''

from cmu_graphics import *

# globals
app.background = rgb(0,250,250)
app.stepsPerSecond = 30

# classes
class GameState(object):
    '''
    Contains methods and properties for the game itself to run.
    '''
    def __init__(self):
        # Creates the properties, labels, and groups for the game state.
        self.mode = 'MENU'
        self.healthLabel = Label('Health:',200,390,visible=False,bold=True,fill='indigo')
        self.pointsLabel = Label('Points:',200,10,visible=False,bold=True,fill='indigo')
        self.roundsLabel = Label('Rounds:',200,200,fill='darkRed',size=30,visible=False,bold=True)
        self.pointsScored = Label('Points Scored:',200,140,visible=False,bold=True)
        self.roundsLasted = Label('Rounds Lasted:',200,160,visible=False,bold=True)
        self.highestScoreLabel = Label('Highest Score:',200,180,visible=False,bold=True)
        self.highestScore = 0
        self.highestRoundLabel = Label('Highest Round:',200,200,visible=False,bold=True)
        self.highestRound = 0
        self.winsLabel = Label('Wins:',200,220,visible=False,bold=True)
        self.wins = 0
        self.lossesLabel = Label('Losses:',200,240,visible=False,bold=True)
        self.losses = 0
        self.title = Label('Player Dodge Game',200,100,size=30,bold=True)
        self.start = Group(Rect(150,275,100,50),
                    Label('Start',200,300,fill='white',size=30,bold=True))
        self.again = Group(Rect(100,275,200,50),
                    Label('Play Again',200,300,fill='white',size=30,bold=True),visible=False)
        self.fireballs = Group()
        self.cars = Group()
        self.rockets = Group()
        self.cannons = Group()
        self.snowflakes = Group()
        self.landscape = Group()
        self.clouds = Group()
        self.lightning = Group()
        self.fireflies = Group()
    
    def summonObstacle(self):
        # Summons a random obstacle based on the number of rounds.
        self.roundsLabel.visible = False
        random = randrange(1,self.rounds+1)
        if random <= 3:
            fireball = Fireball()
        if random == 4 or random == 8:
            car = Car()
        if random == 5 or random == 9:
            rocket = Rocket()
        if random == 6 or random >= 10:
            fireball = Fireball()
        if random == 7:
            cannon = Cannon()
        if random == randrange(1,self.rounds+1):
            snowflake = Snowflake()
        self.stepsPerObstacle = 0
        self.obstaclesSummoned += 1
    
    def nextRound(self):
        # Goes to the next round of the player dodge game.
        self.stepsPerObstacle = 0
        self.obstaclesSummoned = 0
        self.rounds += 1
        self.roundsLabel.value = 'Round ' + str(self.rounds)
        self.roundsLabel.size = 100
        self.roundsLabel.visible = True
    
    def showStats(self):
        # Shows your stats after you win or lose the game.
        app.background = rgb(0,250,250)
        self.mode = 'END'
        self.pointsLabel.visible = False
        self.healthLabel.visible = False
        app.player.drawing.visible = False
        self.title.visible = True
        self.start.visible = True
        self.again.visible = True
        self.pointsScored.value = 'Points Scored: ' + str(self.points)
        self.roundsLasted.value = 'Rounds Lasted: ' + str(self.rounds)
        self.pointsScored.visible = True
        self.roundsLasted.visible = True
        if self.points > self.highestScore:
            self.highestScore = self.points
        if self.rounds > self.highestRound:
            self.highestRound = self.rounds
        self.highestScoreLabel.value = 'Highest Score: ' + str(self.highestScore)
        self.highestScoreLabel.visible = True
        self.highestRoundLabel.value = 'Highest Round: ' + str(self.highestRound)
        self.highestRoundLabel.visible = True
        self.winsLabel.value = 'Wins: ' + str(self.wins)
        self.winsLabel.visible = True
        self.lossesLabel.value = 'Losses: ' + str(self.losses)
        self.lossesLabel.visible = True
        for cannon in self.cannons:
            cannon.body.visible = False
            cannon.ball.visible = False
            cannon.fire.visible = False
        self.fireballs.clear()
        self.cars.clear()
        self.rockets.clear()
        self.cannons.clear()
        self.snowflakes.clear()
        self.landscape.clear()
        self.clouds.clear()
        self.lightning.clear()
        self.fireflies.clear()
    
    def startGame(self):
        # Starts the player dodge game.
        self.dayLightCycle = 0
        self.rounds = 0
        self.stepsPerObstacle = 0
        self.obstaclesSummoned = 0
        self.points = 0
        self.pointsLabel.value = 'Points: ' + str(self.points)
        self.pointsLabel.visible = True
        self.health = 100
        self.healthLabel.value = 'Health: ' + str(self.health)
        self.healthLabel.visible = True
        app.player.drawing.centerX = 200
        app.player.drawing.centerY = 200
        app.player.drawing.visible = True
        self.title.visible = False
        self.start.visible = False
        self.again.visible = False
        self.pointsScored.visible = False
        self.roundsLasted.visible = False
        self.highestScoreLabel.visible = False
        self.highestRoundLabel.visible = False
        self.winsLabel.visible = False
        self.lossesLabel.visible = False
        self.luminescence = 0
        self.dayLightCycle = 0
        self.lightningRate = 0
        self.stormActivate = False
        self.makeLandscape()
        self.makeClouds()
        self.landscape.toBack()
        self.clouds.toBack()
        self.lightning.toBack()
        self.fireflies.toBack()
        app.game.landscape.opacity = 100
        app.game.clouds.opacity = 100
        app.player.drawing.opacity = 100
        app.game.fireballs.opacity = 100
        app.game.cars.opacity = 100
        app.game.rockets.opacity = 100
        app.game.cannons.opacity = 100
        app.game.snowflakes.opacity = 100
        app.game.fireflies.opacity = 100
    
    def makeLandscape(self):
        # Designs new landscape.
        for i in range(1, 6):
            startY = 100 + i * 50
            # Gets a color that is in the landscape's monochromatic scheme.
            color = app.game.getMonochromaticColor(rgb(0,250,0), 1 - i / 10)
            layer = Polygon(0, 410, 0, startY, fill=color)
            y = startY
            for i in range(50):
                x = 10 * i
                y += randrange(-5, 5)
                layer.addPoint(x, y)
            layer.addPoint(405, 410)
            app.game.landscape.add(layer)
    
    def makeClouds(self):
        # Generates more clouds.
        for i in range(3):
            cloud = Oval(i*100+50,25,150,50,fill='white')
            app.game.clouds.add(cloud)
    
    def modifyClouds(self,length,width,color):
        # Changes clouds' color and size.
        for cloud in app.game.clouds:
            cloud.width=width
            cloud.length=length
            cloud.fill=color
    
    def drawLightning(self,startX):
        # Initiates a new lightning bolt.
        if startX <= 300:
            branchNumber = randrange(5,10)
            for i in range(branchNumber):
                x1 = startX
                y1 = 50
                branchLength = randrange(10,20)
                for i in range(branchLength):
                    x2 = x1 + randrange(-15,15)
                    y2 = y1 + randrange(10,20)
                    branch = Line(x1,y1,x2,y2,fill=rgb(245,225,205),lineWidth=5)
                    x1 = x2
                    y1 = y2
                    app.game.lightning.add(branch)
    
    def makeFireflies(self):
        # Makes 30 fireflies in the fireflies group.
        for i in range(30):
            firefly = Group(Line(195,165,190,155,fill='green'),
                            Line(205,165,210,155,fill='green'),
                            Circle(190,150,5,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                            Circle(210,150,5,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                            Circle(180,185,15,fill=gradient('gray','white',start='right')),
                            Circle(220,185,15,fill=gradient('gray','white',start='left')),
                            Oval(180,185,20,10,fill='gray'),
                            Oval(220,185,20,10,fill='gray'),
                            Circle(200,200,15,fill=gradient('lightYellow','yellow',start='bottom'),border='yellow'),
                            Circle(200,175,15,fill=gradient('green','lightGreen',start='bottom'),border='green'),
                            Circle(190,175,5,fill='white'),
                            Circle(210,175,5,fill='white'),
                            Circle(190,175,3,fill='black'),
                            Circle(210,175,3,fill='black'))
            firefly.luminescence = randrange(0,1000)
            firefly.centerX = randrange(0,400)
            firefly.centerY = randrange(200,400)
            app.game.fireflies.add(firefly)
    
    def getAverage(self):
        # Returns the average luminescence of the fireflies. They are stored in the fireflies group.
        total = 0
        for firefly in app.game.fireflies:
            total += firefly.luminescence
        average = total / len(app.game.fireflies)
        return average
    
    def normalize(self,firefly,avg):
        # The factor affects how quickly the fireflies synchronize.
        factor = 10
        # Gets how far the luminescence is from average, then adds the factor to luminescence value.
        app.game.luminescence += (avg - app.game.luminescence)
        if app.game.luminescence > firefly.luminescence:
                firefly.luminescence += factor
    
    def getMonochromaticColor(self,color, ratio):
        # Gets a new color in the same monochromatic scheme as the provided color.
        newColor = rgb(int(color.red * ratio),
                       int(color.green * ratio),
                       int(color.blue * ratio))
        return newColor

class Player(object):
    '''
    Contains properties for the player object that is called.
    '''
    def __init__(self):
        # Creates properties for the player.
        self.drawing = Group(Circle(200,200,25),
            Circle(200,200,20,fill='white'),
            Line(200,225,200,275,lineWidth=5),
            Line(175,250,200,225,lineWidth=5),
            Line(225,250,200,225,lineWidth=5),
            Line(200,275,175,300,lineWidth=5),
            Line(200,275,225,300,lineWidth=5),
            Circle(190,200,5),
            Circle(210,200,5))
        self.drawing.visible = False
        self.drawing.height /= 2
        self.drawing.width /= 2

class Fireball(object):
    '''
    Contains properties for each fireball object that is called.
    '''
    def __init__(self):
        # Creates properties for the fireball.
        self.colors = ['red','orange','yellow','green','blue']
        self.drawing = Star(randrange(60,340),-20,15,50)
        self.drawing.angle = angleTo(self.drawing.centerX,self.drawing.centerY,app.player.drawing.centerX,app.player.drawing.centerY)
        if app.game.rounds == 1:
            self.drawing.speed = randrange(1,2)
        elif app.game.rounds == 2:
            self.drawing.speed = randrange(1,3)
        elif 2 < app.game.rounds < 6:
            self.drawing.speed = randrange(1,4)
        elif 5 < app.game.rounds < 10:
            self.drawing.speed = randrange(1,5)
        else:
            self.drawing.speed = randrange(1,6)
        self.drawing.fill = self.colors[self.drawing.speed-1]
        app.game.fireballs.add(self.drawing)

class Car(object):
    '''
    Contains properties for each car object that is called.
    '''
    def __init__(self):
        # Creates properties for the car.
        self.drawing = Group(Polygon(25,125,75,75,125,75,175,125,fill='blue'),
                Rect(25,125,200,50,fill='orange'),
                Rect(75,80,50,40),
                Circle(75,175,25,fill='lightGray',border='gray',borderWidth=10),
                Circle(175,175,25,fill='lightGray',border='gray',borderWidth=10))
        if app.game.rounds < 8:
            self.drawing.height /= 4
            self.drawing.width /= 4
        else:
            if randrange(0,2) == 0:
                self.drawing.height /= 3
                self.drawing.width /= 3
            else:
                self.drawing.height /= 4
                self.drawing.width /= 4
        self.drawing.centerX = -50
        self.drawing.centerY = randrange(200,340)
        app.game.cars.add(self.drawing)

class Rocket(object):
    '''
    Contains properties for each rocket object that is called.
    '''
    def __init__(self):
        # Creates properties for the rocket.
        self.drawing = Group(RegularPolygon(200,200,30,3,fill='violet',border='black'),
                    Rect(180,215,40,150,fill='gray',border='black'),
                    Polygon(180,300,180,250,150,300,fill='violet',border='black'),
                    Polygon(220,300,220,250,250,300,fill='violet',border='black'),
                    Polygon(180,365,220,365,220,405,200,385,180,405,fill=gradient('yellow','red')))
        if app.game.rounds < 9:
            self.drawing.height /= 4
            self.drawing.width /= 4
        else:
            if randrange(0,2) == 0:
                self.drawing.height /= 3
                self.drawing.width /= 3
            else:
                self.drawing.height /= 4
                self.drawing.width /= 4
        self.drawing.centerY = 460
        self.drawing.centerX = randrange(60,340)
        app.game.rockets.add(self.drawing)

class Cannon(object):
    '''
    Contains properties for each cannon object that is called.
    '''
    def __init__(self):
        # Creates properties for the cannon.
        self.drawing = Circle(10,220,10,fill='brown')
        self.drawing.body = Group(Oval(20,200,50,30),
                    Oval(40,200,10,30))
        self.drawing.ball = Circle(50,0,15,fill=gradient('white','black','black'),visible=False)
        self.drawing.fire = Polygon(40,170,60,170,55,180,60,190,40,190,fill=gradient('yellow','red'),visible=False)
        self.drawing.centerX = -40
        self.drawing.body.centerX = -30
        self.drawing.centerY = randrange(200,340) + 10
        self.drawing.body.centerY = self.drawing.centerY - 20
        self.drawing.energy = 0
        app.game.cannons.add(self.drawing)

class Snowflake(object):
    '''
    Contains properties for each snowflake object that is called.
    '''
    def __init__(self):
        # Creates properties for the snowflake.
        self.drawing = Star(randrange(60,340),randrange(200,340),10,10,fill='white')
        app.game.snowflakes.add(self.drawing)

def main():
    # This function creates the objects for the game and player.
    app.game = GameState()
    app.player = Player()

main()

def onKeyHold(keys):
    # This function is called every time you hold a key.
    if ('up' in keys) and app.player.drawing.centerY > 200:
        app.player.drawing.centerY -= 10
    if ('down' in keys) and app.player.drawing.centerY < 340:
        app.player.drawing.centerY += 10
    if ('left' in keys) and app.player.drawing.centerX > 60:
        app.player.drawing.centerX -= 10
    if ('right' in keys) and app.player.drawing.centerX < 340:
        app.player.drawing.centerX += 10

def onStep():
    # This function is called for 30 times in a second.
    if app.game.mode == 'START':
        if app.game.stepsPerObstacle % 3 == 0:
            if 200 < app.game.dayLightCycle <= 400:
                app.game.stormActivate = True
                app.game.modifyClouds(100,300,'gray')
                app.background = 'darkBlue'
                app.game.lightning.clear()
                app.game.fireflies.clear()
                app.game.landscape.opacity = 50
                app.player.drawing.opacity = 50
                app.game.fireballs.opacity = 50
                app.game.cars.opacity = 50
                app.game.rockets.opacity = 50
                app.game.cannons.opacity = 50
                app.game.snowflakes.opacity = 50
            if 400 < app.game.dayLightCycle <= 500:
                app.game.stormActivate = False
                app.game.modifyClouds(50,150,'white')
                app.background = rgb(0,250,250)
                app.game.lightning.clear()
                app.game.landscape.opacity = 100
                app.player.drawing.opacity = 100
                app.game.fireballs.opacity = 100
                app.game.cars.opacity = 100
                app.game.rockets.opacity = 100
                app.game.cannons.opacity = 100
                app.game.snowflakes.opacity = 100
            if app.game.stormActivate == True:
                if app.game.lightningRate == 0:
                    app.background = gradient('lightGray','darkGray')
                    app.game.drawLightning(randrange(0,300))
                app.game.lightningRate = randrange(0,20)
            if 500 < app.game.dayLightCycle <= 550:
                app.background = rgb(0,app.background.green-5,app.background.blue-5)
                app.game.clouds.opacity -= 2
                app.game.landscape.opacity -= 2
            if app.game.dayLightCycle == 550:
                app.game.luminescence = 0
                app.game.makeFireflies()
                app.game.fireflies.opacity = 0
            if 950 < app.game.dayLightCycle <= 1000:
                app.background = rgb(0,app.background.green+5,app.background.blue+5)
                app.game.fireflies.clear()
                app.game.clouds.opacity += 2
                app.game.landscape.opacity += 2
            if app.game.dayLightCycle > 1000:
                app.game.dayLightCycle = 0
            app.game.dayLightCycle += 1
            # Finds the other fireflies that are close, and finds the average of their centers.
            if len(app.game.fireflies) > 0:
                avg = app.game.getAverage()
                for firefly in app.game.fireflies:
                    app.game.normalize(firefly,avg)
                    if 720 < firefly.luminescence <= 900:
                        firefly.opacity = dsin(firefly.luminescence) * 100
                    if firefly.luminescence > 900:
                        firefly.luminescence = 0
                        firefly.opacity = 0
                    firefly.luminescence += 20
        if app.game.stepsPerObstacle == 40 - app.game.rounds and app.game.obstaclesSummoned != app.game.rounds:
            app.game.summonObstacle()
        if app.game.stepsPerObstacle == 200 - app.game.rounds:
            if app.game.rounds >= 20:
                app.game.title.value = 'You Win!'
                app.game.wins += 1
                app.game.showStats()
            else:
                app.game.nextRound()
        if app.game.roundsLabel.size != 30:
            app.game.roundsLabel.size -= 10
        if app.game.health <= 0:
            app.game.title.value = 'Game Over!'
            app.game.losses += 1
            app.game.showStats()
        if app.game.points >= 20:
            app.game.title.value = 'You Win!'
            app.game.wins += 1
            app.game.showStats()
        app.game.healthLabel.value = 'Health: ' + str(app.game.health)
        for fireball in app.game.fireballs:
            fireball.centerX, fireball.centerY = getPointInDir(fireball.centerX,fireball.centerY,fireball.angle,fireball.speed*2)
            if fireball.hitsShape(app.player.drawing):
                app.game.health -= 10
                app.game.fireballs.remove(fireball)
            if fireball.top >= 400:
                app.game.fireballs.remove(fireball)
        for car in app.game.cars:
            car.centerX += 5
            if car.hitsShape(app.player.drawing):
                app.game.health -= 10
                app.game.cars.remove(car)
            if car.left >= 400:
                app.game.cars.remove(car)
        for rocket in app.game.rockets:
            rocket.centerY -= 5
            if rocket.hitsShape(app.player.drawing):
                app.game.health -= 10
                app.game.rockets.remove(rocket)
            if rocket.bottom <= 0:
                app.game.rockets.remove(rocket)
        for cannon in app.game.cannons:
            if cannon.energy >= 50:
                cannon.centerX -= 1
                cannon.body.centerX -= 1
                cannon.ball.centerX += 10
                cannon.fire.visible = False
                if cannon.ball.hitsShape(app.player.drawing):
                    app.game.health -= 10
                    cannon.ball.left = 400
                if cannon.body.right <= 0:
                    cannon.visible = False
                    cannon.body.visible = False
                    cannon.ball.visible = False
            if cannon.energy == 50:
                cannon.ball.visible = True
                cannon.fire.visible = True
                cannon.ball.centerY = cannon.body.centerY
                cannon.fire.centerY = cannon.body.centerY
            if cannon.energy <= 50:
                cannon.centerX += 1
                cannon.body.centerX += 1
            cannon.energy += 1
        for snowflake in app.game.snowflakes:
            if snowflake.hitsShape(app.player.drawing):
                app.game.points += 1
                app.game.snowflakes.remove(snowflake)
        app.game.pointsLabel.value = 'Points: ' + str(app.game.points)
        app.game.stepsPerObstacle += 1

def onMousePress(mouseX,mouseY):
    # This function is called every time you left click somewhere.
    if app.game.start.hits(mouseX,mouseY) and app.game.mode == 'MENU' or app.game.again.hits(mouseX,mouseY) and app.game.mode == 'END':
        app.game.mode = 'START'
        app.game.startGame()


cmu_graphics.run()
