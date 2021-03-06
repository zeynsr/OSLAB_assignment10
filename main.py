import random
import arcade

SCREENWIDTH = 500
SCREENHEIGHT = 500
FONTSIZE=10

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREENWIDTH ,height=SCREENHEIGHT,title="SNAKE game")
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.snake = Snake()
        self.food1 = Food1()
        self.food2 = Food2()
        self.NP = NegtivePoint()

    def on_draw(self):
        arcade.start_render() 
        self.snake.draw()
        self.food1.draw()
        self.food2.draw()
        self.NP.draw()
        arcade.draw_text(f"SCORES: {self.snake.score}",8, SCREENHEIGHT - 15, arcade.color.BRIGHT_GREEN, FONTSIZE*1, width = 100, align = "left")

        if self.snake.center_x <= 0 or self.snake.center_x >= SCREENWIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREENHEIGHT  or self.snake.score < 0 :
            arcade.draw_text("Game Over!", (SCREENWIDTH // 4) - 40, SCREENHEIGHT // 2, arcade.color.ORANGE_RED, FONTSIZE*4, width = 400, align = "left")
        
            
        


    def on_key_release(self, character: int, modifiers: int):
        if character == arcade.key.LEFT :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif character == arcade.key.RIGHT :
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif character == arcade.key.UP : 
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif character == arcade.key.DOWN :
            self.snake.change_y = -1
            self.snake.change_x = 0

    def on_update(self, delta_time: float):
        self.snake.move() 

        if arcade.check_for_collision(self.snake,self.food1) :
            self.snake.eat('food1')
            self.food1 = Food1()  
            print(self.snake.score)
        elif arcade.check_for_collision(self.snake,self.food2) :
            self.snake.eat('food2')
            self.food2 = Food2()  
            print(self.snake.score) 
        elif arcade.check_for_collision(self.snake,self.NP) :
            self.snake.eat('NP')
            self.NP = NegtivePoint()  
            print(self.snake.score)       

        
    
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 16
        self.height = 16
        self.score = 0
        self.color = arcade.color.BLUE
        self.change_x = 0
        self.change_y = 0
        self.body_size = 0
        self.center_x = SCREENWIDTH //2
        self.center_y = SCREENHEIGHT//2
        self.speed = 4
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

        for i in range(len(self.body)):
            arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width,self.height,self.color)

    def eat(self,type):
        if type == 'food1':
            self.score +=1
        elif type == 'food2':
            self.score +=2      
        elif type == 'NP':
            self.score -=1   
           

    def move(self):
        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.score :
            self.body.pop(0)

        if self.change_x > 0 :
            self.center_x += self.speed
        elif self.change_x < 0 :
            self.center_x -= self.speed

        if self.change_y > 0 :
            self.center_y += self.speed
        elif self.change_y < 0 :
            self.center_y -= self.speed    
    
        
class Food1(arcade.Sprite):
    def __init__(self):
        super().__init__()

        
        self.width = 16
        self.height = 16
        self.r = 8
        self.color = arcade.color.RED
        self.center_x = random.randint(15,SCREENWIDTH-15)
        self.center_y = random.randint(15,SCREENHEIGHT-15)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)
        
class Food2(arcade.Sprite):
    def __init__(self):
        super().__init__()

        
        self.width = 16
        self.height = 16
        self.r = 8
        self.color = arcade.color.GREEN
        self.center_x = random.randint(15,SCREENWIDTH-15)
        self.center_y = random.randint(15,SCREENHEIGHT-15)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class NegtivePoint(arcade.Sprite) :
    def __init__(self) :
        super().__init__()
 
        self.r = 8
        self.color= arcade.color.DARK_BROWN
        self.width =16
        self.height=16   
        self.center_x = random.randint(15,SCREENWIDTH-15)  
        self.center_y = random.randint(15, SCREENHEIGHT-15)  

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

my_game=Game()
arcade.run()