

# def single_letter_count(letter,word):
#     while word_w!="" and letter_l!="":
#         for letter in range(len(word)):
#             substring=letter_l
#             count_of_letter=word_w.count(substring)
#         print("The count of the letter in the word is :", count_of_letter)
#         return count_of_letter

# word_w=str(input("Enter the word")).lower()
# letter_l=str(input("Enter the letter you want to count")).lower()
# single_letter_count(letter_l,word_w)




#Weekly challenge 23

def contains_blue(*words):
    for word in words:
        if "blue" in word:
            return True
        else:
            return False
    

words=list(input("Enter multiple elements to check : ").split())
print(words)
print(contains_blue(words))

