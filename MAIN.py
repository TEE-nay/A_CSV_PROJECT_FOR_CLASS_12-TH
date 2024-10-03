#############################
#                           #
# THIS IS THE MAIN PROGRAM  #
#                           #
#                           #
#############################

import helpers                        #importing the created module
from helpers import *                 #importing everything from the module
x= "data.csv"                         # DEFININGP A PARTICULAR VARIABLE FOR DATA 
from time import sleep

while True:                           #HANDELING EVERYTHING INSIDE A WHILE LOOP
    p = MAIN_MENU()
    if p == 1:
        print("1) VIEW WITH PANDAS.CSV ")
        print("2) VIEW WITH CSV ONLY")
        o = int(input("ENTER CHOICE -->  "))
        if o == 1:
            R_CSV(x)
            WAIT = input("PRESS ENTER TO CONTINUE : ")
            clear()
        else:
            R_W_csv(x)
            WAIT = input("PRESS ENTER TO CONTINUE : ")
            clear()
          
    elif p == 2:
        clear()
        info()
        WAIT = input("PRESS ENTER TO CONTINUE : ")
        clear()
         
    elif p == 3:
        clear()   
        pr0()
        WAIT = input("PRESS ENTER TO CONTINUE : ") 
        clear()
    
    elif p == 4:
        print("ARE YOU SURE YOU WANT TO REDIRECT?\n\n")

        WAIT = input("IF YES THEN PRINT ENTER") 
        print("REDIRECTING...")
        sleep(1.3)
        print("HERE YOU GO !")
        sleep(0.4)
        clear()
    
    elif p == 5:
        a= input("ENTER NAME  : ")
        b = input("ENTER DESIGNATION  : ")
        c = input("EYE MOVEMENT (posetive/negetive) : ")
        d = input("ENTER RESULT OF PREDICTION (memory/imagination) : ")
        e = input("RESULT WHEN INQUIRED DIRECTLY (same/different): ")
        f = input("DOES INQUIRY MATCH PREDICTION (yes/no): ")
        data = [a,b,c,d,e,f]

        with open(x,"a",newline="")as writeinto:
            new = csv.writer(writeinto)
            new.writerow(data)
            writeinto.close()
        print("DATA SUCCESSFULL APPENDED !")
        WAIT = input("press enter to continue") 
        clear() 
    
    elif p == 6:
        rows = []
        filed = []
        with open(x,"r+",newline="")as show:
            read = csv.reader(show)
            filed = next(read)
            for row in read:
                rows.append(row)

        c = read.line_num-2        
        print("\n\n\ntotal numeber of data yet collected is :",c)
        WAIT = input("press enter to continue")
        clear()

    elif p == 7 :
        print()
        COL_print(x)
        wait = input("PRESS ENTER TO CONTINUE : ")
        clear() 

                   
    elif p == 8:
        Count_specific(x)
        WAIT = input("PRESS ENTER TO CONTINUE : ")
        clear()    

    elif p == 9:
        Gud_bye()
        thanks()
        break

    else:
        print("ENTER VALID INPUT ONLY !")
        WAIT = input("PRESS ENTER TO CONTINUE : ")
        clear()

