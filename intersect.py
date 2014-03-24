""" Josh Herzberg
    CS102E
    S. Cusack
    12/5/12
    HW 12
"""

def intersect (x1, y1, x2, y2, x3, y3, x4, y4):
 try:
    ua = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/((y4-y3)*(x2-x1)-(x4-x3)*(y2-y1))

    x = x1 + ua*(x2-x1)
    y = y1 + ua*(y2-y1)
    if(between(x,x1,x2) and between(x,x3,x4) and between(y,y1,y2) and between(y,y3,y4)):
        return (x,y)
    else:
        return (None)
 except:
    return (None)

def between(n, first, second):
    if(first<=n<=second or second<=n<=first):
        return True
    else:
        return False

def edges(sx, sy, ex , ey):
    #West
    line1= (sx,sy,sx,ey)
    #South
    line2= (sx,ey,ex,ey)
    #East
    line3= (ex,ey,ex,sy)
    #North
    line4= (ex,sy,sx,sy)
    return(line1,line2,line3, line4)


def intersectAny(coords,manycoords):
    for e in manycoords:
        if intersect(*(coords+e)):
            return True
    return False

def hits(sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2):
    got_hit= []
    r1=edges(sx1,sy1,ex1,ey1)
    r2=edges(sx2,sy2,ex2,ey2)
    if intersectAny(r1[3],r2):
        got_hit.append('N')
    if intersectAny(r1[2],r2):
        got_hit.append('E')
    if intersectAny(r1[1],r2):
        got_hit.append('S')
    if intersectAny(r1[0],r2):
        got_hit.append('W')    
   
    return got_hit
             


if __name__ == '__main__':
    print( intersect( -1, 2, 1, -1, 1, 1, -2, -1 ) )
    print( intersect( -1, 2, 1, -1, 1, 1, 3, 4 ) )
    print( intersect( 1, 1, 2, 2, 1, 1, 2, 2 ) )
    print( intersect( 1, 1, 2, 2, 2, 1, 3, 2 ) )
    #box1=(1,1,10,10)
    #box2= (5,5,15,15)
    #print(edges(*box1))
    #print(intersectAny((-1, 2, 1, -1), ((1, 1, 2, 2),(1, 1, 2, 2))))
    # print( intersectAny( (1, 1, 2,11),edges(*box1) )
    #print(edges(*box1)[1])
    #print(hits(*(box1+box2)))
    box1 = ( 1, 1, 10, 10 )
    box2 = ( 0, 0, .5, .5 )
    box3 = ( 0, 0, 5, 5 )
    box4 = ( 0, 0, 11, 2 )
    box5 = ( 0, 0, 11, 11 )
    box6 = ( 3, 3, 4, 4 )
    box7 = ( 4, 0, 5, 5 )
    print( hits( *(box1+box2) ) )
    print( hits( *(box1+box3) ) )
    print( hits( *(box1+box4) ) )
    print( hits( *(box1+box5) ) )
    print( hits( *(box1+box6) ) )
    print( hits( *(box1+box7) ) )
    
