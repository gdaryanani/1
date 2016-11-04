from graphics import *
import time

def main():
    win = GraphWin("test",1280,700)
#    win.setCoords(0,22,1280,750)
    #win.setBackground("blue")
    #message = Text(Point(300,400), "Hello!")
    #message.setSize(37)
    #message.setTextColor("white")
    #message.draw(win)
    #c = Circle(Point(500,500), 100)
    #c.draw(win)
    #win.getMouse()
    #time.sleep(1)
    image = Image(Point(640,387),"pic.gif")
    image.draw(win)
    win.getMouse()
    win.getMouse()

main()
