from data import d
from data import logo 
from data import vs
import os
import random

"""
print logo to the game
print to random ppl with the logo in between
checks the player's answer
it clears every thing out(except the logo)
if it is false it ends with sorry
else  
the the b choice becomes a and chooses another person and so on
the score increases
""" 
def finish(score):
    os.system("cls")
    print(logo)
    print(f"sorry, your final score was {score}")
def check_answer(c,o,score):
    if c["follower_count"]>=o["follower_count"]:
            #pass
        print("right! another round")
        game(c,score+1)
    else :
        finish(score)

def game(A,score):
    if A=={} :
        print(logo,f"\n your current score is:{score}\n")
        A = random.choice(d)
    #case where a and b are idetical
    B = random.choice(d)
    choice = input(f"A: {A["name"]}, a {A["description"]} from {A["country"]}\n {vs}\n B: {f"{B["name"]}, a {B["description"]} from {B["country"]}\n"}")
    #try catch
    if choice=="a"or choice=="A" or choice =="1": 
        # if A["follower_count"]>=B["follower_count"]:
        #     #pass
        #     print("right! another round")
        #     game(B,score+1)
        # else :
        #     finish(score)
        check_answer(A,B,score)
    else :
        # if A["follower_count"]<=B["follower_count"]:
        #     #pass
        #     print("right! another round")
        #     game(B,score+1)
        # else :
        #     finish(score)
        check_answer(B,A,score)
game({},0)

