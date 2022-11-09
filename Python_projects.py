#Coding challenge 1 -Your life in weeks
#age=int(input("What is your age in years?"))
#number_of_years=90-age
#days=365
#months=12
#weeks=52
#my_life_indays=number_of_years*days
#my_life_inmonths=number_of_years*months
#my_life_inweeks=number_of_years*weeks
#output= "You have" + str(my_life_indays)+"days"+str(my_life_inmonths)+"months"+str(my_life_inweeks)+"weeks"
#print(output)

#Coding challenge 2- Bill tip calculator
#x=float(input("Whats your bill?"))
#y=float(input("what percentage is the tip?"))
#z=int(input("how many people should the bill be split?"))
#tip=float(y/100)
#bill_with_tip1=float(x*tip)
#bill_with_tip2=float(x+bill_with_tip1)
#total_pay=round(float(bill_with_tip2/z),7)
#print("each person should pay" +" " + str(total_pay))


# Coding challenge 3- BMI calculator

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

#Coding challenge 4 - Leap Year calculation

#year=int(input("Enter the year you want to check"))
#if year%4==0:
    #if year%100==0:
        #if year%400==0:
            #print("This is a leap year")
        #else:
            #print("This is not a leap year")
    #else:
        #print("This is a leap year")
#else:
    #print("This is not a leap year")


#Coding challenge 5- Pizaa order program
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

            
# Coding challenge 6- Love calculator
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

#  Coding exercise 7- Treasure Island
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
        

#Coding exercise 8- Sum of all the even numbers from 1 to 100
sum=0
for number in range(1,101):
    if number%2==0:
        sum+=number
print(sum)
    
#Coding exercise 9- Fizzbuzz game- To print "Fizz" if the number is divisble by 3 and "Buzz if the number is divisible by 5 and Fizzbuzz if divisible by both"
sum=0
for number in range(1,101):
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0 and number%5==0:
        print("Fizzbuzz")
    else:
        print(number)
    sum+=1

# Coding exercise 10- Hangman game 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for letter in chosen_word:
    display+="_"
print(display)
while "_" in display:
    guess =str(input("Guess a letter")).lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=guess
    print(display)
print("You won")



        
        
        





        

            
          
    




    
    













