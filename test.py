from graphics import *
import time

def main():
    win = GraphWin("test",1280,710)
    win.setBackground("blue")
    message = Text(Point(300,400), "Hello!")
    message.setSize(37)
    message.setTextColor("white")
    message.draw(win)
    c = Circle(Point(500,500), 100)
    c.draw(win)
    win.getMouse()
    time.sleep(1)

main()
