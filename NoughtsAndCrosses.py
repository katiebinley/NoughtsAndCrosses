"""
Noughts and Crosses game
Started coding: 27/01/2018
Author: Katie Binley
"""
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *


from random import randint
import sys
import os



class Window(Canvas):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Noughts and Crosses")
        window.geometry("500x500")

        self.canvas = Canvas(window)
        
        self.l1 = Label(window, text = "Click on a space to place your X!")
        self.l1.pack(anchor="center")
        
        self.b1 = Button(window, text = "End turn", width = 10, command = self.end_turn)
        self.b1.pack(anchor="center")
        
        self.canvas.create_line(100, 150, 400, 150)
        self.canvas.create_line(100, 250, 400, 250)
        self.canvas.create_line(200, 50, 200, 350)
        self.canvas.create_line(300, 50, 300, 350)
        
        self.canvas.pack(fill=BOTH, expand=1)
        
        self.b2 = Button(window, text = "Play again", width = 10, command = self.Clear_Canvas)
        self.b2.pack(anchor="center")
        
        self.b3 = Button(window, text = "Quit", width = 10, command = window.destroy)
        self.b3.pack(anchor = "center")
        
        self.playerlog = [0]
        self.complog = [0]
        self.result = 3
        global endmessage
        endmessage = 3
        
        self.canvas.bind("<Button-1>", self.Draw)
        
    
    def Clear_Canvas(Canvas):
        """ Restarts program """
        python = sys.executable
        os.execl(python, python, * sys.argv)
       
        
    def end_turn(Canvas):
            #print("button clicked")
            Canvas.CompDraw()
        
       
    """ Method to draw crosses for player """
    def Draw(Canvas, event):
        
        Canvas.x=event.x
        Canvas.y=event.y
        coords = event.x, event.y
        print(coords)
                           
        """ Set coordinates of squares on grid to assign location of player's click """
        Canvas.square1 = (100, 50, 200, 150)
        Canvas.square2 = (200, 50, 300, 150)
        Canvas.square3 = (300, 50, 400, 150)
        Canvas.square4 = (100, 150, 200, 250)
        Canvas.square5 = (200, 150, 300, 250)
        Canvas.square6 = (300, 150, 400, 250)
        Canvas.square7 = (100, 250, 200, 350)
        Canvas.square8 = (200, 250, 300, 350)
        Canvas.square9 = (300, 250, 400, 350)
        
        """ Set coordinates for crosses """
        cross1 = (125, 70, 175, 120, 150, 95, 175, 70, 125, 120)
        cross2 = (225, 70, 275, 120, 250, 95, 275, 70, 225, 120)
        cross3 = (330, 70, 380, 120, 355, 95, 380, 70, 330, 120)
        cross4 = (125, 175, 175, 225, 150, 200, 175, 175, 125, 225)
        cross5 = (225, 175, 275, 225, 250, 200, 275, 175, 225, 225)
        cross6 = (330, 175, 380, 225, 355, 200, 380, 175, 330, 225)
        cross7 = (125, 280, 175, 330, 150, 305, 175, 280, 125, 330)
        cross8 = (225, 280, 275, 330, 250, 305, 275, 280, 225, 330)
        cross9 = (330, 280, 380, 330, 355, 305, 380, 280, 330, 330)
   
        """ Winning lines coordinates """
        Canvas.line1 = (120, 95, 380, 95)
        Canvas.line2 = (120, 200, 380, 200)
        Canvas.line3 = (120, 305, 380, 305)
        Canvas.line4 = (150, 60, 150, 340)
        Canvas.line5 = (250, 60, 250, 340)
        Canvas.line6 = (355, 60, 355, 340)
        Canvas.line7 = (125, 70, 380, 330)
        Canvas.line8 = (125, 330, 380, 70)
        
        """ Draw a cross in the square that the player clicks """
        if Canvas.square1[0]<= coords[0] <= Canvas.square1[2]:
            if Canvas.square1[1]<= coords[1] <= Canvas.square1[3]:
                Canvas.canvas.create_line(cross1, width=4)
                Canvas.playerlog.append(1)
                
        
        if Canvas.square2[0]<= coords[0] <= Canvas.square2[2]:
            if Canvas.square2[1]<= coords[1] <= Canvas.square2[3]:
                Canvas.canvas.create_line(cross2, width=4)
                Canvas.playerlog.append(2)
                
        
        if Canvas.square3[0]<= coords[0] <= Canvas.square3[2]:
            if Canvas.square3[1]<= coords[1] <= Canvas.square3[3]:
                Canvas.canvas.create_line(cross3, width=4)
                Canvas.playerlog.append(3)
                
        
        if Canvas.square4[0]<= coords[0] <= Canvas.square4[2]:
            if Canvas.square4[1]<= coords[1] <= Canvas.square4[3]:
                Canvas.canvas.create_line(cross4, width=4)
                Canvas.playerlog.append(4)
                
        
        if Canvas.square5[0]<= coords[0] <= Canvas.square5[2]:
            if Canvas.square5[1]<= coords[1] <= Canvas.square5[3]:
                Canvas.canvas.create_line(cross5, width=4)
                Canvas.playerlog.append(5)
                
        
        if Canvas.square6[0]<= coords[0] <= Canvas.square6[2]:
            if Canvas.square6[1]<= coords[1] <= Canvas.square6[3]:
                Canvas.canvas.create_line(cross6, width=4)
                Canvas.playerlog.append(6)
                
        
        if Canvas.square7[0]<= coords[0] <= Canvas.square7[2]:
            if Canvas.square7[1]<= coords[1] <= Canvas.square7[3]:
                Canvas.canvas.create_line(cross7, width=4)
                Canvas.playerlog.append(7)
                
        
        if Canvas.square8[0]<= coords[0] <= Canvas.square8[2]:
            if Canvas.square8[1]<= coords[1] <= Canvas.square8[3]:
                Canvas.canvas.create_line(cross8, width=4)
                Canvas.playerlog.append(8)
                
        
        if Canvas.square9[0]<= coords[0] <= Canvas.square9[2]:
            if Canvas.square9[1]<= coords[1] <= Canvas.square9[3]:
                Canvas.canvas.create_line(cross9, width=4)
                Canvas.playerlog.append(9)
        
        """ Check for player winning line - if 3 in a row, draw line """
        if (1 in Canvas.playerlog and 2 in Canvas.playerlog and 3 in Canvas.playerlog) or (4 in Canvas.playerlog and 5 in Canvas.playerlog and 6 in Canvas.playerlog) or (7 in Canvas.playerlog and 8 in Canvas.playerlog and 9 in Canvas.playerlog) or (1 in Canvas.playerlog and 4 in Canvas.playerlog and 7 in Canvas.playerlog) or (2 in Canvas.playerlog and 5 in Canvas.playerlog and 8 in Canvas.playerlog) or (3 in Canvas.playerlog and 6 in Canvas.playerlog and 9 in Canvas.playerlog) or (1 in Canvas.playerlog and 5 in Canvas.playerlog and 9 in Canvas.playerlog) or (3 in Canvas.playerlog and 5 in Canvas.playerlog and 7 in Canvas.playerlog):
            if 1 in Canvas.playerlog and 2 in Canvas.playerlog and 3 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line1, width = 2)
            elif 4 in Canvas.playerlog and 5 in Canvas.playerlog and 6 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line2, width = 2)
            elif 7 in Canvas.playerlog and 8 in Canvas.playerlog and 8 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line3, width = 2)
            elif 1 in Canvas.playerlog and 4 in Canvas.playerlog and 7 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line4, width = 2)
            elif 2 in Canvas.playerlog and 5 in Canvas.playerlog and 8 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line5, width = 2)
            elif 3 in Canvas.playerlog and 6 in Canvas.playerlog and 9 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line6, width = 2)
            elif 1 in Canvas.playerlog and 5 in Canvas.playerlog and 9 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line7, width = 2)
            elif 3 in Canvas.playerlog and 5 in Canvas.playerlog and 7 in Canvas.playerlog:
                Canvas.canvas.create_line(Canvas.line8, width = 2)
                
            Canvas.result = 1
            Canvas.EndGame() # If player has 3 in a row, call EndGame method with Canvas.result = 1 (player won)
        
        """ If all spaces used up, end game as draw """
        if Canvas.result != 1 and len(Canvas.playerlog) > 5:
            Canvas.result = 2
            Canvas.EndGame()
        
    
    def CompDraw(Canvas):
        
        """Create coordinates for computer circles"""
        circle1 = (130, 80, 170, 120)
        circle2 = (230, 80, 270, 120)
        circle3 = (330, 80, 370, 120)
        circle4 = (130, 180, 170, 220)
        circle5 = (230, 180, 270, 220)
        circle6 = (330, 180, 370, 220)
        circle7 = (130, 285, 170, 325)
        circle8 = (230, 285, 270, 325)
        circle9 = (330, 285, 370, 325)
        
        """Create random number 1-9 from spaces available on the current board"""
        Canvas.randomno = 0
        while Canvas.randomno in Canvas.complog or Canvas.randomno in Canvas.playerlog:
            Canvas.randomno = randint(1, 9)
        
        """Now draw circle corresponding to random number picked"""
        if Canvas.randomno == 1:
            Canvas.canvas.create_oval(circle1, width=4, outline="#ff1c2e")
            Canvas.complog.append(1)
            
        elif Canvas.randomno == 2:
            Canvas.canvas.create_oval(circle2, width=4, outline="#ff1c2e")
            Canvas.complog.append(2)
       
        elif Canvas.randomno == 3:
            Canvas.canvas.create_oval(circle3, width=4, outline="#ff1c2e")
            Canvas.complog.append(3)
        
        elif Canvas.randomno == 4:
            Canvas.canvas.create_oval(circle4, width=4, outline="#ff1c2e")
            Canvas.complog.append(4)
       
        elif Canvas.randomno == 5:
            Canvas.canvas.create_oval(circle5, width=4, outline="#ff1c2e")
            Canvas.complog.append(5)
        
        elif Canvas.randomno == 6:
            Canvas.canvas.create_oval(circle6, width=4, outline="#ff1c2e")
            Canvas.complog.append(6)
        
        elif Canvas.randomno == 7:      
            Canvas.canvas.create_oval(circle7, width=4, outline="#ff1c2e")
            Canvas.complog.append(7)
        
        elif Canvas.randomno == 8:
            Canvas.canvas.create_oval(circle8, width=4, outline="#ff1c2e")
            Canvas.complog.append(8)
        
        elif Canvas.randomno == 9:
            Canvas.canvas.create_oval(circle9, width=4, outline="#ff1c2e")
            Canvas.complog.append(9)
        
        
        """ Check for computer winning line - if 3 in a row, draw line """
        if (1 in Canvas.complog and 2 in Canvas.complog and 3 in Canvas.complog) or (4 in Canvas.complog and 5 in Canvas.complog and 6 in Canvas.complog) or (7 in Canvas.complog and 8 in Canvas.complog and 9 in Canvas.complog) or (1 in Canvas.complog and 4 in Canvas.complog and 7 in Canvas.complog) or (2 in Canvas.complog and 5 in Canvas.complog and 8 in Canvas.complog) or (3 in Canvas.complog and 6 in Canvas.complog and 9 in Canvas.complog) or (1 in Canvas.complog and 5 in Canvas.complog and 9 in Canvas.complog) or (3 in Canvas.complog and 5 in Canvas.complog and 7 in Canvas.complog):
            if 1 in Canvas.complog and 2 in Canvas.complog and 3 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line1, width = 2)
            elif 4 in Canvas.complog and 5 in Canvas.complog and 6 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line2, width = 2)
            elif 7 in Canvas.complog and 8 in Canvas.complog and 9 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line3, width = 2)
            elif 1 in Canvas.complog and 4 in Canvas.complog and 7 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line4, width = 2)
            elif 2 in Canvas.complog and 5 in Canvas.complog and 8 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line5, width = 2)
            elif 3 in Canvas.complog and 6 in Canvas.complog and 9 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line6, width = 2)
            elif 1 in Canvas.complog and 5 in Canvas.complog and 9 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line7, width = 2)
            elif 3 in Canvas.complog and 5 in Canvas.complog and 7 in Canvas.complog:
                Canvas.canvas.create_line(Canvas.line8, width = 2)
            
            Canvas.result = 0
            Canvas.EndGame() # If computer has 3 in a row, call EndGame method with Canvas.result = 0 (comp won)
        
    
    """ Method to call relevant class depending on final result of game """
    def EndGame(Canvas):
        
        if Canvas.result == 0:
            #print("Sorry, you lost!")
            endmessage = 0
            Canvas.end = tk.Toplevel(Canvas.window)
            Canvas.app = EndWindowLose(Canvas.end)
        elif Canvas.result == 1:
            #print("Congratulations, you won!")
            endmessage = 1
            Canvas.end = tk.Toplevel(Canvas.window)
            Canvas.app = EndWindowWin(Canvas.end)
        elif Canvas.result == 2:
            #print("Draw!")
            endmessage = 2
            Canvas.end = tk.Toplevel(Canvas.window)
            Canvas.app = EndWindowDraw(Canvas.end)


""" Player lost outcome """
class EndWindowLose(Canvas):
    def __init__(self, window2):
        self.window2 = window2
        self.window2.wm_title("Game over")
        window2.geometry("250x50")
            
        l1 = Label(window2, text = "Sorry, you lost!")
        l1.pack(anchor="center")
        

""" Player won outcome """
class EndWindowWin(Canvas):
    def __init__(self, window3):
        self.window3 = window3
        self.window3.wm_title("Game over")
        window3.geometry("250x50")
            
        l1 = Label(window3, text = "Congratulations, you won!!")
        l1.pack(anchor="center")
        
""" Draw outcome """        
class EndWindowDraw(Canvas):
    def __init__(self, window4):
        self.window4 = window4
        self.window4.wm_title("Game over")
        window4.geometry("250x50")
            
        l1 = Label(window4, text = "Draw!")
        l1.pack(anchor="center")
        

window = Tk()
app = Window(window)
window.mainloop()
###

