# Mini-project #6 - Blackjack

#import simplegui  #run on http://www.codeskulptor.org/
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome1 = ""
outcome2 = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.card=[]

    def add_card(self,card):
        self.card.append(card)

    def __str__(self):
        s='Hand contains :'
        for i in self.card:
            s += str(i)+' ,'
        return s

    def get_value(self):
        j=0
        have_ace=False

        for i in self.card:
            j+=VALUES[i.get_rank()]
            if VALUES[i.get_rank()] == 1:have_ace=True
        if not have_ace:
            return j
        else:
            if j+10 < 22:
                return j+10
            else:
                return j

    def draw_card(self,canvas,pos):
        tmppos=pos[:]
        if len(self.card)==0:
            return
        for i in range(0,len(self.card)):
            self.card[i].draw(canvas,tmppos)
            tmppos[0] += 90


class Deck():
    def __init__(self):
        self.deck_card=[]
        for i in SUITS:
            for j in RANKS:
                self.deck_card.append(i+j)

    def shuffle(self):
        random.shuffle(self.deck_card)

    def deal_card(self):
        i=random.randrange(0,len(self.deck_card))
        j=self.deck_card.pop(i)
        return Card(j[0],j[1])

    def __str__(self):
        return str(self.deck_card)



#define event handlers for buttons
def deal():
    global outcome1, in_play,score,deck_card,player_card,deal_card
    outcome1=''
    if in_play:
        outcome1='You give up! LOSE!'
        score -= 1
        in_play = False
    else:
        deck_card=Deck()
        player_card=Hand()
        deal_card=Hand()
        deck_card.shuffle()
        deal_card.add_card(deck_card.deal_card())
        deal_card.add_card(deck_card.deal_card())
        player_card.add_card(deck_card.deal_card())
        player_card.add_card(deck_card.deal_card())
        print 'Player ' + str(player_card)
        print 'Dealer ' + str(deal_card)
        in_play = True




def hit():
    global outcome1,score,in_play
    if in_play == True:
        player_card.add_card(deck_card.deal_card())
        print 'Player ' + str(player_card)
        print player_card.get_value()
        if player_card.get_value() > 21:
            outcome1='You have brusted'
            score -=1
            in_play=False
        else:pass
    else:pass
        

def stand():
    global outcome1,score,in_play
    if in_play == True:
        while deal_card.get_value()<17 :
            deal_card.add_card(deck_card.deal_card())
            print 'Dealer ' + str(deal_card) 
        if deal_card.get_value() == player_card.get_value():
            outcome1='Tied,but Dealer Win'
            score -=1
        elif deal_card.get_value()> 21:
            outcome1='Dealer have brusted,You Win'
        elif deal_card.get_value() > player_card.get_value():
            outcome1='Dealer Win'
            score -=1
        else:
            outcome1='Player Win'
            score +=1
        in_play=False
    else:pass


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome1,[100,50],30,'white')
    canvas.draw_text('Your Score:'+str(score),[100,500],30,'white')
    player_card.draw_card(canvas, [100, 300])
    deal_card.draw_card(canvas, [100, 100])
    canvas.draw_text('BLACKJACK',[370,50],50,'white')
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,[136,150], CARD_BACK_SIZE) 
        outcome2='Hit Or Stand?'
    else:
        outcome2='New Deal?'
        
    canvas.draw_text(outcome2,[100,250],30,'white')
        
        
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()

# remember to review the gradic rubric