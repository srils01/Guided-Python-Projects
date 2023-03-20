# Coding project - Building a blackjack game

# Assumptions are below
# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer

#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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
#     if 11 in user_card and sum(user_card)>21:
#         for number in range(len(user_card)):
#             if user_card[number]==11:
#                 user_card[number]=1
#                 return user_score
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




# # Coding Project- Coffee Machine Project

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }




# coins={
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickles":0.05,
#     "pennies":0.01
# }

# def coffee_choice():
#         user_input= input("What would you like to have ?(espresso/latte/cappuccino)").lower()
#         while user_input!="off":
#             if user_input=="latte":
#                 if MENU["latte"]["ingredients"]["water"]>resources["water"]:
#                     print("Sorry, there is not enough water")
#                     break
#                 elif  MENU["latte"]["ingredients"]["milk"]>resources["milk"]:
#                     print("Sorry, there is not enough milk")
#                     break
#                 elif MENU["latte"]["ingredients"]["coffee"]>resources["coffee"]:
#                     print("Sorry, there is not enough coffee") 
#                     break          
#                 else:
#                     ask_user="Insert coins"
#                     print(ask_user)
#                     if ask_user:
#                         user_inserted_number_of_quarters=int(input("Enter the number of quarters inserted"))
#                         user_inserted_number_of_dimes=int(input("Enter the number of dimes inserted"))
#                         user_inserted_number_of_nickles=int(input("Enter the number of nickles inserted"))
#                         user_inserted_number_of_pennies=int(input("Enter the number of pennies inserted"))
#                         total_money_inserted=(user_inserted_number_of_quarters*coins["quarters"]+user_inserted_number_of_dimes*coins["dimes"]+user_inserted_number_of_nickles*coins["nickles"]+user_inserted_number_of_pennies*coins["pennies"])
#                         print(total_money_inserted)
#                         if total_money_inserted < MENU["latte"]["cost"]:  
#                             print("Sorry that's not enough money. Money refunded.") 
#                         elif total_money_inserted > MENU["latte"]["cost"]:
#                             print("Here is the change")
#                         elif total_money_inserted== MENU["latte"]["cost"]:
#                             order_processed="y"
#                             if order_processed:     
#                                 updated_resources_water=resources["water"]-MENU["latte"]["ingredients"]["water"]
#                                 updated_resources_milk=resources["milk"]-MENU["latte"]["ingredients"]["milk"]
#                                 updated_resources_coffee=resources["coffee"]-MENU["latte"]["ingredients"]["coffee"]
#                                 resources["water"]=updated_resources_water
#                                 resources["milk"]=updated_resources_milk
#                                 resources["coffee"]=updated_resources_coffee
#                             print("Here is your drink.Enjoy!")
#                             print("Next order")
#                             user_input= input("What would you like to have ?(espresso/latte/cappuccino)").lower()
#             elif user_input=="espresso":
#                 if MENU["espresso"]["ingredients"]["water"]>resources["water"]:
#                     print("Sorry, there is not enough water")
#                     break
#                 elif MENU["espresso"]["ingredients"]["coffee"]>resources["coffee"]:
#                     print("Sorry, there is not enough coffee") 
#                     break             
#                 else:
#                     ask_user="Insert coins"
#                     print(ask_user)
#                     if ask_user:
#                         user_inserted_number_of_quarters=int(input("Enter the number of quarters inserted"))
#                         user_inserted_number_of_dimes=int(input("Enter the number of dimes inserted"))
#                         user_inserted_number_of_nickles=int(input("Enter the number of nickles inserted"))
#                         user_inserted_number_of_pennies=int(input("Enter the number of pennies inserted"))
#                         total_money_inserted=(user_inserted_number_of_quarters*coins["quarters"]+user_inserted_number_of_dimes*coins["dimes"]+user_inserted_number_of_nickles*coins["nickles"]+user_inserted_number_of_pennies*coins["pennies"])
#                         print(total_money_inserted)
#                         if total_money_inserted < MENU["espresso"]["cost"]:  
#                             print("Sorry that's not enough money. Money refunded.") 
#                         elif total_money_inserted > MENU["espresso"]["cost"]:
#                             print("Here is the change")
#                         elif total_money_inserted== MENU["espresso"]["cost"]:
#                             order_processed="y"
#                             if order_processed:     
#                                 updated_resources_water=resources["water"]-MENU["espresso"]["ingredients"]["water"]
#                                 updated_resources_coffee=resources["coffee"]-MENU["espresso"]["ingredients"]["coffee"]
#                                 resources["water"]=updated_resources_water
#                                 resources["coffee"]=updated_resources_coffee
#                             print("Here is your drink.Enjoy!")
#                             print("Next order")
#                             user_input= input("What would you like to have ?(espresso/latte/cappuccino)").lower()
#             elif user_input=="cappuccino":
#                 if MENU["cappuccino"]["ingredients"]["water"]>resources["water"]:
#                     print("Sorry, there is not enough water")
#                     break
#                 elif  MENU["cappuccino"]["ingredients"]["milk"]>resources["milk"]:
#                     print("Sorry, there is not enough milk")
#                     break
#                 elif MENU["cappuccino"]["ingredients"]["coffee"]>resources["coffee"]:
#                     print("Sorry, there is not enough coffee") 
#                     break             
#                 else:
#                     ask_user="Insert coins"
#                     print(ask_user)
#                     if ask_user:
#                         user_inserted_number_of_quarters=int(input("Enter the number of quarters inserted"))
#                         user_inserted_number_of_dimes=int(input("Enter the number of dimes inserted"))
#                         user_inserted_number_of_nickles=int(input("Enter the number of nickles inserted"))
#                         user_inserted_number_of_pennies=int(input("Enter the number of pennies inserted"))
#                         total_money_inserted=(user_inserted_number_of_quarters*coins["quarters"]+user_inserted_number_of_dimes*coins["dimes"]+user_inserted_number_of_nickles*coins["nickles"]+user_inserted_number_of_pennies*coins["pennies"])
#                         print(total_money_inserted)
#                         if total_money_inserted < MENU["cappuccino"]["cost"]:  
#                             print("Sorry that's not enough money. Money refunded.") 
#                         elif total_money_inserted > MENU["cappuccino"]["cost"]:
#                             print("Here is the change")
#                         elif total_money_inserted== MENU["cappuccino"]["cost"]:
#                             order_processed="y"
#                             if order_processed:     
#                                 updated_resources_water=resources["water"]-MENU["cappuccino"]["ingredients"]["water"]
#                                 updated_resources_milk=resources["milk"]-MENU["lcappuccino"]["ingredients"]["milk"]
#                                 updated_resources_coffee=resources["coffee"]-MENU["cappuccino"]["ingredients"]["coffee"]
#                                 resources["water"]=updated_resources_water
#                                 resources["milk"]=updated_resources_milk
#                                 resources["coffee"]=updated_resources_coffee
#                             print("Here is your drink.Enjoy!")
#                             print("Next order")
#                             user_input= input("What would you like to have ?(espresso/latte/cappuccino)").lower()
#             elif user_input=="report":
#                 print(resources)
#                 user_input= input("What would you like to have ?(espresso/latte/cappuccino)").lower()
# coffee_choice()













