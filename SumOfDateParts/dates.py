#!/bin/python3
# GPL something something, do what you want with this :)

# checks whether the parts of a date adds up to a target number
# e.g. 1/11/2022 -> 1 + 11 + 20 + 22 = 54


import sys
from time import sleep

def isLeap(year: int) -> int :
    res = False
    if year%4 == 0:
        res = True;
        if year%100 == 0:
            if(year%400 == 0):
                res = True;
            else:
                res = False;

    return 1 if res else 0

def main():

    MONTHS = [31, 28 ,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    startYr = 1900
    endYr = 2022
    target = 68

    helpMsg = "The arguments of the program should include a start year, end year, and a target value. \nExample \"./dates.py 1900 2022 68\".\nOr leave empty to use default values."
    try:
        argc = len(sys.argv)
        if argc == 1:
            print("Using default values (1900 2022 68).")

        elif argc == 4: 
            startYr = int(sys.argv[1])

            endYr = int(sys.argv[2]) 
            if int(sys.argv[2]) <= startYr:
                print("Your start year is greater than end year, modifying your start year to Start + 1") 
                sleep(2) # micro sleep to give user time to read
                endYr= startYr + 1

            target = int(sys.argv[3])

        else:
            raise Exception()

    except:
        print(helpMsg)
        return

    print("Starting...")
    sleep(1.5) # micro sleep to give user time to read
    print("DAY/MONTH/YEAR")
    years = []
    for year in range(startYr, endYr + 1):
        for  monthNumber, month in enumerate(MONTHS):
            for day in range(1, MONTHS[monthNumber] + 1 + (isLeap(year))):
                val = monthNumber+1 + day + int(str(year)[:2]) + int(str(year)[2:]) 
                if val == target:
                    years.append(str(day) + "/" + str(monthNumber +1 ) + "/" + (str(year)))

    
    print('\n'.join(years))
    occurance = len(years) 
    print("\nStatistics from year [" + str(startYr) + " to " + str(endYr) + "], with a target value of " + str(target) + ".")
    print("Total occurances " + str(occurance))
    print("Average occurance of " + str(occurance/365.25) + " per year between " )

if __name__ == '__main__':
    main()
