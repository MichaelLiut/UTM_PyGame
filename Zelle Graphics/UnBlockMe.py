# Course: Course ID
# Name:  XXXXXXXX
# Student number: 0000000
# File: UnBlockMe.py

# import names from module graphics
from graphics import *
from time import sleep
import sys

# draw the frame of the grid in the window win
# x,y are coordinates of the top left corner of the first field
def frame(x,y,win):
    p = Rectangle(Point(x-8,y-8),Point(x+248,y))
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(win)
    p = Rectangle(Point(x-8,y-8),Point(x,y+248))
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(win)
    p = Rectangle(Point(x-8,y+240),Point(x+248,y+248))
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(win)
    p = Rectangle(Point(x+240,y-8),Point(x+248,y+80))
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(win)
    p = Rectangle(Point(x+240,y+120),Point(x+248,y+248))
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(win)
#end frame

#draw the grid
def grid(win):
    x = 20
    y = 20
    for d in [40,80,120,160,200]:
        p = Line(Point(x,y+d),Point(x+240,y+d))
        p.setFill('gray')
        p.draw(win)
        p = Line(Point(x+d,y),Point(x+d,y+240))
        p.setFill('gray')
        p.draw(win)
#end grid

# returns coordinates of the top left and bottom right corners of the field with if fid
# x and y are coordinates of the left top corner of the first field
def fieldCoord(x,y,fid):
    if 1 <= fid and fid <= 6:
        return(Point(x+(fid-1)*40,y),Point(x+fid*40,y+40))
    elif 7 <= fid and fid <= 12:
        return(Point(x+(fid-7)*40,y+40),Point(x+(fid-6)*40,y+80))
    elif 13 <= fid and fid <= 18:
        return(Point(x+(fid-13)*40,y+80),Point(x+(fid-12)*40,y+120))
    elif 19 <= fid and fid <= 24:
        return(Point(x+(fid-19)*40,y+120),Point(x+(fid-18)*40,y+160))
    elif 25 <= fid and fid <= 30:
        return(Point(x+(fid-25)*40,y+160),Point(x+(fid-24)*40,y+200))
    else:
        return(Point(x+(fid-31)*40,y+200),Point(x+(fid-30)*40,y+240))
#end fieldCoord


# set field with id fid to color and green border. The type of the border is
# determined by btype
# btype '[' indicates border type for left end field of a horizontal block
# btype ']' indicates border type for right end field of a horizontal block
# btype '=' indicates border type for middle field of a horizontal block
# btype '^' indicates border type for top field of a vertical block
# btype 'v' indicates border type for bottom field of a vertical block
# btype '"' indicates border type for a middle field of a vertical block
# setField returns a list of rectangles drawn in that field
# x and y are coordinates of the top left corner of the first field
def setField(x,y,win,fid,color,border,btype): 
    tl,br = fieldCoord(x,y,fid)
    r1 = Rectangle(tl,br)
    r1.setFill(border)
    r1.draw(win)
    if btype == '[':
        p1 = Point(tl.getX()+4,tl.getY()+4)
        p2 = Point(br.getX(),br.getY()-4)
    elif btype == ']':
        p1 = Point(tl.getX(),tl.getY()+4)
        p2 = Point(br.getX()-4,br.getY()-4)
    elif btype == '^':
        p1 = Point(tl.getX()+4,tl.getY()+4)
        p2 = Point(br.getX()-4,br.getY())
    elif btype == 'v':
        p1 = Point(tl.getX()+4,tl.getY())
        p2 = Point(br.getX()-4,br.getY()-4)
    elif btype == '=':
        p1 = Point(tl.getX(),tl.getY()+4)
        p2 = Point(br.getX(),br.getY()-4)
    else:  # btype == '"'
        p1 = Point(tl.getX()+4,tl.getY())
        p2 = Point(br.getX()-4,br.getY())
    r2 = Rectangle(p1,p2)
    r2.setFill(color)
    r2.draw(win)
    return r1, r2
#end setField


# returns id of the field where the mouse click was made or 0 if the click was 
# not on any field
# x and y are coordinates of the top left corner of the first field
def whichFieldClicked(x,y,click):
    for fid in range(1,37):
        tl, br = fieldCoord(x,y,fid)
        a = tl.getX() < click.getX() and click.getX() < br.getX()
        b = tl.getY() < click.getY() and click.getY() < br.getY()
        if a and b:
            return fid
    #end for
    return 0
#end whichFieldClicked

Left = [1,7,13,19,25,31] # list of id's on leftmost column of the grid
Top = [1,2,3,4,5,6]    # list of id's on the topmost row of the grid
Right = [6,12,18,24,30,36]  # list of id's on the rightmost column of the grid
Bottom = [31,32,33,34,35,36]  # list of id's on the bottom row of the grid

# returns the id of the neighbouring field to the right of fid or 0
def rightNeighbour(fid):
    if fid in Right:
        return 0
    else:
        return fid+1
#end rightNeighbour

# returna the id of the neighbouring field to the left of fid or 0
def leftNeighbour(fid):
    if fid in Left:
        return 0
    else:
        return fid-1
