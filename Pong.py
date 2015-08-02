# Implementation of classic arcade game Pong
#import simplegui  #run on http://www.codeskulptor.org/
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
paddle1_pos = [HALF_PAD_WIDTH,HALF_PAD_HEIGHT]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT-HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] = random.randrange(120, 240)
    if direction == 'left':
        ball_vel[0] = 0- random.randrange(60, 180)
    else:
        ball_vel[0] = random.randrange(60, 180)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1=0
    score2=0
    direction=random.choice(['left','right'])
    spawn_ball(direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
        
    ball_pos[0] += ball_vel[0]/60
    ball_pos[1] += ball_vel[1]/60
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'red','white')
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos[1] + paddle1_vel  <= HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    else:
        pass
    if paddle2_pos[1] + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos[1] + paddle2_vel <= HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    else:
        pass
    # draw paddles
    canvas.draw_polygon([(paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT),
                        (paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT),
                        (paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT),
                        (paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT)],1,'WHITE','GREEN')
                        
                        
                        
    canvas.draw_polygon([(paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT),
                        (paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT),
                        (paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT),
                        (paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT)],1,'WHITE','GREEN')
    # determine whether paddle and ball collide    
    #碰撞
    if ball_pos[1] - BALL_RADIUS + ball_vel[1] /60 < 0 or ball_pos[1]  + ball_vel[1] /60+ BALL_RADIUS  > HEIGHT:
        ball_vel[1] = - ball_vel[1]
    else:
        if ball_pos[0] + ball_vel[0] /60 > WIDTH - PAD_WIDTH - BALL_RADIUS:
            if paddle2_pos[1] + HALF_PAD_HEIGHT +10 > ball_pos[1] > paddle2_pos[1] - HALF_PAD_HEIGHT:
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = 1.2 * ball_vel[0]
                ball_vel[1] = 1.2 * ball_vel[1]
            else:
                score1 += 1
                spawn_ball('left')	
        
        elif ball_pos[0] + ball_vel[0] /60  < PAD_WIDTH + BALL_RADIUS: #进入左沟槽
            if paddle1_pos[1] + HALF_PAD_HEIGHT +10 > ball_pos[1] > paddle1_pos[1] - HALF_PAD_HEIGHT:
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = 1.2 * ball_vel[0]
                ball_vel[1] = 1.2 * ball_vel[1]
            else:
                score2 += 1
                spawn_ball('right') 
        else:
            pass

    # draw scores
    canvas.draw_text(str(score1),[WIDTH / 2 -100 , 100],80,'GRAY')
    canvas.draw_text(str(score2),[WIDTH / 2 +60 , 100],80,'GRAY')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -6
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 6
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -6 
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 6
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0 
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('RESTART', new_game,80)
frame.start()
