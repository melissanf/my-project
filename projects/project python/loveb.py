from tkinter import *
def on_button_click():
    import math
    from turtle import *
    pensize(2)
    def heart(k):
       return 15*math.sin(k)**3

    def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
        
    speed(100)
    #tracer(1000)
    bgcolor('black')
    for i in range(206):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(1):
        color('blue')
        style = ('Comic Sans MS', 100, 'italic')
        
    write(' ily', font=style)
    done()       
    
root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()
