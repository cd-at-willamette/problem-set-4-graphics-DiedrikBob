########################################
# Name: Diedirik Boberg
# Collaborators: Anika, Quad Center
# Estimate time spent (hrs): 3
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score


#placing a square in de center of our window for the first square
xc = GW_WIDTH/2 - SQUARE_SIZE/2
yc = GW_HEIGHT/2 - SQUARE_SIZE/2





def clicky_box():

    def on_mouse_down(event): 
        #getting my x and y cordinates from existing square
        x = sq.get_x() 
        y = sq.get_y()

        #creating random cordinates
        xs = random.randint(0,GW_WIDTH-SQUARE_SIZE)
        ys = random.randint(0,GW_HEIGHT-SQUARE_SIZE)

        #getting mouse cordinates when mouse is clicked
        xm = event.get_x()
        ym = event.get_y()
    
        #checking if mouse location is in square, and then placing the square to a random location within the window
        if xm >= x and xm <=  x + SQUARE_SIZE and ym >= y and ym <= y + SQUARE_SIZE:
            sq.set_location(xs,ys)
            gw.example += 1
            lab.set_label(str(gw.example))

        else: #setting count to zero if we didnt hit the square
                gw.example = 0
                lab.set_label(str(gw.example))

    

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    bg = GRect(0,0,GW_WIDTH,GW_HEIGHT) #creating a big rectangle to color the background
    bg.set_fill_color("darkred")
    bg.set_filled(True)
    gw.add(bg)

    
    sq = GRect(xc,yc,SQUARE_SIZE,SQUARE_SIZE) #creating my square
    sq.set_fill_color("orangered")
    sq.set_color("orangered")
    sq.set_filled(True)
    gw.add(sq)

    gw.example =  0 #adding a variable to our gw.window

    lab = GLabel(str(gw.example),SCORE_DX,GW_HEIGHT - SCORE_DY) #creating my lable
    lab.set_font(SCORE_FONT)
    lab.set_color("orangered")
    gw.add(lab)

    gw.add_event_listener("click",on_mouse_down) #event listener

if __name__ == '__main__':
    clicky_box()
