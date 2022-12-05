#Coding project 15- Building a blackjack game
#Assumptions are below
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack=[11,10]
user_card=[]
computer_card = []
computer_check=all(value in computer_card for value in blackjack)
user_check=all(value in user_card for value in blackjack)

import random 
def deal_card_user():
    pick=0
    while pick<2:
        random_card=random.choice(cards)
        user_card.append(random_card)
        pick+=1
    print(user_card)
deal_card_user()

def deal_card_computer():
    pick=0
    while pick<2:
        random_card=random.choice(cards)
        computer_card.append(random_card)
        pick+=1
    print(computer_card)
deal_card_computer()


user_score=sum(user_card)
computer_score=sum(computer_card)


def calculate_user_score():
    user_check=all(value in user_card for value in blackjack)
    if user_check:
        return 0
    if "11" in user_card:
        if user_score>=21:
            for number in range(len(user_card)):
                if user_card[number]=="11":
                    user_card[number]="1"
                print(user_card)
            user_score=sum(user_card)


    computer_check=all(value in computer_card for value in blackjack)
    if computer_check:
        return 0
      
    if user_check or computer_check or sum(user_card)>=21:   
        print("game over")
    else:
        ask=input("Do you want to withdraw another card?")
        print(ask)
        if ask=="yes":
            random_card=random.choice(cards)
            user_card.append(random_card)
            print(user_card)
            print(sum(user_card))
            print("Ok, it is now the turn of the computer")
        else:
            print("Ok, wait for the game")
calculate_user_score()



def computer_withdraw():
    withdraw=sum(computer_card)
    while withdraw<17:
        random_card=random.choice(cards)
        computer_card.append(random_card)
        withdraw+=random_card
    print(computer_card)
    print(sum(computer_card))
computer_withdraw()

def compare(calculate_user_score,computer_withdraw):
    if sum(user_card)==sum(computer_card):
        print("Draw")
    elif computer_check==True:
        print("You lose")
    elif user_check==True:
        print("You win")
    elif sum(user_card)>21:
        print("You lose")
    elif sum(user_card)>sum(computer_card):
        print("You win")
    elif sum(computer_card)>21:
        print("You win")
    else:
        print("Computer wins")
compare(calculate_user_score,computer_withdraw)
