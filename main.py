# !/usr/bin/env python3
##===========================================================================##
##                  F I L E     D O C U M E N T A T I O N                    ##
##===========================================================================##
##                                                                           ##
## Author:              Bryant                                               ##
##---                                                                        ##
## Title:               Palindrome                                           ##
## Filename:            main.py                                              ##
##---                                                                        ##
## Date of Creation:    05/20/22                                             ##
## Last Revised By:     N/A                                                  ##
## Last Revision Date:  05/20/22                                             ##
##                                                                           ##
## Copyright:           Copyright © 2020 Bryant.                             ##
##                      All rights reserved.                                 ##
##---------------------------------------------------------------------------##
##                                                                           ##
##- FizzBuzz Kata : Program Description:                                     ##
##                                                                           ##
## :: PROMPT ::                                                              ##
## Write a function that recieves and prints                                 ##
#  a paassed in [integer] number.                                            ##
##                                                                           ##
## :: CONSTRAINTS ::                                                         ##
## - For multiples of 3, print "FIZZ" instead of printing the number         ##
## - For multiples of 5, print "BUZZ" instead of printing the number         ##
## - For multiples of 3 & 5, print "FIZZBUZZ" instead of printing the number ##
##                                                                           ##
##---------------------------------------------------------------------------##


##===========================================================================##
##                      G L O B A L    S E C T I O N                         ##
##===========================================================================##
# -------------------------------------------------------
# Libraries/Modules                                     :
# -------------------------------------------------------
# ... import


# -------------------------------------------------------
# MACROS                                                :
# -------------------------------------------------------
# ...


# -------------------------------------------------------
# Global Variables                                      :
# -------------------------------------------------------
# ...


# -------------------------------------------------------
# Global Enumerations                                   :
# -------------------------------------------------------
# ...
# -------------------------------------------------------
# Global Lists [Structs]                                :
# -------------------------------------------------------
# ...
# -------------------------------------------------------
# Global Dictionaries [Structs]                         :
# -------------------------------------------------------
# ...
# -------------------------------------------------------
# Global Classes                                        :
# -------------------------------------------------------
# ...


# -------------------------------------------------------
# Global User-Defined Functions - Prototypes            :
# -------------------------------------------------------
import numbers


def fizzBuzz( integerVal : int ) -> str:
    """A INPUT gives an OUTPUT. Only number inputs are accepted!"""

    # Number input:
    if ( integerVal != str(integerVal) ):
        if( integerVal%3 == 0 and integerVal%5 == 0 ):
            return "FIZZBUZZ"
        else:
            if( integerVal%3 == 0 ):
                return "FIZZ"
            elif( integerVal%5 == 0 ):
                return "BUZZ"
            else:
                intToString = str( integerVal )   
                return intToString

    # Non-number input:
    else:
        return -1



    
##===========================================================================##
##                         M A I N    P R O G R A M                          ##
##===========================================================================##
# ---------------------------------------
# Main Function                         :
# ---------------------------------------
def main():
    # --------------------------------------------------------------------
    # INPUT - Variable Declaration / Initialization                      :
    # --------------------------------------------------------------------
    print('Enter a positive integer:')
    try:
#         x = int(  input() )
        x = 3
    except:
        print("An exception occurred")

    print( fizzBuzz( x ) )
    print( fizzBuzz( x ) )
    print( fizzBuzz( x ) )
    
# ---------------------------------------
# Main Function Return                  :
# ---------------------------------------
if __name__ == '__main__':
    main()

