# template for "Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# define global variables
time=0
clock=0
success=0
total=0
score=str('0/0')
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global clock,time
    d = time % 10
    c = time / 10 % 10
    b = time / 100 % 6
    a = time / 600
    clock = str(str(a)+'.'+str(b)+str(c)+'.'+str(d))

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global time,total,success
    timer.start()

    
def stop_handler():
    global score,total,success
    timer.stop()
    total +=1
    if time % 10 == 0:
        success += 1
    else:
        pass
 
    
def reset_handler():
    global time
    time = 0
    success = 0
    total =0
    timer.stop()



# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1       

    
# define draw handler
def draw_handler(canvas):
    global clock,success,total
    format()
    canvas.draw_text(str(clock),[100,120],50,'red', "serif")
    canvas.draw_text(str(str(success)+'/'+str(total)),[280,40],30,'green')

# create frame
frame = simplegui.create_frame('game',350,200)
    
# register event handlers
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw_handler)
button_start=frame.add_button('start',start_handler,90)
label1 = frame.add_label('')
button_stop=frame.add_button('stop',stop_handler,90)
label2 = frame.add_label('')
bbutton_reset=frame.add_button('reset',reset_handler,90)


# start frame
frame.start()

# Please remember to review the grading rubric
