#from tkinter.messagebox import QUESTION
from typing_extensions import Self
#from wsgiref.util import shift_path_info
from argparse import ArgumentParser
from time import time
from time import sleep
import datetime
import random 
import pandas as pd
import re
import sys
emptydict={}

class Riddler:
    """The Riddler Class represents how the game will played and the game it self
    this class will provide funtions that display the rules, starts the game and
    reads text files.
    """
    def __init__(self,rtxt,guesses,guessed_words):
        """This displays the players name.

        Args:
            player (str): Player name
        Side effects:
            displays an instance of the variable."""
        #no need to store player name 
        
        expr = r"""
        (?xm)
        ^
        (?:(?P<question_number>\d(?:\d)?\.)\s)
        (?P<question>[^?\n]+.\s)
        (?:(?P<answer>.+))
        """
        searchtxt=re.search(expr,rtxt)
        self.question_number=searchtxt.group("question_number")
        self.question=searchtxt.group("question")
        self.answer=searchtxt.group("answer")
        emptydict[self.question]=self.answer
        #add guesses to the init method and good guesses and bad guesses to be stored as a set
        #make a dictionary of the riddle and then complies them 
        #dictionary may have easier functionality 
        #need to be stored somewhere, maybe list of tuples
        #make riddle saying key
        #make value the answer
        #or make key the number
        #value be the a tuple or index zero is riddle    
    def __repr__(self):
        "Return formal riddle of the code"
        return (
            f"question_answer{self.question_number}\n"
            f"question: {self.question}\n"    
            f"answer:   {self.answer}\n")
        #find a way to break up from answer and question and print them seperately 
        
    def game_rules(rules):
        """This function displays the instruction to the player so they
            understand what tasks need to be done and the rules.
        """
        rules = f"""Welcome Player. 
        Are you ready to play The Riddler Game?
            Here are the Rules:
            
            1. You will be given a riddle, that they have to answer 
                with a  timer that goes down every second you take .
                
            2.  If you make one mistake the time goes 10 to 20 to 30 seconds 
                faster and then this will continue until the BOMB goes off or you answer the riddle correctly.
                
            3. This will happen 5 times until the user saves the city and there will be times for each bomb upcoming and there will be
                    significantly lower or harder as a riddle compared to the last one.
            
            4.The user or “Batman” if failed will have the city destroyed and
                a statement would be printed that they lose.
                Unless you win then a statement that you win will be diplayed
                """
        print(rules)

def read_riddle(r_file):
    """This takes a text file and reads the text file, then converts the 
    lines of the text file which will return the riddle given
    Args: 
        textfile
    Returns:
            Prints read riddle statement"""
    with open(r_file,"r",encoding="utf-8") as f:
        riddle_path=[Riddler(self.rtxt)(line.strip()) for line in f]
        return riddle_path
        #currently takes the riddle and opens it maybe find a way to have it only open to the riddle not answer
        #capture the question including question mark with one capturing group 
        #capture the anwser with a capturing group
        #find a way to randomize the riddles in the txtfile before being called or after 
        #need to change this to it actually making the file for the riddle a dictionary 
#def read_answer(self, a_file):
    """This takes a text file reads the text file then converts the lines
    of the text file return the answer of the riddle
    Args: 
        self: an instance of the Riddler class
        param: textfile
    Returns:
            Prints Riddle answer"""
    with open(a_file,"r",encoding="utf-8") as f:
        for line in f:
            alist=alist.append(line.strip("?",))
            return alist    
    
    
class Time(Riddler):
    """ This Time class will keep track of time and create any time deductions
    that may be taken as the user answers the riddles"""    
   
    def countdown(m):
        print(f"Be careful Batman, You'll only have 3 mins add \
            anymore time then that and the place will blow.")
        total_seconds = m * 60
        
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            if m > 3:
                break
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
    m = input("Enter the time in minutes: ")
    countdown(int(m))
 

        
    #maybe make a heart system 
    print("""Oh No! It looks like you've ran out of time.
    You set off the bomb Batman, lets see how you'll save Gotham now""")
 
    def play_game(self):
        """ This function will allow the player to guess the riddle through 
        amount of guesses. This will call the deduction method and for each bad.
            guess the deduction would be taken off. 
        Args: 
            str()s which may be the user input and holds that in until called for.
            
        Side effects: 
            displays information in the terminal.
        """
        self.game_rules()
        read_riddle()
        self.countdown()
        guess = input(" ") 
        if guess == self.answer:
            print("Well Done Batman, onto the next riddle. Let's see if you \
                 can answer this one correctly")
        elif guess != self.answer:
            print("Good Try! But your answer was WRONG... Try Again >:) ")
     
                
    def game_over(self):
        """stops game if the player answers the game correclty or the \
            time runs out."""
         
                

            
    def play_again(self):
        """ This fuction will provide the player to either continue the game
        or end the game if they get the riddle correct. If the player beats all 
        of the riddles they will recive a congratulatory message.
        Args:
        
        Side effects:
            Displays information of the winner in the terminal.
        """
        player= input("Would you like to play again <:^)")
         
        while player !="no":
             self.play_game()
        else: 
            print("Thank you for trying to save Gotham Batman you failed \
                though. ?<.,>???>?><?>?>?-Riddler")
            
        
    def wireline(self,play_answer):
        """ For this method we will be using the import time to deduct time 
        as the player begins to answer the riddle. If the answer given the 
        timer will deduct 10 seconds for 1 wrong guess, 20 for 2 and 30 for 3. 
        If the play continously answers incorrectly the timer will keep deducting 
        30 seconds until the time is up
        Args:
        
        Side effects:
            modifies the value of the "game_time" variable. (mutable)
        Returns:
            (int): an updated variable "game_time" with the deducted amount printed into the console.
         """
         #uses len(bad_guesses) =3: 
         #game_over()
        #while guess is not == play_answer 3 times:
            #print(you  done batman)
        #else:
            #print(good job batman)
        #PSEUDOCODE

        
                
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
        the parsed arguments.     
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    for riddle in r_file(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        Riddler()          
        #flow chart of how your code should flow and then structure the name block     
    

    
        #for guesses or like guess class
    #make a function that takes the guesses
    #a way to take off time from the counter when a bad guess is inputed
    #2 minutes for a guess, 1st guess takes off 10 seconds, 2nd takes off 20 seconds
    #3rd is 30 seconds. after 3rd guess every guess is 30 seconds
    

    #loop - would be inside the guessing and the time
    #loop - for the riddle (repeating the riddle)
    #if statement - if guess is correct, winner moves to next round
    #next round function - play game, rules, winner function
    #read txt file (1) - would read the file and take riddles
    #read txt file (2) - would read the file and take anwsers