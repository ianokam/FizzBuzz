"""AN EXAMPLE TEST MODULE"""
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/ibeawuchi/.jenkins/workspace/FizzBuzz-Python/src/program_package')
# import main
from main import fizzBuzz


class Test_for_a_str_number:
    def test_1( self ) -> int :
        """ Test Definition: A Return Value can be found of the same value as 
            the input is found"""
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 1          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "1"


##===========================================================================##

class Test_for_multiplesOfThree:
    def test_1( self ):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 3          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "FIZZ"

    def test_2( self ):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 6          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "FIZZ"
    
    def test_3( self ):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 24          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "FIZZ"
 

##===========================================================================##

class Test_for_multiplesOfFive:
    def test_1(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 5          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "BUZZ"

    def test_2(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 10          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "BUZZ"
    
    def test_3(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 25          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "BUZZ"


##===========================================================================##

class Test_for_multiplesOfThreeAndFive:
    def test_1(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 270          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "FIZZBUZZ"

        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 450          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "FIZZBUZZ"


##===========================================================================##

class Test_for_numberInputs_only:
    def test_1(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = 8          # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == "8"

    def test_2(self):
        # --------------------------------------------------------------------
        # DUMMY INPUT - Variable Declaration / Initialization                :
        # --------------------------------------------------------------------
        integerVal = "8"        # Integer
        # --------------------------------------------------------------------
        # DUMMY OUTPUT                                                       :
        # --------------------------------------------------------------------
        assert fizzBuzz(integerVal) == -1