#end leftNeighbour

# returns the id of the neighbouring field above fid or 0
def upNeighbour(field):
    if fid in Top:
        return 0
    else:
        return fid-6
#end upNeighbour

# returna the id of the neighbouring field below fid or 0
def downNeighbour(fid):
    if fid in Bottom:
        return 0
    else:
        return fid+6
#end downNeighbour

# returns True if fields with id's fid1 and fid2 are in the same row
def sameRow(fid1,fid2):
    if abs(fid1-fid2) < 6:
        return True
    else:
        return False
#end sameRow

# returns True if fields with id's fid1 and fid2 are in the same column
def sameColumn(fid1,fid2):
    if (abs(fid2-fid1) % 6) == 0:
        return True
    else:
        return False
#end sameColumn
        


# class Block --------------------------------------------------------
class Block:
    def __init__(self, x, y, win, fid, length, orien, color):
        self.x = x
        self.y = y
        self.win = win
        self.length = length
        self.color = color
        self.fids = [fid]
        self.hilite_flag = False
        if orien == 'h':
            r1, r2 = setField(x,y,win,fid,color,'black','[')
        else:
            r1, r2 = setField(x,y,win,fid,color,'black','^')
        self.fields = []
        self.fields.append([r1,r2])
        self.orien = orien
        if not (length == 2 or length == 3):
            win.close()
            print("wrong length of a block -- must be 2 or 3")
            sys.exit()
        if not (orien == 'h' or orien == 'v'):
            win.close()
            print("wrong orientation -- must be 'h' or 'v'")
            sys.exit()

        if orien == 'h':
            f = rightNeighbour(fid)
        else:
            f = downNeighbour(fid)
        if f == 0:
            win.close()
            print("block would stick out")
            sys.exit()
        self.fids.append(f)
        if length == 2:
            if orien == 'h':
                r1, r2 = setField(x,y,win,f,color,'black',']')
            else:
                r1, r2 = setField(x,y,win,f,color,'black','v')
            self.fields.append([r1,r2])
        else: # length == 3
            if orien == 'h':
                r1, r2 = setField(x,y,win,f,color,'black','=')
            else:
                r1, r2 = setField(x,y,win,f,color,'black','"')
            self.fields.append([r1,r2])            
            if orien == 'h':
                f = rightNeighbour(self.fids[1])
            else:
                f = downNeighbour(self.fids[1])
            if f == 0:
                win.close()
                print("block would stick out")
                sys.exit()
            self.fids.append(f)
            if orien == 'h':
                r1, r2 = setField(x,y,win,f,color,'black',']')
            else:
                r1, r2 = setField(x,y,win,f,color,'black','v') 
            self.fields.append([r1,r2])
    #end __init__
                
    def draw(self):
        self.fields[0][0].draw(self.win)
        self.fields[0][1].draw(self.win)
        self.fields[1][0].draw(self.win)
        self.fields[1][1].draw(self.win)
        if self.length == 3:
            self.fields[2][0].draw(self.win)
            self.fields[2][1].draw(self.win) 
        grid(self.win)
    #end draw
        
    def undraw(self):
        self.fields[0][0].undraw()
        self.fields[0][1].undraw()
        self.fields[1][0].undraw()
        self.fields[1][1].undraw()
        if self.length == 3:
            self.fields[2][0].undraw()
            self.fields[2][1].undraw()
        grid(self.win)
    #end undraw
    
    def hilite(self):
        if self.hilite_flag:
            return
        self.undraw()
        self.fields[0][0].setFill('green')        
        self.fields[1][0].setFill('green')
        if self.length == 3:
            self.fields[2][0].setFill('green')
        self.draw()
        self.hilite_flag = True
    #end hlite
        
    def unhilite(self):
        if self.hilite_flag == False:
            return
        self.undraw()
        self.fields[0][0].setFill('black')        
        self.fields[1][0].setFill('black')
        if self.length == 3:
            self.fields[2][0].setFill('black')
        self.draw()
        self.hilite_flag = False
    #end unhilite
        
    def switchHilite(self):
        if self.hilite_flag:
            self.unhilite()
        else:
            self.hilite()
    #end switchHilite


    # move the block to new target, the target is a list of 2 or 3 fields that the
    # block should occupy after the move
    # after the move, the block is in unhighlighted state
    def move(self,target):
        self.undraw()
        self.fids = target
        self.fields = []
        if self.orien == 'h':
            r1, r2 = setField(self.x,self.y,self.win,self.fids[0],self.color,'black','[')
        else:
            r1, r2 = setField(self.x,self.y,self.win,self.fids[0],self.color,'black','^')
        self.fields.append([r1,r2])
        if self.length == 3:
            if self.orien == 'h':
                r1, r2 = setField(self.x,self.y,self.win,self.fids[1],self.color,'black','=')
            else:
                r1, r2 = setField(self.x,self.y,self.win,self.fids[1],self.color,'black','"')
        else:
            if self.orien == 'h':
                r1, r2 = setField(self.x,self.y,self.win,self.fids[1],self.color,'black',']')
            else:
                r1, r2 = setField(self.x,self.y,self.win,self.fids[1],self.color,'black','v')
        self.fields.append([r1,r2])
        if self.length == 3:
            if self.orien == 'h':
                r1, r2 = setField(self.x,self.y,self.win,self.fids[2],self.color,'black',']')
            else:
                r1, r2 = setField(self.x,self.y,self.win,self.fids[2],self.color,'black','v')
            self.fields.append([r1,r2])
        grid(self.win)
        self.hilite_flag = False
    #endmove
