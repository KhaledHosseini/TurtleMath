import turtle
from Mibo.Helper import decimal_range

class Mibo(turtle.Turtle):
    """My own version of turtle"""
    def __init__(self,*args,**kwargs):
        super(Mibo,self).__init__(*args,**kwargs)
        self.UnitSize = 40
        self.XColor = 'blue'
        self.YColor = 'red'
        self.width = 800
        self.height = 800
        self.screen.screensize(canvwidth=self.width, canvheight=self.height)
        self.screen.bgcolor("orange")
        self.lines()
    def goto(self,x: float, y: float):
        super(Mibo, self).goto(x*self.UnitSize,y*self.UnitSize)
    
    def circle(self, radius: float):
        pos = self.position()
        self.penup()
        super(Mibo,self).goto(pos[0],pos[1] - radius * self.UnitSize)
        self.pendown()
        super(Mibo,self).circle(radius*self.UnitSize)
        self.penup()
        super(Mibo,self).goto(pos[0],pos[1])
        self.pendown()
    def recatngle(self,width: float,height: float):
        self.pendown()
        pos = self.position()
        super(Mibo,self).goto(pos[0],pos[1] + height*self.UnitSize)
        super(Mibo,self).goto(pos[0] + width * self.UnitSize, pos[1] + height*self.UnitSize)
        super(Mibo,self).goto(pos[0] + width * self.UnitSize, pos[1])
        super(Mibo,self).goto(pos[0],pos[1])

    def lines(self):
        self.pensize(1)
        self.penup();
        self.speed('fastest')
        print(self.screen.tracer)
        self.screen.tracer(0, 0)
        for x in decimal_range(-self.width*0.5/self.UnitSize,self.width*0.5/self.UnitSize,1):
            for y in decimal_range(-self.height * 0.5 / self.UnitSize,self.height*0.5 / self.UnitSize,1):
                self.penup()
                self.goto(-self.width * 0.5 / self.UnitSize,y)
                self.pencolor(self.XColor)
                self.pendown()
                self.goto(self.width*0.5 / self.UnitSize,y)
                self.penup()
                self.goto(x,-self.height*0.5 / self.UnitSize)
                self.pencolor(self.YColor)
                self.pendown()
                self.goto(x,self.height*0.5 / self.UnitSize)
                if y == 0 :
                    self.penup()
                    self.pencolor(self.XColor)
                    self.goto(x,y)
                    self.write(int(x))
                if x == 0:
                    self.penup()
                    self.goto(x,y)
                    self.pencolor(self.YColor)
                    self.write(int(y))
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.screen.update()
        self.screen.tracer(1,0)
        self.pensize(2)
        self.pencolor("black")