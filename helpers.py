# W-3-L-C-0-M-3   U-$-3-R
# A PROGRAMM BY TANAY NAGESH
# STUDENT OF CLASS 12TH - B
# SESSION : 2024-25 
# ROLL NO.: 16

from colorama import Fore             #this is for colour purpose  
import pandas as pd                   #module to read csv
import csv                            #module to read and edit csv file

#defining functions

def clear():                         #TO CLEAR THE SCREEN
    for i in range (0,200):
        print()
    
def R_CSV(x):                        #TO READ AND PRINT CSV FILE (PANDAS)
    print("""
          
    ____       __    ____    __ ____   __
     |   |__| [__   |    |  /__|  |   /__|
     |   |  | |__   |____]  |  |  |   |  |
 ________________________________________________________________________          
 ________________________________________________________________________         
          """)
    df=pd.read_csv(x)
    print(df)    

def R_W_csv(x):                      # TO READ WITH CSV
    print("""
          
    ____       __    ____    __ ____   __
     |   |__| [__   |    |  /__|  |   /__|
     |   |  | |__   |____]  |  |  |   |  |
 ________________________________________________________________________          
 ________________________________________________________________________         
          """)
    with open(x,"r+") as d:
     FILE = csv.reader(d)
     for i in FILE:
        print(i)
            
def info():                          #TO PRESENT THE INFO 
    print(Fore.LIGHTCYAN_EX+"""
 ______                            _______
   ||     []      []   FFFFFFFFF  |       |
   ||     || #    ||   ffffff     |       |
   ||     ||  #   ||   FFF        |       |
   ||     ||   #  ||   FFF        |       |
 __[]__   []    # []   FFF        [_______]
                             
 """)
    print(Fore.MAGENTA+"""
  ###### TITLE #### 
           
  PREPARED BY :  Tanay Nagesh
  
  OF CLASS    :  XII  - 'B'
  
  ON SUBJECT  : COMPUTER SCIENCE
          

 """)
    print(Fore.LIGHTGREEN_EX+"""
 
 __________________________________________________________________________________
 |                  -----  WHAT THIS PROJECT IS ABOUT ----                         |
 |                                                                                 |
 |  TO THE RESPECTED READER.                                                       |
 |  WE [ ME AND SOME OF MY FRIEND] CONDUCTED A MERE PSYCHOLOGICAL EXPERIMENT AT    |
 |  THE SCALE THAT WAS POSSILBE TO CONDUCT.                                        | 
 |  THE PURPOSE OF THE EXPERIMENT WAS TO IDENTIFY WHETHER WHEN WE IMAGINE THE      |
 |  IMAGE OF MEMORY OR IMAGE OF IMAGINATION, DO OUR EYES SHOW MOVEMENT OR NOT.     |
 |                                                                                 |
 |  THE PROJECT WAS INSPIRED BY A 1910 PAPER ENTITLED                              |
 |   "\x1B[3m AN EXPERIMENTAL STUDY OF IMAGINATION - by PROF. PERKY"\x1B           |
 |_________________________________________________________________________________|
 """)

def pr0():                           #TO DEFINE HOW WE COLLECTED THE DATA
    print("_"*100)
    print(Fore.CYAN+"THE PROCEUDER WAS AS SUCH :\n")
    print(Fore.WHITE+"""
   1) WE VISITED AS MANY CLASSROOM AS WE COULD
    ________________________________________________________________________________     
          
   2) WE ASKED THEM TO IMAGINE AN RED APPLE 
    ________________________________________________________________________________      
   
   3) UNBEKNOWEST TO THEM, WE WERE INTRESTED IN THEIR EYE MOVEMENT  
      AND NOT IN THEIR  IMAGINATION CAPABLITY. 
    ________________________________________________________________________________      
  
   4) AS WE EXPECTED, MOST OF OUR DATA WAS IN VAIN, AS LESS OF THEM
      TOOK IT SERIOUSLY.  
    ________________________________________________________________________________     
   
   5) WE PRIDECTED WHAT THEIR EYE-MOVEMENT MUST MEAN
    ________________________________________________________________________________      
           
   6) IF THEY SHOW MOVEMENT LIKE THEY ARE SEARCHING,IT IS MEMORY IMAGE.
    ________________________________________________________________________________  
   
   7) IF THEY SHOW NO OR VERY LESS MOVEMENT, IT IS IMAGINATION.                                    
    ________________________________________________________________________________

   8) THEN WE ASKED THE SUBJECT THEMSELVES AND MATCHED WITH OUR
     PREDICTION.
   _________________________________________________________________________________      
   
   9) IN TOTAL WE COLLECTED 37 GENUINE DATA
   _________________________________________________________________________________
   _________________________________________________________________________________                      
   """)


