from turtle import *

def fractale(o:float, l:float):
    if o>0:
        penup()
        setposition(0,0)
        pendown()
        forward(l*1/3)
        left(60)
        forward(l*1/3)
        right(120)
        forward(l*1/3)
        pencolor("white") 
        right(120)
        forward(l*1/3)
        right(180)
        forward(l*1/3)
        pencolor("black") 
        forward(l*1/3)
        return fractale(o-1,l*1/3)

try :
    reset ()
except Terminator:
    pass
    
setup (600 ,400)
mainloop ()