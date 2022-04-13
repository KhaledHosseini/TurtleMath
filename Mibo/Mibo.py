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
        self.drawCoordinateSystem()
    
    def goto(self,x: float, y: float):
        super(Mibo, self).goto(x*self.UnitSize,y*self.UnitSize)
    
    def circle(self, radius: float):
        pos = self.position()
        self.pendown()
        super(Mibo,self).goto(pos[0],pos[1] - radius * self.UnitSize*0.5)
        self.penup()
        super(Mibo,self).goto(pos[0] + 0.1,pos[1] - radius * self.UnitSize*0.5)
        self.pendown()
        self.write(radius,font=("Arial", 20, 'bold', 'italic'))
        self.penup()
        super(Mibo,self).goto(pos[0],pos[1] - radius * self.UnitSize*0.5)
        self.pendown()
        super(Mibo,self).goto(pos[0],pos[1] - radius * self.UnitSize)
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
        self.penup()
        self.pensize(4)
        super(Mibo,self).goto(pos[0]  - width * self.UnitSize * 0.05 ,pos[1] + height*self.UnitSize * 0.5)
        self.write(height,font=("Arial", 20, 'bold', 'italic'))
        super(Mibo,self).goto(pos[0] + width * self.UnitSize * 0.5, pos[1] + height*self.UnitSize * 1.05)
        self.write(width,font=("Arial", 20, 'bold', 'italic'))
        self.pensize(2)
        super(Mibo,self).goto(pos[0],pos[1])
        self.pendown()

    def recatngleAreaAnimation(self,width: float,height: float):
        shape = turtle.Shape('compound')
        p = self.position()
        #poly = ((p[0],p[1]),(p[0],p[1]+height*self.UnitSize),(p[0]+self.UnitSize,p[1]+height*self.UnitSize),(p[0]+self.UnitSize,p[1]))
        poly = ((0,0),(0,self.UnitSize),(-self.UnitSize,self.UnitSize),(-self.UnitSize,0))
        shape.addcomponent(poly,'green','yellow')
        self.screen.register_shape('rectangle', shape)
        turtles = []
        for i in range(height):
            t = turtle.Turtle(shape='rectangle')
            t.speed(1)
            t.penup()
            t.goto(p[0],p[1]+self.UnitSize*i)
            turtles.append(t)
        #self.screen.tracer(0, 0)
        for j in range(width-1):
            for t in turtles:
                t.speed(1)
                t.forward(self.UnitSize)
            #self.screen.update()
        self.screen.tracer(1,0)

    def drawCoordinateSystem(self):
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
                    self.goto(x+0.1,y+0.1)
                    self.write(int(x),font=("Arial", 12, 'normal', 'italic'))
                if x == 0:
                    self.penup()
                    self.goto(x+0.1,y)
                    self.pencolor(self.YColor)
                    self.write(int(y),font=("Arial", 12, 'normal', 'italic'))
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.screen.update()
        self.screen.tracer(1,0)
        self.pensize(2)
        self.pencolor("black")