# #Coding challenge 1 -Your life in weeks
# age=int(input("What is your age in years?"))
# number_of_years=90-age
# days=365
# months=12
# weeks=52
# my_life_indays=number_of_years*days
# my_life_inmonths=number_of_years*months
# my_life_inweeks=number_of_years*weeks
# output= "You have" + str(my_life_indays)+"days"+str(my_life_inmonths)+"months"+str(my_life_inweeks)+"weeks"
# print(output)

# #Coding challenge 2- Bill tip calculator
# x=float(input("Whats your bill?"))
# y=float(input("what percentage is the tip?"))
# z=int(input("how many people should the bill be split?"))
# tip=float(y/100)
# bill_with_tip1=float(x*tip)
# bill_with_tip2=float(x+bill_with_tip1)
# total_pay=round(float(bill_with_tip2/z),7)
# print("each person should pay" +" " + str(total_pay))


# #Coding challenge 3- BMI calculator

# x=float(input("weight"))
# y=float(input("heaight"))
# z=float(x/y**2)
# if z<18.5:
#     print("You are underweight")
# elif z<25 and z<30:
#     print("You are in normal weight")
# elif z<40:
#     print("Your are overweight")
# elif z<35:
#     print("You are obese")
# else:
#     print("You are clinically obese")

# #Coding challenge 4 - Leap Year calculation

# year=int(input("Enter the year you want to check"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("This is a leap year")
#         else:
#             print("This is not a leap year")
#     else:
#         print("This is a leap year")
# else:
#     print("This is not a leap year")


# #Coding challenge 5- Pizaa order program
# print("Welcome to Python Pizaa deliveries")
# size=input("What size of pizza do you want? S,M,L?").lower()
# add_pepporoni=input("Do you want to add pepperoni? Y or N").lower()
# extra_cheese=input("Do you want extra cheese? Y or N").lower()
# small=15
# medium=20
# large=25
# if size=="s":
#     final_bill= int(small)
#     if add_pepporoni=="y" and extra_cheese=="y":
#         final_bill3= int(small)+3
#         print("Your final bill is" + str(final_bill3))
#     elif extra_cheese=="n" and add_pepporoni=="n":
#         print("Your final bill is" + str(final_bill))
#     elif extra_cheese=="y" and add_pepporoni=="n":
#         final_bill4=int(small)+1
#         print("Your final bill is" + str(final_bill4))
#     elif extra_cheese=="n" and add_pepporoni=="y":
#         final_bill2=int(small)+2
#         print("Your final bill is" + str(final_bill2))
# if size=="m":
#     final_bill= int(medium)
#     if add_pepporoni=="y" and extra_cheese=="y":
#         final_bill3= int(medium)+4
#         print("Your final bill is" + str(final_bill3))
#     elif extra_cheese=="n" and add_pepporoni=="n":
#         print("Your final bill is" + str(final_bill))
#     elif extra_cheese=="y" and add_pepporoni=="n":
#         final_bill4=int(medium)+1
#         print("Your final bill is" + str(final_bill4))
#     elif extra_cheese=="n" and add_pepporoni=="y":
#         final_bill2=int(medium)+3
#         print("Your final bill is" + str(final_bill2))
# if size=="l":
#     final_bill= int(large)
#     if add_pepporoni=="y" and extra_cheese=="y":
#         final_bill3= int(large)+4
#         print("Your final bill is" + str(final_bill3))
#     elif extra_cheese=="n" and add_pepporoni=="n":
#         print("Your final bill is" + str(final_bill))
#     elif extra_cheese=="y" and add_pepporoni=="n":
#         final_bill4=int(large)+1
#         print("Your final bill is" + str(final_bill4))
#     elif extra_cheese=="n" and add_pepporoni=="y":
#         final_bill2=int(large)+3
#         print("Your final bill is" + str(final_bill2))

            
# # Coding challenge 6- Love calculator
# print("Welcome to the love calculator")
# name1=str(input("What is your name?\n")).lower()
# name2=str(input("What is their name?\n")).lower()
# count_of_true1=int(name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e"))
# count_of_true2=int(name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e"))
# total_count_of_true=count_of_true1+count_of_true2
# count_of_love1=int(name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e"))
# count_of_love2=int(name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e"))
# total_count_of_love=count_of_love1+count_of_love2
# score=str(total_count_of_true)+str(total_count_of_love)
# print("Your score is " + str(score))

# #  Coding exercise 7- Treasure Island
# print(r'''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island")
# print("Your mission is to find the treasure")
# question1=input("Where do you want to go? Left or right?").lower()
# if question1!="left":
#     print("You fell into a hole. Game over")
# else:
#     question2=input("Ok, do you want to swim or wait").lower()
#     if question2!="wait":
#         print("Attacked by trout.Game over")
#     else:
#         question3=input("Which door?.Red or Blue or Yellow?").lower()
#         if question3=="red":
#             print("Burned by fire.Game over")
#         elif question3=="blue":
#             print("Eaten by beasts.Game over")
#         elif question3=="yellow":
#             print("You win!")
#         elif question3!="red"and"blue"and"yellow":
#             print("Game over")
        

# #Coding exercise 8- Sum of all the even numbers from 1 to 100
# sum=0
# for number in range(1,101):
#     if number%2==0:
#         sum+=number
# print(sum)
    