#end class Block ------------------------------------------------------


# creates the initial configuration of blocks
# x and y are the coordinates of the left top corner of the first field
def initConfig(x,y,win):
    blocks = []
    b = Block(x,y,win,1,3,'h','brown')
    blocks.append(b)
    b = Block(x,y,win,9,3,'v','brown')
    blocks.append(b)
    b = Block(x,y,win,13,2,'h','red')
    blocks.append(b)
    b = Block(x,y,win,19,2,'v','brown')
    blocks.append(b)
    b = Block(x,y,win,31,3,'h','brown')
    blocks.append(b)
    b = Block(x,y,win,6,3,'v','brown')
    blocks.append(b)
    b = Block(x,y,win,23,2,'h','brown')
    blocks.append(b)
    b = Block(x,y,win,29,2,'v','brown')
    blocks.append(b)
    grid(win)
    return blocks

# returns a block that was clicked or 0 if the click was not on a block
# x and y are the coordinates of the left top corner of the first field
# blocks is a list of all blocks that are on the grid
def whichBlockClicked(x,y,click,blocks):
    fid = whichFieldClicked(x,y,click)
    if fid == 0:
        return 0
    for b in blocks:
        if fid == b.fids[0]:
            return b
        elif fid == b.fids[1]:
            return b
        if b.length == 3:
            if fid == b.fids[2]:
                return b
    #end for
    return 0
#end whichBlockClicked


# check whether block b if moved to the target would intersect any other block
# blocks is a list of all blocks that are on the grid
# returns True or False
def inter(b,blocks,target):
    for b1 in blocks:
        if b == b1:
            continue
        for i in target:
            for j in b1.fids:
                if i == j:
                    return True
        #endfor
    #endfor
    return False
#end inter


# b is a block to be moved, blocks is a list of all blocks that are on the grid
# destin is id of the field the block should be moved to
# destinOK checks if it would be a legal move, i.e. destin must be in the same
# row if it b is a horizontal block, or in the same column if b is a vertical block
# it determines if the move should be left or right, or up or down
# it checks whether moving the block would intersect with any other block using inter()
# if all is OK, destinOk returns target, i.e. the list of field id's the block should
# occupy after the move
# if the move cannot be made, destinOK returns an empty list
def destinOK(b,blocks,destin):
    if destin == b.fids[0] or destin == b.fids[1]:
        return []
    if b.length == 3:
        if destin == b.fids[2]:
            return []

    if b.orien == 'h':
        if not sameRow(b.fids[0],destin):
            return []
        if destin < b.fids[0]:
            target = [destin,destin+1]
            if b.length == 3:
                target.append(destin+2)
        else:
            if b.length == 3:
                target = [destin-2,destin-1,destin]
            else:
                target = [destin-1,destin]
        if inter(b,blocks,target):
            return []
        else:
            return target
    if b.orien == 'v':
        if not sameColumn(b.fids[0],destin):
            return []
        if destin < b.fids[0]:
            target = [destin,destin+6]
            if b.length == 3:
                target.append(destin+12)
        else:
            if b.length == 3:
                target = [destin-12,destin-6,destin]
            else:
                target = [destin-6,destin]
        if inter(b,blocks,target):
            return []
        else:
            return target
    return []
#end destinOK

# undraw all blocks on the grid
def undrawBlocks(blocks):
    for b in blocks:
        b.undraw()
#end undrawBlocks


# function main()
def main():
    win = GraphWin("Unblock me",280,280)
    x = 20
    y = 20
    frame(x,y,win)
    grid(win)
    blocks = initConfig(x,y,win)
    hilited_block = 0

    # main loop -- until the red block is succesfully moved out of grid
    while True:
        click = win.getMouse()
        if hilited_block == 0:
            b = whichBlockClicked(x,y,click,blocks)
            if b == 0:
                continue
            else:
                hilited_block = b
                hilited_block.hilite()
                continue
        else:
            fid = whichFieldClicked(x,y,click)
            if fid == 0:
                continue
            target = destinOK(hilited_block,blocks,fid)
            if target == []:
                hilited_block.unhilite()
                hilited_block = 0
                continue
            else:
                # so the move is fine, check if it is a final move
                hilited_block.move(target)
                a = hilited_block.color == 'red'
                a = a and hilited_block.fids[0] == 17
                a = a and hilited_block.fids[1] == 18
                if a:
                    for i in range(3):
                        sleep(0.3)
                        hilited_block.switchHilite()
                    undrawBlocks(blocks)
                    win.close()
                    return
                else:
                    hilited_block = 0
                continue
        #endif
    #endwhile
  #end main



# the executable part of the program starts here
main()  # execute function main()
