############################################################
# Name: Diedrik Boberg
# Name(s) of anyone worked with: -
# Est time spent (hr): 3
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel, GArc

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    
    def my_rect(x,y,w,h,c,f):
        rect = GRect(x,y,w,h)
        rect.set_filled(f)
        rect.set_fill_color(c)
        gw.add(rect)


    def my_line(x1,y1,x2,y2,color):
        line = GLine(x1,y1,x2,y2)
        line.set_line_width(3)
        line.set_color(color)
        gw.add(line)

    
    def my_arc(x,y,w,h,start, sweep, color):
        arc = GArc(x,y,w,h,start,sweep)
        arc.set_fill_color(color)
        arc.set_filled(True)
        gw.add(arc)
    
    def my_circ(x,y,w):
        circle = GOval(x,y,w,w)
        circle.set_fill_color("lavenderblush")
        circle.set_filled(True)
        gw.add(circle)

    def my_label(str,x,y):
        label = GLabel(str, x,y)
        label.set_color("lavenderblush")
        gw.add(label)


    for i in range(150):
        for x in range(150):
            if is_odd(x):
                my_rect(i*4, x*4, 4, 4, "blue", True)
                my_rect(2+ i*4, x*4, 4, 4, "red", True)
            else:
                my_rect(i*4, x*4, 4, 4, "red", True)
                my_rect(2+ i*4, x*4, 4, 4, "blue", True)


    for y in range(14):
        for z in range(4):
                if is_odd(y) == True:
                    my_circ(180*z,40*y,60)
                
                else:
                    my_circ(90 + 180*z, 40*y,60)
    

    for y in range(14):
        for z in range(4):
            for i in range(4):
                if is_odd(y) == True:
                    
                    my_arc(180*z,40*y,60,60,90*i-15,30,"darkviolet")
                    my_arc(180*z,40*y,60,60,90*i + 30,30,"violet")
                
                else:
                    my_arc(90 + 180*z, 40*y,60,60,90*i-15,30,"darkviolet")
                    my_arc(90 + 180*z, 40*y,60,60,90*i+30,30,"violet")


    for i in range(11):
       my_line(0,80*i,i*180,0,"mediumorchid")

    for i in range(11):
        my_line(610 - 180  *i,0,600, 80*i,"mediumorchid")
    
    for i in range(4):
        my_label("Diedrik Boberg",180*i-25,590)
    
def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    draw_image()
