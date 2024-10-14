########################################
# Name: Diedrik
# Collaborators: Anika
# Estimated time spent (hrs): 3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT)

    """
    def my_red_rect(x,y,w,h): #red brick that I'll be placing in the middle of the window to confirm the location of the pyramid
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_fill_color("red")
        gw.add(rect)

    """

    def my_rect(x,y,w,h): #function to draw a brick
        rect = GRect(x,y,w,h)
        rect.set_filled(False)
        gw.add(rect)
    
    def draw_brick():
        for y in range(BRICKS_IN_BASE): #going down BRICKS_IN_BASE rows
            for x in range(1,y+2): #placing number of bricks on each row
                my_rect((WIDTH/2 - BRICK_WIDTH/2) - y * BRICK_WIDTH/2 + x *BRICK_WIDTH  - BRICK_WIDTH,    (HEIGHT/2 - (BRICKS_IN_BASE/2 * BRICK_HEIGHT)) + BRICK_HEIGHT * y, BRICK_WIDTH, BRICK_HEIGHT) #I somehow got the pyramid to be placed at the right location, i don't understand the math behind it, it's wo weird with the "grid" being upside down
          


    draw_brick()
    

    #my_red_rect(WIDTH//2 - BRICK_WIDTH//2, HEIGHT//2 - BRICK_HEIGHT//2, BRICK_WIDTH, BRICK_HEIGHT) #check where the middle is
    

if __name__ == '__main__':
    draw_pyramid()