def MAIN_MENU():                     #THE MAIN MENU SCREEN
    print(Fore.CYAN+"_"*79)
    print(""""

 ______               _____    ______     
|  ___ \      /\     (_____)  |  ___ \    
| | _ | |    /  \       _     | |   | |   
| || || |   / /\ \     | |    | |   | |   
| || || |  | |__| |   _| |_   | |   | |   
|_||_||_|  |______|  (_____)  |_|   |_|   
                                          
 ______     _______    ______     _     _ 
|  ___ \   (_______)  |  ___ \   | |   | |
| | _ | |   _____     | |   | |  | |   | |
| || || |  |  ___)    | |   | |  | |   | |
| || || |  | |_____   | |   | |  | |___| |
|_||_||_|  |_______)  |_|   |_|   \______|

""")
    print("_"*79)
    Fore.RESET

    print("""
 
   1) VIEW RECORD 
   2) VIEW INFO
   3) VIEW PROCEDURE OF DATA COLLECTION 
   4) REDIRECT TO MAIN MENU 
   5) ADD DATA
   6) COUNT TOTAL NUMBER OF DATA    
   7) PRINT SPECIFIC COLOUMN  
   8) COUNT SPECIFIC NUMBER OF DATA
   9) EXIT 
   
 
 """)
    t = int(input("ENTER YOUR CHOICE'S CORRESPONDING NUMBER : \n"))
    return t 


def Count_specific(x):               #TO COUNT SPECIFIC DATA 
    count1 = 0
    count2 = 0
    print(Fore.YELLOW+"""
          




 what do you want to count ?
          
          1) EYE-MOVEMENT                      | (posetive V/S negetive  )
          2) PREDICTION                        | (memeory V/S imagiantion )
          3) MATCH OF PREDICTION AND INQUIRY   | (YES V/S NO )  

 """) 
      
    w = int(input("ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE : "))
    if w == 1:
        with open(x,"r+") as file:
         read = csv.reader(file)
         for line in read:
              if line[2] == "posetive":
                  count1+=1
              else:
                count2+=1   
        print("total posetive cases are : ",count1)
        print("total negetive cases are : ",count2)       
    elif w == 2:
        with open(x,"r+") as file:
         read = csv.reader(file)
         for line in read:
              if line[3] == "memory":
                  count1+=1
              else:
                count2+=1   
        print(Fore.LIGHTGREEN_EX+"total memory cases are : ",count1)
        print("total imagination cases are : ",count2)   

    if w == 3:
        with open(x,"r+") as file:
         read = csv.reader(file)
         for line in read:
              if line[5] == "yes":
                  count1+=1
              else:
                count2+=1   
        print("total cases in which the inquiry match are : ",count1)
        print("total cases in which the inquiry DID NOT match are : ",count2)       


def Gud_bye():                       #TO WISH GOODBYE 
    print(Fore.LIGHTMAGENTA_EX+"""

   _______                         __     ________
  (                                ||     |       )
  |    __    ______    _____       ||     |_______)            _____
  |   (__)  (      )  (      )  ___||     |_______     \  |   (_____)
  |    | |  (      )  (      ) |   ||     |       )     \_|   (_) _
  |____|_|  (______)  (______) |___||     |_______)       |   (____)
                                                          /
  
""")

    
def COL_print(x):                    # TO PRINT SEPCIFIC COLOUMN
    
    print("""
  select the coloumn to print specifically:
          
  1) names
  2) designation
  3) eye- movement
  4) prediction 
  5) match of prediction                                  

  

 """)
    w = int(input("enter the corresponding numeber : "))
    

    with open(x,"r+") as file :
        read = csv.reader(file)
        for line in read :
            if w <= 4:
              print(line[w-1])
            else:
                print(line[w])

    print("all the data of coloum ",w, "is succsessfully printed")
              

def thanks():                        #TO DELIVER A FINAL THANK YOU MESSAGE
    print(Fore.LIGHTCYAN_EX+"""

 _________          ____                           ____   __ 
     |     |    |  /   |  |--  |  |  /     \___/  (    )  | |  ___
     |     |----|  |---|  | -- |  |_/         /   |    |  | |  | |
     |     |    |  |   |  |  --|  | \_       /    (____)  (______)

 _______________________________________________________________________________________       

  ________________________________        
 |                                |
 |  A PROGRAMM BY: TANAY NAGESH   |
 |                                |
 |________________________________|
          
""")

####################################################
#                                                  #
#  THE PROCESSES WOULD BE HANDLED IN MAIN FILE     #
#                                                  #
#                                                  #
#  THANK YOU                                       #
#                                                  #
####################################################