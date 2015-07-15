# implementation of card game - Memory
# run on http://www.codeskulptor.org/

import simplegui
import random
card=[]
expose=[]
state= 0
pair_values = []
pair_index = []
turn=0
# helper function to initialize globals
def new_game():
    global turn,card,expose
    card=[]
    expose=[]
    state= 0
    turn = 0
    for i in range(8):
        card.append(i)
        card.append(i)
        expose.append(False)
        expose.append(False)
        random.shuffle(card)
    pass


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,pair_index,pair_values,turn
    for i in range(16):
        if pos[0] < (i+1)*50:break
    if expose[i] == False:
        label.set_text("Turns = %d " %turn)
        expose[i]= True
        pair_index.append(i)
        pair_values.append(card[i])
        if state == 1:state = 2
        elif state == 2:
            if pair_values[1] != pair_values[0]:
                expose[pair_index[0]]=False
                expose[pair_index[1]]=False		
            else:pass     
            pair_values.pop(0)
            pair_values.pop(0)
            pair_index.pop(0)
            pair_index.pop(0)
            state =1
            turn += 1
        else:state = 1		
    else:pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    a=0
    for i in card:
        canvas.draw_text(str(i),[10+a*50,70],60,'black')
        a+=1
    for i in range(16):
        if not expose[i]:
            canvas.draw_image(image, (336 / 2, 500 / 2), (336 , 500), (25+i*50, 50), (50, 90))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = %d " %turn)
image = simplegui.load_image('http://www.youqudian.com/upload/you/others/2014/09/20140915172747_1edazjw2.jpg')
# register event handlers
frame.set_canvas_background('white')
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