# #Coding exercise 9- Fizzbuzz game- To print "Fizz" if the number is divisble by 3 and "Buzz if the number is divisible by 5 and Fizzbuzz if divisible by both"
# sum=0
# for number in range(1,101):
#     if number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     elif number%3==0 and number%5==0:
#         print("Fizzbuzz")
#     else:
#         print(number)
#     sum+=1

# # Coding exercise 10- Hangman game 
# # import random
# # word_list = ["aardvark", "baboon", "camel"]
# # chosen_word=random.choice(word_list)
# # print(chosen_word)
# # display=[]
# # for letter in chosen_word:
# #     display+="_"
# # print(display)
# # while "_" in display:
# #     guess =str(input("Guess a letter")).lower()
# #     for position in range(len(chosen_word)):
# #         letter=chosen_word[position]
# #         if guess==letter:
# #             display[position]=guess
# #     print(display)
# # print("You won")

#Coding exercise 11- Paint Area
# def paint_calc(height,width,cover):
#     number_of_cans=round(height*width/coverage)
#     print(f"You will need {number_of_cans} cans to paint the wall")
    
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Coding Project 12- Caesar Cipher Encryption

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text_t = input("Type your message:\n").lower()
# shift_s = int(input("Type the shift number:\n"))

# def encrypt(text,shift):
#     encrypted_message=""
#     for letter in text_t:
#         position=alphabet.index(letter)+shift_s
#         new_letter= alphabet[position]
#         encrypted_message+=new_letter
#     print(encrypted_message)


# def decrypt(text,shift):
#     decrypted_message=""
#     for letter in text_t:
#         position=alphabet.index(letter)-shift_s
#         new_letter= alphabet[position]
#         decrypted_message+=new_letter
#     print(decrypted_message)

# if direction=="encode":
#     encrypt(text=text_t, shift=shift_s)
# else:
#     decrypt(text=text_t,shift=shift_s)



#coding Project 13- Building a calculator function
# def add(n1,n2):
#     return n1+n2
# def subtract(n1,n2):
#     return n1-n2
# def multiply(n1,n2):
#     return n1*n2
# def divide(n1,n2):
#     return n1/n2

# operations={"+":add, "-":subtract, "*":multiply, "/":divide}
# num1=float(input("Whats your first number?"))
# num2=float(input("what is your second number?"))

# for symbol in operations:
#     print(symbol)
# operation_symbol=input("Pick a symbol from above")
# calculation=operations[operation_symbol]
# answer=calculation(num1,num2)
# print(answer)

# Coding project 14-Secret auction program

# bids={}
# bidding_finished = False
# def highest_bidder(bidding_record):
#     highest_bid=0
#     winner=""
#     for bidder in bidding_record:
#         bid_amount=bidding_record[bidder]
#         if bid_amount>highest_bid:
#             highest_bid=bid_amount
#             winner=bidder
#     print(f"The winner is {winner}")
# while not bidding_finished:
#     name_n=input("What is your name?")
#     bid_price_p= float(input("What is your bid price?"))
#     bids[name_n]=bid_price_p
#     bid_users_u= input("Are there any other users who want to bid?") 
#     if bid_users_u=="no":    
#         bidding_finished=True
#         highest_bidder(bids)
#     else:
#         print("Sure, let us continue")

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

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# blackjack=[11,10]
# user_card=[]
# computer_card = []
# computer_check=all(value in computer_card for value in blackjack)
# user_check=all(value in user_card for value in blackjack)

# import random 
# def deal_card_user():
#     pick=0
#     while pick<2:
#         random_card=random.choice(cards)
#         user_card.append(random_card)
#         pick+=1
#     print(user_card)
# deal_card_user()

# def deal_card_computer():
#     pick=0
#     while pick<2:
#         random_card=random.choice(cards)
#         computer_card.append(random_card)
#         pick+=1
#     print(computer_card)
# deal_card_computer()


# user_score=sum(user_card)
# computer_score=sum(computer_card)


# def calculate_user_score():
#     user_check=all(value in user_card for value in blackjack)
#     if user_check:
#         return 0
#     if "11" in user_card:
#         if user_score>=21:
#             for number in range(len(user_card)):
#                 if user_card[number]=="11":
#                     user_card[number]="1"
#                 print(user_card)
#             user_score=sum(user_card)


#     computer_check=all(value in computer_card for value in blackjack)
#     if computer_check:
#         return 0
      
#     if user_check or computer_check or sum(user_card)>=21:   
#         print("game over")
#     else:
#         ask=input("Do you want to withdraw another card?")
#         print(ask)
#         if ask=="yes":
#             random_card=random.choice(cards)
#             user_card.append(random_card)
#             print(user_card)
#             print(sum(user_card))
#             print("Ok, it is now the turn of the computer")
#         else:
#             print("Ok, wait for the game")
# calculate_user_score()



# def computer_withdraw():
#     withdraw=sum(computer_card)
#     while withdraw<17:
#         random_card=random.choice(cards)
#         computer_card.append(random_card)
#         withdraw+=random_card
#     print(computer_card)
#     print(sum(computer_card))
# computer_withdraw()

# def compare(calculate_user_score,computer_withdraw):
#     if sum(user_card)==sum(computer_card):
#         print("Draw")
#     elif computer_check==True:
#         print("You lose")
#     elif user_check==True:
#         print("You win")
#     elif sum(user_card)>21:
#         print("You lose")
#     elif sum(user_card)>sum(computer_card):
#         print("You win")
#     elif sum(computer_card)>21:
#         print("You win")
#     else:
#         print("Computer wins")
# compare(calculate_user_score,computer_withdraw)





    






    
    









