
# coding: utf-8
import random
amount = ''
player_decision_cards = ''

### This block is creating the class for the dealer

class Dealer(object):
    hand = []

    def __init__(self, dealer_name, dealer_hand = hand, dealer_score = 0):
        self.dealer_name = dealer_name
        self.dealer_hand = dealer_hand
        self.dealer_score = dealer_score

    ## Dealer's method

    def __str__(self):
        return 'Welcome to the BlackJack! Your dealer for today is Mr. '+str(self.dealer_name)

    @staticmethod
    def createDealer():
        return Dealer(
        dealer_name = 'Denny')

    ## Need to create function to generate dealer hand
    def dealer_first_card(self):

        del self.dealer_hand[:]

        for i in range(2):
            self.dealer_hand.append(random.randrange(1,11,1))
        print 'Dealer first card ' + '[' '%s' ']' % str(self.dealer_hand[0])
        self.dealer_score = self.dealer_hand[0] + self.dealer_hand[1]

    def dealer_give_cards(self):

        while not self.dealer_score > 21:
            if self.dealer_score <= 17:
                print 'Mr. ' + str(self.dealer_name) + ': %s' % str(self.dealer_hand)
                for i in range(1):
                    self.dealer_hand.append(random.randrange(1,11,1))
                    print 'Mr. ' +str(self.dealer_name)+ "'" + 's new card is: %s' % str(self.dealer_hand[-1])
                self.dealer_score += self.dealer_hand[-1]
            else:
                break

    def dealer_checkScore(self):
        while not self.dealer_score > 21:
            print 'Mr. ' + str(self.dealer_name) + ': %s' % str(self.dealer_hand)

            if self.dealer_score == 21:
                print 'Mr. ' +str(self.dealer_name)+ ' made BlackJack!'
            else:
                print 'Mr. ' + str(self.dealer_name) +"'" + 's' +' final score is: ' + str(self.dealer_score)
            break

        while self.dealer_score > 21:
            print 'Mr. ' + str(self.dealer_name) + "'"+'s'+' final score is higher than 21.'
            break

### This block is creating the class for the Player

class Players(object):
    starting_balance = 10.0
    hand = []

    ## Player initialization and attributes
    def __init__(self, name, risk_profile, balance = int(starting_balance), score = 0, player_hand = hand):
        self.name = name
        self.balance = balance
        self.risk_profile = risk_profile
        self.score = score
        self.player_hand = player_hand


    ## Player's methods
    def showCurrentBalance(self):
        print self.balance

    @staticmethod
    def createNewPlayer():
        risk_options = ('high', 'medium', 'low')
        return Players(
        name = raw_input('Please, enter player name: '),
        risk_profile = raw_input('Please, select one of the following profile ... ' + str(risk_options)))

    def addWinnings(self, amount):
        self.balance += amount
        return

    def reduceWinnings(self, amount):
        self.balance -= amount
        return

    def checkScore(self):
        while not self.score > 21:

            if self.score == 21:
                print 'BlackJack!'

            else:
                print str(self.name) + ', your score is: ' + str(self.score)
            break

        while self.score > 21:
            print str(self.name) + ' your score is higher than 21. You loose'
            break

    def give_cards(self):
        global player_decision_cards
        del self.player_hand[:]

        for i in range(2):
            self.player_hand.append(random.randrange(1,11,1))
            print str(self.name) + ': ' + '[' + '%s' ']' % str(self.player_hand)[1:-1]
        self.score = self.player_hand[0] + self.player_hand[1]

        plyr.checkScore()

        while not self.score == 21 or len((self.player_hand) == 3):
            player_decision_cards = raw_input(str(self.name) + ' do you hit? Yes or No?').upper()

            if player_decision_cards == 'Y':
                for i in range(1):
                    self.player_hand.append(random.randrange(1,11,1))
                    print '%s' % str(self.player_hand)
                    self.score += self.player_hand[-1]
                    plyr.checkScore()
                break
            else:
                break




    def __str__(self):
        return 'Player name: %s, Risk profile: %s, Balance: %s, Player Hand: %s, Score: %s' % (self.name, self.risk_profile, float(self.balance), self.player_hand, self.score)


def bet():
    global amount
    amount = ''


    while True:
        try:
            amount = int(raw_input('Please enter your bet: '))
        except:
            print 'It looks like you did not enter a number. Retry! Please, enter a valid digit'
        else:
            if amount > plyr.balance:
                print 'You cannot bet more than your current balance!'
                print 'Your maximum bet can be up to ' + str(plyr.balance)
                continue
            elif amount == 0:
                print 'You have to bet some money!'
                break
            else:
                print 'Thank you'
                break


def end_game_check():
    global amount

    if plyr.score > dlr.dealer_score:
        if plyr.score <21:
            print str(plyr.name) + ' you win!'
            plyr.addWinnings(amount)
            print str(plyr.name) + 'your balance increases to ' + str(plyr.balance)

        elif plyr.score == 21:
            print str(plyr.name) + ' BlackJack!'
            plyr.addWinnings(amount * 1.5)
            print str(plyr.name) + 'your balance increases to ' + str(plyr.balance)

        elif plyr.score > 21 and dlr.dealer_score <= 21:
            print str(plyr.name) + ' you loose!'
            plyr.reduceWinnings(amount)
            print str(plyr.name) + ' your balance decreases to ' + str(plyr.balance)

    if plyr.score < dlr.dealer_score:
        if dlr.dealer_score <= 21:
            print str(plyr.name) + ' you loose!'
            plyr.reduceWinnings(amount)
            print str(plyr.name) + ' your balance decreases to ' + str(plyr.balance)

        elif dlr.dealer_score > 21 and plyr.score <= 21:
            print str(plyr.name) + ' you win!'
            plyr.addWinnings(amount)
            print str(plyr.name) + 'your balance increases to ' + str(plyr.balance)


    if plyr.score == dlr.dealer_score:
        print "It's a tie!"

def BlackJack():
    game_on = True
    decision = ''

    plyr = Players.createNewPlayer()
    print plyr
    dlr = Dealer.createDealer()
    print dlr

    while game_on:
        global plyr
        global dlr
        global decision


        dlr.dealer_first_card()
        bet()
        plyr.give_cards()
        dlr.dealer_give_cards()
        end_game_check()

        while not plyr.balance == 0:
            decision = raw_input(str(plyr.name)+ ' do you want to play again? ').upper()

            if decision == 'Y':
                game_on = True
                print 'Game on!'
                break
            else:
                print str(plyr.name) + ' thanks for playing BlackJack. Your available balance is ' + str(plyr.balance)
                game_on = False
                break
            break
        else:
            print str(plyr.name) + ' your balance is zero. GameOver'
            break








# In[22]:


BlackJack()
