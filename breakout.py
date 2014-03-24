""" Josh Herzberg
    CS102E
    S. Cusack
    12/5/12
    HW 12
"""


from tkinter import *
import time
from intersect import * #to determine when intersections happen.
from math import *
root = Tk()

class MyCanvas(Canvas):

    def makeBall( this, x, y, color="blue" ):
        return this.create_oval( x, y, x+5, y+5, fill=color )

    def moveStuff(this):
        time.sleep(.01)
        ball1coords= (sx, sy, ex, ey) = this.coords( this.ball ) #ball's location: s for start; e for end.
        rsx,rsy,rex,rey = this.coords(this.rect) #paddle's location.
        third1= rsx +16.7
        third2= rsx + 33.3
        midball1= (sx+ex)/2
		
        #this is ball1
		#determine where on paddle it hit and act accordingly.
        if((rsy<=ey and rey>=ey)):
            if(third1<=midball1<=third2):
                this.ball_velocity_y=-abs(this.ball_velocity_y)
                #print("hit middle")
            if(rsx<=sx<third1):
                if this.ball_velocity_x<0:
                    this.ball_velocity_y=-abs((this.ball_velocity_y))/1.3
                if this.ball_velocity_x>0:
                    this.ball_velocity_y=-abs((this.ball_velocity_y))*1.3
                #print("hit left")
            if(third2<ex<=rex):
                if this.ball_velocity_x<0:
                    this.ball_velocity_y=-abs((this.ball_velocity_y))/1.3
                if this.ball_velocity_x>0:
                    this.ball_velocity_y=-abs((this.ball_velocity_y))*1.3
                #print("hit right")
               
		
        if(sx <=0 or ex>=500): #ball hit a wall
            this.ball_velocity_x=-this.ball_velocity_x
            #print("hit wall")

        if(sy<=0): #hit roof
            this.ball_velocity_y=-this.ball_velocity_y
            #print("hit wall")
        #game over
        if(ey>=500):
            throw("Game Over")
       
		#this is for the blocks
        #regular Block#
        allblocks = this.find_withtag( "block")
		#can use location (e, w...) of hits to make blocks that can only be destroyed on top etc.
        for e in allblocks:
            bcoords = (bsx, bsy, bex, bey) = this.coords(e)
            if('E' in (hits(*(bcoords+ ball1coords)))):
                this.ball_velocity_x=abs(this.ball_velocity_x)
                this.delete(e)
                #print("e")
            if('W' in (hits(*(bcoords+ ball1coords)))):
                this.ball_velocity_x=-abs(this.ball_velocity_x)
                this.delete(e)
                #print("w")
            if('S' in (hits(*(bcoords+ ball1coords)))):
                this.ball_velocity_y=abs(this.ball_velocity_y)
                this.delete(e)
                #print("s")
            if('N' in (hits(*(bcoords+ ball1coords)))):
                this.ball_velocity_y=-abs(this.ball_velocity_y)
                this.delete(e)
                #print("n")

		#To make it more general (and more "strengths"), it could be a tag with a strength num.
		#then make a new block with a low strength num when hit. 
        allstrong = this.find_withtag( "strong")
        for e in allstrong:
            wcoords = (wsx, wsy, wex, wey) = this.coords(e)
            wsx, wsy, wex, wey = this.coords(e)
            if('E' in (hits(*(wcoords+ ball1coords)))):
                this.ball_velocity_x=abs(this.ball_velocity_x)
                this.delete(e)
                this.makeBlock(wsx,wsy)
                #print("e")
            if('W' in (hits(*(wcoords+ ball1coords)))):
                this.ball_velocity_x=-abs(this.ball_velocity_x)
                this.delete(e)
                #print("w")
                this.makeBlock(wsx,wsy)
            if('S' in (hits(*(wcoords+ ball1coords)))):
                this.ball_velocity_y=abs(this.ball_velocity_y)
                this.delete(e)
                #print("s")
                this.makeBlock(wsx,wsy)
            if('N' in (hits(*(wcoords+ ball1coords)))):
                this.ball_velocity_y=-abs(this.ball_velocity_y)
                this.delete(e)
                #print("n")
                this.makeBlock(wsx,wsy)
 
        if len(allblocks)==0:
            throw("YOU WIN") #b/c all blocks are gone
			
        #speedlimit# so that ball doesn't go past both borders without intersect ever catching it. 
        if this.ball_velocity_y>=5:
            this.ball_velocity_y=4
            #print("speed limit")
        if this.ball_velocity_y<=-5:
            this.ball_velocity_y=-4
            #print("speed limit")
        if this.ball_velocity_x>=5:
            this.ball_velocity_x=4
            #print("speed limit")
        if this.ball_velocity_x<=-5:
            this.ball_velocity_x=-4
            #print("speed limit")
            
        this.move( this.ball,this.ball_velocity_x,this.ball_velocity_y)
    
    def keyWasPressed(this,event=None):
            key = event.keysym
            #print("just pressed",key)
            rsx,rsy,rex,rey = this.coords(this.rect) #paddle's old location: s for start; e for end; r for rectangle;
            if(key=="Left" and rsx>0):
                this.move(this.rect, -25,0)
            if(key=="Right" and rex<500):
                this.move(this.rect,25,0)

    def makeRectangle( this, x, y, color="pink" ):
            return this.create_rectangle(x,y,x+50,y+15, fill=color)

    def makeBlock(this,x,y):
        return this.create_rectangle(x,y,x+50,y+20,tags="block",  fill="black")

    def makeStrong(this,x,y):
        return this.create_rectangle(x,y,x+50,y+20,tags="strong", fill="red")

    def mouseHasMoved( this, event ):
        # print( event.x, event.y )
        rsx,rsy,rex,rey = this.coords(this.rect) #paddle's old location: s for start; e for end; r for rectangle;
        rmiddlex= (rex + rsx)/2
        if((0<=rsx and rex<=500) or (rex>500 and (event.x - rmiddlex)<0) or (rsx<0 and (event.x - rmiddlex)>0)):
            this.move(this.rect,event.x - rmiddlex,0)

    def __init__( this, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        this.ball = this.makeBall( 200, 300 ) #the ball
        this.rect = this.makeRectangle(100,475) #the paddle
        this.bind("<KeyPress>", this.keyWasPressed)
        this.bind( "<Motion>", this.mouseHasMoved )
        this.focus_set()
        this.ball_velocity_x=3
        this.ball_velocity_y =-3
 
		#Create the bricks/blocks
        for j in range(8,100,24):
            for i in range(10,455,52):
               this.makeBlock(i,j) #regular blocks
        for j in range(103,151,24):
            for i in range(10,455,52):
                this.makeStrong(i,j) #strong blocks
        
canvas = MyCanvas( root, width=500, height=500 )
canvas.pack()

try:
    while( True ):
        canvas.moveStuff()   
        root.update()
except:
    print( "program closed" )
    # http://docs.python.org/2/library/traceback.html#traceback-examples
    import traceback, sys #error stuff
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb( exc_traceback )
